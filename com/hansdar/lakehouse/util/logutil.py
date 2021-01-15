import logging
import sys

event_logs = "lakehouse.log"


def getlogger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    ch = logging.StreamHandler(sys.stderr)
    ch.setLevel(level)
    fh = logging.FileHandler(event_logs)
    fh.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)15s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger
