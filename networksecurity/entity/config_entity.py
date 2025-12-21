from networksecurity.constants import training_pipeline
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logging import logger
import os
from  datetime import datetime
import sys

class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        try:
            logger.info("Training pipeline config class initialized")

            self.timestamp=timestamp.strftime("%d_%m_%Y_%H_%M_%S")

            self.pipeline_name=training_pipeline.PIPELINE_NAME

            self.artifact_dir_name=training_pipeline.ARTIFACT_DIR_NAME
            self.artifact_dir=os.path.join(self.artifact_dir_name,self.timestamp)
            os.makedirs(self.artifact_dir,exist_ok=True)

        except Exception as e:
            logger.error(e)
            raise NetworkSecurityException(e,sys)




class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            logger.info("Data Ingestion Config class initialized")
            self.artifact_dir=training_pipeline_config.artifact_dir

            self.data_ingestion_dir_name=training_pipeline.DATA_INGESTION_DIR_NAME
            self.data_ingestion_dir=os.path.join(self.artifact_dir,self.data_ingestion_dir_name)
            os.makedirs(self.data_ingestion_dir,exist_ok=True)

            self.feature_store_dir_name=training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR_NAME
            self.feature_store_dir=os.path.join(self.data_ingestion_dir,self.feature_store_dir_name)
            os.makedirs(self.feature_store_dir,exist_ok=True)

            self.ingested_dir_name=training_pipeline.DATA_INGESTION_INGESTED_DIR_NAME
            self.ingested_dir=os.path.join(self.data_ingestion_dir,self.ingested_dir_name)
            os.makedirs(self.ingested_dir,exist_ok=True)

            self.row_data_file_name=training_pipeline.ROW_DATA_FILE_NAME
            self.row_data_file_path=os.path.join(self.feature_store_dir,self.row_data_file_name)

            self.train_data_file_name=training_pipeline.TRAIN_FILE_NAME
            self.train_file_path=os.path.join(self.ingested_dir,self.train_data_file_name)

            self.test_data_file_name=training_pipeline.TEST_FILE_NAME
            self.test_file_path=os.path.join(self.ingested_dir,self.test_data_file_name)

            self.train_test_split_ratio=training_pipeline.TRAIN_TEST_SPLIT_RATIO

            self.mongo_db_url=training_pipeline.MONGO_DB_URL
            self.mongo_db_collection_name=training_pipeline.MONGO_DB_COLLECTION_NAME
            self.mongo_db_database_name=training_pipeline.MONGO_DB_DATABASE_NAME

            logger.info("Data Ingestion Configuration Completed")

        except Exception as e:
            logger.error(e)
            raise NetworkSecurityException(e,sys)

