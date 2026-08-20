#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Handling loggers
"""

import sys
import logging

# set up default logging configureation
_FORMAT = "[%(name)-s | %(levelname)-8s] %(message)s"
_TFORMAT = "[%(asctime)s | %(name)-s | %(levelname)-8s] %(message)s"
_DATEFMT = "%Y-%m-%d %H:%M:%S"

_LEVELS = {"DEBUG": logging.DEBUG,
           "INFO": logging.INFO,
           "WARNING": logging.WARNING,
           "ERROR": logging.ERROR,
           "FATAL": logging.FATAL,
           "CRITICAL": logging.CRITICAL}


LOGINIT = False

def getFileHandler(filename, mode="a"):
    """Default console handler"""
    file_handler = logging.FileHandler(filename, mode=mode)
    file_handler.setFormatter(
        logging.Formatter(fmt=_TFORMAT, datefmt=_DATEFMT))
    return file_handler


class ConsolerFormatter(logging.Formatter):
    """Colored logging formatter intended for the console output"""
    def format(self, record):
        logging.Formatter(_FORMAT)
        return formatter.format(record)


def getConsoleHandler():
    """Default console handler"""
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(ConsoleFormatter())
    return console_handler

def get_logger(name='sitka', level="INFO"):
    """Utility function to get the logger with customization

    .. warning:: NOT WORKING AS EXPECTED -> FIXME!!!

    Parameters
    ----------
    name : str        name of the logger
    level : str (optional)   logging level ['INFO']
    """
    global LOGINIT
    if not LOGINIT:
        logging.basicConfig(level=_LEVELS[level],
                            format=_FORMAT, datefmt=_DATEFMT)
        LOGINIT = True
    logger = logging.getLogger(name)
    logger.setLevel(_LEVELS[level])

    if logger.hasHandlers():
        logger.handlers.clear()
    logger.propagate = False
    return logger


def test_logger(level="DEBUG"):
    """Test custom logger"""
    logger = getLogger("sitka test logger", level=level)
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    import tempfile

    flog = tempfile.mktemp(prefix="test_logger_", suffix=".log")
    logger.addHandler(getFileHandler(flog))
    logger.info(f"Added a file handler -> {flog}")
    logger.info("Testing all log levels (again):")
    logger.debug("This is a debug message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")


if __name__ == "__main__":
    test_logger()
