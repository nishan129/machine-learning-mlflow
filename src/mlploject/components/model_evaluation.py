import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from src.mlploject.config.configuration import ModelEvaluationConfig
from src.mlploject.utils.common import save_json
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        
    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mse = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        
        return rmse, mse, r2
    
    
    def log_into_mlflow(self):
        
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]
        
        mlflow.set_registry_uri(self.config.mtflow_uri)
        tracking_url_type_stor = urlparse(mlflow.get_tracking_uri()).scheme
        
        
        with mlflow.start_run():
            
            predict_qualities = model.predict(test_x)
            
            (rmse, mse, r2) = self.eval_metrics(test_y, predict_qualities)
            
            # saving matrics as loacal
            
            score = {"rmse": rmse, "mse": mse, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=score)
            
            mlflow.log_params(self.config.all_params)
            
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2",r2)
            mlflow.log_metric("mae", mse)
            
            
            # model registry does not work with file store
            
            if tracking_url_type_stor != "file":
                
                
                
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElsticnetModel")
            else:
                mlflow.sklearn.log_model(model, "model")
            