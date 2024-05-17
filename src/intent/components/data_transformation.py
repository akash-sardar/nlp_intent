from intent.config.configuration import *
import os
from intent.logging import logging
from transformers import AutoTokenizer
from datasets import load_dataset, Dataset

class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def transform_data(self):
        banking77 = load_dataset("csv", data_files = { "train" : os.path.join(self.config.data_path, "train.csv"), 
                                                        "test" : os.path.join(self.config.data_path, "test.csv")})
        banking77_categories = load_dataset("json", data_files = os.path.join(self.config.data_path, "categories.json"))
        banking77_categories_dict  = {}
        for key, value in enumerate(banking77_categories["train"]["text"]):
                banking77_categories_dict[value] = key
        train_df = banking77["train"].to_pandas()
        test_df = banking77["test"].to_pandas()
        # changing the labels to label_ids
        def category2label(x):
            return banking77_categories_dict[x]

        train_df["category_name"] = train_df["category"].apply(category2label)
        test_df["category_name"] = test_df["category"].apply(category2label)
        train_dataset = Dataset.from_pandas(train_df[["text", "category_name"]])
        test_dataset = Dataset.from_pandas(test_df[["text", "category_name"]])
        def tokenize(batch):
            return self.tokenizer(batch["text"], padding = True, truncation = True, return_tensors = "pt")        
        train_dataset_encoded = train_dataset.map(tokenize, batched = True, remove_columns = ["text"])
        train_dataset_encoded = train_dataset_encoded.rename_column("category_name", "labels")
        test_dataset_encoded = test_dataset.map(tokenize, batched = True, remove_columns = ["text"])
        test_dataset_encoded = test_dataset_encoded.rename_column("category_name", "labels") 

        train_dataset_encoded.save_to_disk(os.path.join(self.config.root_dir, "train_dataset_encoded"))
        test_dataset_encoded.save_to_disk(os.path.join(self.config.root_dir, "test_dataset_encoded"))