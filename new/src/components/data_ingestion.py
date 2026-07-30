import pandas as pd
import numpy as np
import os 
import sys
import logging
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','data.csv')
class DataIngestion:
    def __init__(self):
        self.data_ingestion=DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info('enter the data ingestion method or component')
        try:
            df=pd.read_csv('notebook/data/stud.csv')
            os.makedirs(os.path.dirname(self.data_ingestion.raw_data_path),exist_ok=True)
            df.to_csv(self.data_ingestion.raw_data_path,index=False,header=True)
            logging.info('train test split initiated')
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.data_ingestion.train_data_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion.test_data_path,index=False,header=True)
            logging.info('ingestion of the data is completed')
            return(
                self.data_ingestion.train_data_path,
                self.data_ingestion.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
