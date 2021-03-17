import logging


def logs_init_std(file_name):
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    log_formatter = logging.Formatter('%(asctime)s@%(filename)s/%(funcName)s %(message)s')
    log_file_name = f'logs/{file_name}.log'
    file_handler = logging.FileHandler(filename=log_file_name)
    file_handler.setFormatter(log_formatter)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
