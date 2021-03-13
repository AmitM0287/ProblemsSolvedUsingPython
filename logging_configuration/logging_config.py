"""
logging configuration
"""
import logging


def get_logger():
    """
    get_logger(): This function sets the logging configuration. It returns a logger.
    Using this logger we can put the exceptions or etc. in the log file.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    # set the logging format
    formatter = logging.Formatter('%(asctime)s : %(name)s : ', datefmt='%m/%d/%Y %I:%M:%S %p')
    # adding a exception.log file
    file_handler = logging.FileHandler('exceptions.log')
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger