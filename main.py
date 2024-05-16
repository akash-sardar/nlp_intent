from intent.pipeline.stage_01_data_ingestion import * # type: ignore

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<") # type: ignore
    data_ingestion = DataIngestionTrainingPipeline() # type: ignore
    data_ingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx=======================================================x\n\n") # type: ignore
except Exception as e:
    logger.exception(e) # type: ignore
    raise e
