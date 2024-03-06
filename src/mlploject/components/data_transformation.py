import pandas as pd
from src.mlploject import logger
from sklearn.model_selection import train_test_split
from src.mlploject.config.configuration import DataTransformationConfig
import os

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
        
    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)
        
        # split the data into training and test set split
        
        train, test = train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index= False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)
        
        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)
        
        # print(train.shape)
        # print(test.shape)