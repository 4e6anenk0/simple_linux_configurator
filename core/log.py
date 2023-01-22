import logging
from core.settings import settings


_log_format_for_file = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"

_log_format_for_cli = f"%(asctime)s    [%(levelname)s]    (%(filename)s).%(funcName)s (%(lineno)d) - %(message)s"

def get_file_handler():
    file_handler = logging.FileHandler(f'{settings.log_path}')
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter(_log_format_for_file))
    return file_handler

def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(
        _log_format_for_cli, datefmt='%H:%M:%S'))
    return stream_handler

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(settings.logging['level'])
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger
    
