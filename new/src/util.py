import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os
import sys
import pandas as pd
import dill
from src.exception import CustomException
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
def evaluate_model(x_train, y_train, x_test, y_test, models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            # Train model
            model.fit(x_train, y_train)
            # Predict Testing data
            y_test_pred = model.predict(x_test)
            # Predict Training data
            y_train_pred = model.predict(x_train)
            # Evaluate model on training and testing data
            train_mae, train_rmse, train_r2_square = evaluate_model(y_train, y_train_pred)
            test_mae, test_rmse, test_r2_square = evaluate_model(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_r2_square
        return report
    except Exception as e:
        raise CustomException(e, sys)