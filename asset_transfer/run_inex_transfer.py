import os
import sys
sys.path.append(os.getcwd())

from core.logs import *
from asset_transfer.inex_transfer.inex_transfer import InexTransfer


def run():
    logs_init_std('inex_transfer')

    mongo_uri, secret_id, currency, amount, from_field, from_pair, to_field, to_pair = sys.argv[1:]
    inex_transfer = InexTransfer(mongo_uri=mongo_uri, secret_id=secret_id,
                                 currency=currency, amount=amount, from_field=from_field, from_pair=from_pair, to_field=to_field, to_pair=to_pair)
    inex_transfer.transfer()


if __name__ == '__main__':
    run()
