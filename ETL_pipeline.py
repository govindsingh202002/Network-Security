from pymongo import MongoClient
import os
import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logging import logger
import pandas as pd
import json
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

# server connection is CA certified/verified
import certifi
certifi.where()

"""
load dataset from local --> convert this dataset into json format ---> upload this dataset on mongodb 

"""
class NetworkDataExtract:
    def __init__(self):
        try:
            self.mongo_db_url=os.getenv("MONGO_DB_URL")
            self.mongo_db_name=os.getenv("MONGO_DB_NAME")
            self.mongo_db_collection_name=os.getenv("MONGO_DB_COLLECTION_NAME")
            
            logger.info("Network data Extract class object initialised")
        except Exception as e:
            logger.error(e)
            raise NetworkSecurityException(e,sys)
        
    def load_csv_file(self,csv_file_path):
        try:
            df=pd.read_csv(csv_file_path)
            df.reset_index(drop=True,inplace=True)
            return df
        except Exception as e:
            logger.error(e)
            raise NetworkSecurityException(e,sys)
    
    def convert_csv_data_into_json(self,dataframe):
        try:
            json_data=list(json.loads(dataframe.T.to_json()).values())
            return json_data
        except Exception as e:
            logger.error(e)
            raise NetworkSecurityException(e,sys)

    def push_data_into_mongo_db(self,csv_file_path):
        try:
            self.csv_file_path=csv_file_path
            self.dataframe=self.load_csv_file(self.csv_file_path)
            logger.info("loaded the .csv file data")
            self.json_data=self.convert_csv_data_into_json(self.dataframe)
            logger.info("converted csv dataframe data into json data")
            self.mongodb_client=MongoClient(self.mongo_db_url)
            logger.info("Mongo client create and connected to mongodb")
            self.database=self.mongodb_client[self.mongo_db_name]
            self.collection=self.database[self.mongo_db_collection_name]
            self.collection.insert_many(self.json_data)
            logger.info("Json data uploaded into mongodb client")

        except Exception as e:
            logger.error(e)
            raise NetworkSecurityException(e,sys)


if __name__=="__main__":
    networkdataextract_object=NetworkDataExtract()
    networkdataextract_object.push_data_into_mongo_db(r"C:\Users\Rajera\Desktop\Network Security\Network_data\phisingData.csv")

        
