from src.mlploject import logger
from src.mlploject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlploject.pipeline.stage_02_data_validation import DataValidationTrainingPipeLine
from src.mlploject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeLine
STAGE_NAME = "Data Transformation stage"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataTransformationTrainingPipeLine()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)