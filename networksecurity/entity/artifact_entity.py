from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.logging.logging import logger
from networksecurity.exception.exception import NetworkSecurityException
import sys

class DataIngestionArtifact:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logger.info("Data Ingestion Artifact called")
            self.row_data_file_path:str=data_ingestion_config.row_data_file_path
            self.train_file_path:str=data_ingestion_config.train_file_path
            self.test_file_path:str=data_ingestion_config.test_file_path
        except Exception as e:
            logger.error(e)
            raise NetworkSecurityException(e,sys)