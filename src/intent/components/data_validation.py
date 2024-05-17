# define components
import os
from intent.logging import logger
from intent.config.configuration import *

class DataValidation:
    def __init__(self, config:DataValidationConfig):
        self.config = config   

    def validate_all_files_exists(self) -> bool:
        try:
            validation_status = None
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion"))
            for file in self.config.ALL_REQUIRED_FILES:
                if file not in all_files:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation Status: {validation_status} for file {file}")
                    break 
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status:{validation_status} for all required files")
            return validation_status
        except Exception as e:
            raise e