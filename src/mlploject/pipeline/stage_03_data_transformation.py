from src.mlploject.config.configuration import ConfigurationManager
from src.mlploject.components.data_transformation import DataTransformation
from src.mlploject import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeLine:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]
                
            if status == "True":
                
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
        except:
            raise Exception("You data schema is not valid") 
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeLine()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
    except Exception as e:
        logger.exception(e)