import logging
import sys

def initialize_logger(logger_name, file_name):
    logger = logging.getLogger(logger_name)
    handler = logging.StreamHandler(sys.stdout)
    f_handler = logging.FileHandler(file_name)
    formatter = logging.Formatter('{"logger_time": "%(asctime)s", "logger_name": "%(name)s", "logger_level":"%(levelname)s", "logger_properties": %(message)s}')
    f_handler.setFormatter(formatter)
    handler.setFormatter(formatter)
    f_handler.setLevel(logging.ERROR)
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.addHandler(f_handler)
    return logger


logging.basicConfig(level=logging.INFO)

logging.debug('Message with level: debug') 
logging.info('Message with level: info') 
logging.warning('Message with level: warning') 
logging.error('Message with level: error') 
logging.critical('Message with level: critical')

logger = initialize_logger("my_test_logger", file_name='my_log_file.log')
logger.info('Message with level: info')
logger.warning('Message with level: warning')
logger.error('Message with level: error') 
logger.critical('Message with level: critical')

# initialize a logger with level debug and format like [time]: loggername loggerlevel message


