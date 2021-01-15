import logging
import sys

event_logs = "lakehouse.log"


def getlogger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setLevel(level)
    file_handler = logging.FileHandler(event_logs)
    file_handler.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)15s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger
