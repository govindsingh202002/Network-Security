import sys
from networksecurity.logging.logging import logger
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.artifact_entity import DataIngestionArtifact
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from datetime import datetime
import pandas as pd
from pymongo import MongoClient
from sklearn.model_selection import train_test_split

class DataIngestion:
    def __init__(self,data_ingestion_artifact:DataIngestionArtifact,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            logger.error(e)
            raise NetworkSecurityException(e,sys)

    def get_data_from_mongo_db(self):
        try:
            self.mongo_db_url=self.data_ingestion_config.mongo_db_url
            self.mongo_db_collection_name=self.data_ingestion_config.mongo_db_collection_name
            self.mongo_db_database_name=self.data_ingestion_config.mongo_db_database_name

            self.mongo_db_client=MongoClient(self.mongo_db_url)
            self.mongo_db_database=self.mongo_db_client[self.mongo_db_database_name]
            self.mongo_db_collection=self.mongo_db_database[self.mongo_db_collection_name]

            return self.mongo_db_collection.find()

        except Exception as e:
            logger.error(e)
            raise NetworkSecurityException(e,sys)

    def convert_data_into_dataframe(self,cursor_data):
        try:
            df=pd.DataFrame(list(cursor_data))
            df.drop(columns=['_id'],axis=1)
            return df
        except Exception as e:
            logger.error(e)
            raise NetworkSecurityException(e,sys)
        
        
    def save_row_dataframe_in_feature_store(self,dataframe):
        try:
            self.row_data_file_path=self.data_ingestion_artifact.row_data_file_path
            print(self.row_data_file_path)
            dataframe.to_csv(self.row_data_file_path,index=False,header=True)
        except Exception as e:
            logger.error(e)
            raise NetworkSecurityException(e,sys)
        
    def split_and_save_train_test_data(self,dataframe):
        try:
            self.train_test_split_ratio=self.data_ingestion_config.train_test_split_ratio
            self.train_file_path=self.data_ingestion_config.train_file_path
            self.test_file_path=self.data_ingestion_config.test_file_path
            print(self.train_file_path)
            print(self.test_file_path)
            train_data,test_data=train_test_split(dataframe,test_size=self.train_test_split_ratio,random_state=42)

            train_data.to_csv(self.train_file_path,index=False,header=False)
            test_data.to_csv(self.test_file_path,index=False,header=False)

        except Exception as e:
            logger.error(e)
            raise NetworkSecurityException(e,sys)

    def initiate_data_ingestion(self):
        try:
            logger.info("data ingestion initiated")
            self.mongodb_cursor_format_data=self.get_data_from_mongo_db()
            logger.info("data fetched successfully from mongo db")
            self.row_data_in_dataframe=data_ingestion.convert_data_into_dataframe(self.mongodb_cursor_format_data)
            logger.info("Cursor format data converted into dataframe")
            self.save_row_dataframe_in_feature_store(self.row_data_in_dataframe)
            logger.info("Row data saved at feature store directory")
            self.split_and_save_train_test_data(self.row_data_in_dataframe)
            logger.info("Row data splitted into train test and saved at corresponded directories")

        except Exception as e:
            logger.error(e)
            raise NetworkSecurityException(e,sys)




if __name__=="__main__":
    training_pipeline_config=TrainingPipelineConfig(datetime.now())
    data_ingestion_config=DataIngestionConfig(training_pipeline_config)
    data_ingestion_artifact=DataIngestionArtifact(data_ingestion_config)
    data_ingestion=DataIngestion(data_ingestion_artifact,data_ingestion_config)
    data_ingestion.initiate_data_ingestion()

