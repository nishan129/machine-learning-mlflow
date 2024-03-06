from src.mlploject.config.configuration import ConfigurationManager
from src.mlploject.components.data_transformation import DataTransformation
from src.mlploject import logger


STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeLine:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.train_test_spliting()
        except Exception as e:
            raise e
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeLine()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
    except Exception as e:
        logger.exception(e)