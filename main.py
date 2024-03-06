from src.mlploject import logger
from src.mlploject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlploject.pipeline.stage_02_data_validation import DataValidationTrainingPipeLine
STAGE_NAME = "Data Validation stage"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeLine()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)