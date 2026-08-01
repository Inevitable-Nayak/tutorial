import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os
import sys
import pandas as pd
import dill
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException
import warnings
warnings.filterwarnings("ignore")
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
def evaluate_model(x_train, y_train, x_test, y_test, models, params):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]
            grid_search = GridSearchCV(estimator=model,param_grid=param,cv=3)
            grid_search.fit(x_train, y_train)
            model.set_params(**grid_search.best_params_)
            model.fit(x_train, y_train)
            # Predict Testing data
            y_test_pred = model.predict(x_test)
            # Predict Training data
            y_train_pred = model.predict(x_train)
            # Evaluate model on training and testing data
            train_r2_square = r2_score(y_train, y_train_pred)
            test_r2_square = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_r2_square
        return report
    except Exception as e:
        raise CustomException(e, sys)
def load_data(file_path):
    try:
        with(open(file_path,'rb'))  as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)       