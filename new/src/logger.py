import logging
import os
from datetime import datetime
LOG_file=f"{datetime.now().strftime('%M%H%D%M%Y')}.log"
logs_path=os.path.join(os.getcwd(), "logs", LOG_file)
os.mkdir(logs_path,exist_ok=True)
log_file_path=os.path.join(logs_path,LOG_file)
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)