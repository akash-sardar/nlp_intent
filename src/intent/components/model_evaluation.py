import os
import pandas as pd
from intent.logging import logger
from intent.entity import *


from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import Trainer
from datasets import load_from_disk, load_dataset
from sklearn.metrics import f1_score, accuracy_score
import torch

class ModelEvaluation:
    def __init__(self, config:ModelEvaluationConfig):
        self.config = config
    
    def evaluate(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        test_dataset_encoded = load_from_disk(os.path.join(self.config.transformed_data_path, "test_dataset_encoded"))
        test_dataset = pd.read_csv(os.path.join(self.config.data_path, "test.csv"))
        banking77_label = load_dataset("json", data_files = os.path.join(self.config.data_path, "categories.json"))
        banking77_label_dict  = {}
        for key, value in enumerate(banking77_label["train"]["text"]):
            banking77_label_dict[value] = key
        def category2label(x):
            return banking77_label_dict[x]
        test_dataset["category_name"] = test_dataset["category"].apply(category2label)

        model = AutoModelForSequenceClassification.from_pretrained(self.config.model_path).to(device)
        trainer = Trainer(model = model)
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        preds_output = trainer.predict(test_dataset_encoded)
        y_preds = preds_output.predictions.argmax(-1)  
        y_test = test_dataset["category_name"]   
        test_results = pd.DataFrame()
        test_results["text"] = pd.Series(test_dataset["text"])
        test_results["category_name"] = pd.Series(test_dataset["category_name"])
        test_results["predicted_category"] = y_preds
        test_results.to_csv(os.path.join(self.config.root_dir, "eval_results.csv"), index = False)
        score_df = pd.DataFrame(self.evaluate_metrics(y_preds, y_test), index=[0])
        score_df.to_csv(self.config.metric_file_name)      


    def evaluate_metrics(self, y_preds, y_test):
        labels = y_test
        preds = y_preds
        f1 = f1_score(labels, preds, average= "weighted")
        acc = accuracy_score(labels, preds)
        return {"f1" : f1, "accuracy" : acc}