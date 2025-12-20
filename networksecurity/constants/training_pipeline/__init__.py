from dotenv import load_dotenv
load_dotenv('.env')

import os



# Some common constant for training pipeline
TARGET_COLUMN:str="result"
TRAIN_TEST_SPLIT_RATIO:float=0.2
ROW_DATA_FILE_NAME="data.csv"
TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"
PIPELINE_NAME:str="NETWORK SECURITY"
ARTIFACT_DIR_NAME:str="Artifacts"

# Data Ingestion pipeline's constants
MONGO_DB_URL=os.getenv("MONGO_DB_URL")
MONGO_DB_COLLECTION_NAME=os.getenv("MONGO_DB_COLLECTION_NAME")
MONGO_DB_DATABASE_NAME=os.getenv("MONGO_DB_NAME")
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR_NAME:str="feature_store"
DATA_INGESTION_INGESTED_DIR_NAME:str="ingested_data"
