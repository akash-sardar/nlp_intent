import os
from intent.logging import logger
from intent.config.configuration import *

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import Trainer, TrainingArguments
from datasets import load_from_disk
from sklearn.metrics import f1_score, accuracy_score
import torch

class ModelTrainer:
    def __init__(self, config:ModelTrainerConfig):
        self.config = config
    
    def compute_metrics(self, pred):
        labels = pred.label_ids
        preds = pred.predictions.argmax(-1)
        f1 = f1_score(labels, preds, average= "weighted")
        acc = accuracy_score(labels, preds)
        return {"f1" : f1, "accuracy" : acc}
    
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        num_labels = 77
        model = AutoModelForSequenceClassification.from_pretrained(self.config.model_ckpt, num_labels = num_labels).to(device)
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        train_dataset_encoded = load_from_disk(os.path.join(self.config.data_path, "train_dataset_encoded"))
        test_dataset_encoded = load_from_disk(os.path.join(self.config.data_path, "test_dataset_encoded"))

        training_args = TrainingArguments(
            output_dir = os.path.join(self.config.root_dir, "training_output_directory"),
            num_train_epochs = self.config.num_train_epochs,
            per_device_train_batch_size = self.config.per_device_train_batch_size,
            per_device_eval_batch_size = self.config.per_device_eval_batch_size,
            weight_decay = self.config.weight_decay,
            logging_steps = self.config.logging_steps,
            evaluation_strategy = self.config.evaluation_strategy,
            disable_tqdm = self.config.disable_tqdm,
            log_level = self.config.log_level,
            learning_rate = self.config.learning_rate,
           
        )
        trainer = Trainer(model = model,
                          args = training_args,
                          compute_metrics = self.compute_metrics,
                          train_dataset = train_dataset_encoded,
                          eval_dataset = test_dataset_encoded,
                          tokenizer = tokenizer
                          )
        
        trainer.train()
        model.save_pretrained(os.path.join(self.config.root_dir, f"{self.config.model_ckpt}-finetuned-banking77"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer-finetuned-banking77"))