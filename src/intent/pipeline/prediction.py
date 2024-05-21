import os
from intent.config.configuration import *
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
from datasets import load_dataset


class PredictionPipeline:
    def __init__(self):
        config = config.get_model_evaluation_config()
    
    def predict(self, text):
        try:
            banking77_label_dict_rev  = {}
            banking77_label = load_dataset("json", data_files = os.path.join(self.config.data_path, "categories.json"))
            for key, value in enumerate(banking77_label["train"]["text"]):
                    banking77_label_dict_rev[key] = value
            def label2category(x):
                return banking77_label_dict_rev[x]            
            model = AutoModelForSequenceClassification.from_pretrained(self.config.model_path)
            tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
            pipe = pipeline("text-classification", model = model, tokenizer = tokenizer)
            print("Query: ")
            print(text)
            category = str(pipe(text)[0]["label"]).split("_")[1]
            print(category)
            predicted_intent = label2category(int(category))
            return predicted_intent
        except Exception as e:
            return e