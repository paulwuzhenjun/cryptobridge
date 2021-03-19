import json
import requests

proxies = {
    'https': 'http://127.0.0.1:8890'
}

response = requests.get('https://api.hbtc.com/openapi/v1/brokerInfo', proxies=proxies)
content = response.content
content_json = json.loads(content)
symbols = content_json['symbols']
for symbol_ctx in symbols:
    pair_symbol = symbol_ctx['symbol']
    if pair_symbol == 'AAVEUSDT':
        print(f'{symbol_ctx}')
