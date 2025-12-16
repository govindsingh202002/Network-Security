import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

#get directory of this logging file 
base_dir= os.path.dirname(os.path.abspath(__file__))
# define log folder directory path
log_dir=os.path.join(base_dir,"..","..","logs")
os.makedirs(log_dir,exist_ok=True)
# define log file path name
log_file_name = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
log_file_path=os.path.join(log_dir,log_file_name)

# creating a log formatter
log_formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

#create rotating file handler 
file_handler=RotatingFileHandler(
    filename=log_file_path,
    maxBytes=5*1024*1024,
    backupCount=5,
    encoding="utf-8"
)
file_handler.setFormatter(log_formatter)
file_handler.setLevel(logging.DEBUG)

#create logger

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
if not logger.handlers:
    logger.addHandler(file_handler)
    #logger  →  handler  →  formatter  →  file
    
logger.propagate=False