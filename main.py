from intent.pipeline.stage_01_data_ingestion import * 
from intent.pipeline.stage_02_data_validation import *

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"\n\n\n>>>>>> Stage {STAGE_NAME} started <<<<<<\n\n\n")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"\n\n\n>>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx=======================================================x\n\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f"\n\n\n>>>>>> Stage {STAGE_NAME} started <<<<<<\n\n\n")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"\n\n\n>>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n\nx=======================================================x\n\n\n")
except Exception as e:
    logger.exception(e)
    raise e