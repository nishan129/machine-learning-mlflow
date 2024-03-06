from src.mlploject import logger
from src.mlploject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlploject.pipeline.stage_02_data_validation import DataValidationTrainingPipeLine
from src.mlploject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeLine
from src.mlploject.pipeline.stage_04_model_trainer import ModelTrainerPipeline
STAGE_NAME = "Model Trainer stage"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainerPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)