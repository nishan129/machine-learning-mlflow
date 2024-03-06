from src.mlploject.config.configuration import ConfigurationManager
from src.mlploject.components.model_trainer import ModelTrainer
from src.mlploject import logger
from pathlib import Path


STAGE_NAME = "Model Trainer Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
                
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer  = ModelTrainer(config= model_trainer_config)
            model_trainer.train()
        except:
            raise Exception("You data schema is not valid") 
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
    except Exception as e:
        logger.exception(e)
