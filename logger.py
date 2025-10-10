# logger.py

import logging
import os
from datetime import datetime

# --- Configuration ---
LOG_DIR_NAME = "logs"
LOG_FILENAME = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Create the full path for the logs directory
# os.getcwd() gets the current working directory, which is your project's root
logs_path = os.path.join(os.getcwd(), LOG_DIR_NAME)
os.makedirs(logs_path, exist_ok=True)

# Define the full path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILENAME)


# --- Setup Logger ---
# This configures the root logger. 
# Any logger instance created later will inherit this configuration.
logging.basicConfig(
    # The format string defines how each log message will look
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    
    # The minimum level of messages to be logged. INFO includes INFO, WARNING, ERROR, CRITICAL.
    level=logging.INFO,

    # A list of handlers to send the log messages to
    handlers=[
        logging.FileHandler(LOG_FILE_PATH), # Handler to write logs to a file
        logging.StreamHandler()             # Handler to write logs to the console
    ]
)

# Create a logger instance that you can import in other modules
# Using a specific name helps in identifying the source of logs in complex apps.
logger = logging.getLogger("SelfSupervisedLearningLogger")

# Example of how to use it (optional, for testing)
# if __name__ == "__main__":
#     logger.info("Logger setup complete. This is an informational message.")
#     logger.warning("This is a warning message.")
#     logger.error("This is an error message.")