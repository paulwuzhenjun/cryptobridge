import os
import sys
sys.path.append(os.getcwd())

import asyncio
from core import *
from exchanges.hbg.utils import *

api_key, api_secret = sys.argv[1:]


async def main():
    response = await hbg_contracts_post(api_key, api_secret, 'https://api.hbdm.com/swap-api/v1/swap_balance_valuation')
    print(f'response:', response)

    await close_aio_session()
asyncio.run(main())
