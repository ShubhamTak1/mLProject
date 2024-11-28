import logging
import os
from datetime import datetime 

# Generate a log file name with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the logs directory and file path
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging setup
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Fixed the parameter name
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Fixed 'formate' typo
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")


if __name__=="__main__":
    logging.info("Logging has started")