import os
import sys
sys.path.append(os.getcwd())

import click
import logging
import asyncio
from core.logs import *
from strategies.ssf.strategy_ssf import StrategySSF


@click.command()
@click.option('--sentry', help='the sentry mongo-uri', required=True)
@click.option('--broker', help='the broker address, hkgw.uranome.com:443', required=True)
@click.option('--code', help='the strategy code', required=True)
@click.option('--deploy', help='the strategy deploy id', required=True)
def run(sentry, broker, code, deploy):
    logs_init_std(f'{code}')

    strategy_code_clazz = {
        'ssf': StrategySSF
    }

    mongo_uri = sentry
    broker_address = broker
    broker_host, broker_port = broker_address.split(':')
    strategy_code = code
    strategy_deploy_id = deploy
    logging.info(f'mongo-uri: {mongo_uri}, broker-address: {broker_address}')
    logging.info(f'strategy-code: {strategy_code}, deploy-id: {strategy_deploy_id}')

    strategy_clazz = strategy_code_clazz[strategy_code]
    strategy_inst = strategy_clazz(mongo_uri, strategy_deploy_id, broker_host, broker_port)
    asyncio.run(strategy_inst.initialize())
    while True:
        asyncio.run(asyncio.sleep(10))


if __name__ == '__main__':
    run()
