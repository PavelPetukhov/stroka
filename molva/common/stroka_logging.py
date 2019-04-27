import logging
from .log_formatter import LogFormatter


m_logger = None


def setLogger(logger):
    global m_logger
    m_logger = logger


def getLogger():
    global m_logger
    if m_logger is None:
        return logging.getLogger()
    else:
        return m_logger


def setup_logging(cfg, logger_name):
    logging.basicConfig(level=logging.INFO, filename=logger_name)
    logger = logging.getLogger(logger_name)
    logger.setLevel(cfg.logger.level)
    setLogger(logger)
    return logger
