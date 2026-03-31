import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s" # Define the logging format for the application. It includes the timestamp, log level, module name, and the log message itself.

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    format=logging_str,
    level=logging.INFO,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]

)

logger = logging.getLogger("cnnClassifier") 