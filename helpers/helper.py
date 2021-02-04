import inspect
import logging
from datetime import date

today = date.today()


def line_info():
    f = inspect.currentframe()
    i = inspect.getframeinfo(f.f_back)

    return f"{i.filename} : {i.lineno} called from {i.function}"


def logInfo(msg):
    """"""
    feedDataLogFile = f'../log/FeedDataLogFile-{today}.log'
    logging.basicConfig(filename=feedDataLogFile, level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    logging.info(msg)


def logDebug(msg):
    """"""
    DebugLogFile = f'./log/DebugLogFile-{today}.log'
    logging.basicConfig(filename=DebugLogFile, level=logging.DEBUG,
                        format='%(levelname)s:%(message)s')
    logging.debug(msg)


def logError(msg):
    """"""
    ErrorLogFile = f'./log/ErrorLogFile-{today}.log'
    logging.basicConfig(filename=ErrorLogFile, level=logging.ERROR,
                        format='%(levelname)s:%(message)s')
    logging.error(msg)
