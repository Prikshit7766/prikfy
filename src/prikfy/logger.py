import os 
import sys
import logging


logging_str='[%(asctime)s: %(levelname)s: %(module)s]: %(message)s'
log_dir="./logs"
log_filepath = os.path.join(log_dir,"runnig_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
                    level=logging.INFO,
                    format=logging_str,
                    handlers=[logging.FileHandler(log_filepath), # this will print logs in file   
                              logging.StreamHandler(sys.stdout)] # this will print logs on console as well as in file
                    
                    )


logger=logging.getLogger("prikfy")



