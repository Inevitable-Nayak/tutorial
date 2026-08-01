import numpy as np
import pandas as pd
import sys
from src.exception import CustomException
from src.util import load_data
class predictpipeline:
    def __init__(self):
        pass    
    def predict(self,features):
        
        model_path='artifacts/model.pkl'
        preprocessor_path='artifacts/preprocessor.pkl'
        model=load_data(model_path)
        preprocessor=load_data(preprocessor_path)
        data_scaled=preprocessor.transform(features)
        model_prediction=model.predict(data_scaled)
        return model_prediction

class customdata:
    def __init__(self,gender:int,race_ethnicity:int,parental_level_of_education,lunch:int,test_preparation_course:int,reading_score:int,writing_score:int):
        self.gender=gender
        self.race_Ethnicity=race_ethnicity
        self.parental_level_of_education=parental_level_of_education
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict={
                'gender':[self.gender],
                'race_ethnicity':[self.race_Ethnicity],
                'parental_level_of_education':[self.parental_level_of_education],
                'lunch':[self.lunch],
                'test_preparation_course':[self.test_preparation_course],
                'reading_score':[self.reading_score],
                'writing_score':[self.writing_score]
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)