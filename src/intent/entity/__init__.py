# This block will be moved to entity

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen = True)
class DataValidationConfig:
    root_dir : Path
    STATUS_FILE : str
    ALL_REQUIRED_FILES : list

@dataclass(frozen = True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path

@dataclass(frozen = True)
class ModelTrainerConfig:
    root_dir: Path
    data_path : Path
    model_ckpt : Path
    num_train_epochs : int
    learning_rate : float
    per_device_train_batch_size : int
    per_device_eval_batch_size : int
    weight_decay : float
    evaluation_strategy : str
    disable_tqdm : bool
    logging_steps : int
    log_level : str   

@dataclass(frozen = True)
class ModelEvaluationConfig:
    root_dir : Path
    transformed_data_path : Path
    data_path : Path
    model_path : Path
    tokenizer_path : Path
    metric_file_name : Path    