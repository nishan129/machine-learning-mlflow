from src.mlploject.config.configuration import ConfigurationManager
from src.mlploject.components.data_validation import DataValidation
from src.mlploject import logger

STAGE_NAME = "Data Validation Stage"


class DataValidationTrainingPipeLine:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeLine()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
    except Exception as e:
        logger.exception(e)