import os
import sys
import logging
from datetime import datetime
from from_root import from_root


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"



log_filepath = os.path.join(from_root(),"logs", LOG_FILE)

os.makedirs(log_filepath,exist_ok=True)

LOG_FILE_PATH = os.path.join(log_filepath, LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s]%(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO,
)

logger = logging.getLogger("mlPtojectLogger")