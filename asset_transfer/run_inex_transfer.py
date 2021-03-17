import os
import sys
sys.path.append(os.getcwd())

import logging
from asset_transfer.inex_transfer.inex_transfer import InexTransfer


def run():
    mongo_uri, secret_id, currency, amount, from_field, from_pair, to_field, to_pair = sys.argv[1:]

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    log_formatter = logging.Formatter('%(asctime)s@%(filename)s/%(funcName)s %(message)s')
    log_file_name = f'logs/inex_transfer.log'
    file_handler = logging.FileHandler(filename=log_file_name)
    file_handler.setFormatter(log_formatter)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    inex_transfer = InexTransfer(mongo_uri=mongo_uri, secret_id=secret_id,
                                 currency=currency, amount=amount, from_field=from_field, from_pair=from_pair, to_field=to_field, to_pair=to_pair)
    inex_transfer.transfer()


if __name__ == '__main__':
    run()
