from catboost import CatBoostRegressor
import pandas as pd
import numpy as np
import os 
import sys
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.util import save_object, evaluate_model
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.exception import CustomException
from src.logger import logging
from src.util import save_object
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
class modeltrainerconfig:
    def __init__(self):
        self.trained_model_file_path=os.path.join('artifacts','model.pkl')
class modeltrainer:
    def __init__(self) :
        self.model_trainer_config=modeltrainerconfig()
        def initiate_model_trainer(self,train_array,test_array):
            try:
                logging.info('splitting training and test input data')
                x_train,y_train,x_test,y_test=(
                    train_array[:, :-1], train_array[:, -1], test_array[:, :-1], test_array[:, -1]
                )
                models = {
                    "Random Forest": RandomForestRegressor(),
                    "Decision Tree": DecisionTreeRegressor(),
                    "Gradient Boosting": GradientBoostingRegressor(),
                    "Linear Regression": LinearRegression(),
                    "K-Neighbors": KNeighborsRegressor(),
                    "XGBoost": XGBRegressor(),
                    "CatBoost": CatBoostRegressor(),
                    "AdaBoost": AdaBoostRegressor()
                }
                model_report:dict=evaluate_model(x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test,models=models)
                best_model_score=max(sorted(model_report.values()))
                best_model_name=list(model_report.keys())[
                    list(model_report.values()).index(best_model_score)
                ]
                best_model=models[best_model_name]
                if best_model<0.6:
                    raise CustomException('No best model found')
                logging.info('best model found on both training and testing dataset')
                save_object(file_path=self.model_trainer_config.trained_model_file_path,obj=best_model)
                predicted=best_model.predict(x_test)
                mae, rmse, r2_square = evaluate_model(y_test, predicted)
                return mae, rmse, r2_square
            except Exception as e:
                raise CustomException(e,sys)