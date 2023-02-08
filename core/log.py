import logging
from core.settings import settingsObj


def _get_cli_log_format():
    detail_log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    minimal_log_format = f"%(asctime)s    [%(levelname)s] - %(message)s"
    if settingsObj.project.get('mode') == 'dev':
        return detail_log_format
    elif settingsObj.project.get('mode') == 'prod':
        return minimal_log_format
    else:
        print('Perhaps the wrong attribute is set in the settings!')

_log_format_for_cli = _get_cli_log_format()
_log_format_for_file = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"

def get_file_handler():
    file_handler = logging.FileHandler(f'{settingsObj.log_path}')
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
    logger.setLevel(settingsObj.logging['level'])
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger
    
