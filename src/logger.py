# this file is used to log whatever happens - every execution, error raised etc so that we can trace what happened
import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# the log file will be a text file created with name as current date's month,day,year and time's hr,min,sec
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)  # cwd - current working directory
# the log path should include cwd,the log file name preceded with the word logs
os.makedirs(logs_path,exist_ok=True)  #mkdirs - make directories
# says that even though there exists a folder logs_path keep appending to it everytime a file is created 

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

'''
if __name__=="__main__":
    logging.info("Logging has started")
'''