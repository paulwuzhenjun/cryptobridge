import base64
import datetime
import hashlib
import hmac
import urllib.parse

from core import *


def __hbg_contracts_sign(api_key, api_secret, method, uri):
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
    params_to_sign = {
        'AccessKeyId': api_key,
        'SignatureMethod': 'HmacSHA256',
        'SignatureVersion': '2',
        'Timestamp': timestamp
    }
    uri_parsed = urllib.parse.urlparse(uri)
    host_name, path = uri_parsed.hostname.lower(), uri_parsed.path
    sorted_params = sorted(params_to_sign.items(), key=lambda d: d[0], reverse=False)
    encode_params = urllib.parse.urlencode(sorted_params)
    payload = [method, host_name, path, encode_params]
    payload = '\n'.join(payload)
    payload = payload.encode(encoding='UTF8')
    secret_key = api_secret.encode(encoding='UTF8')
    digest = hmac.new(secret_key, payload, digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(digest)
    signature = signature.decode()
    params_to_sign['Signature'] = signature
    return params_to_sign


async def hbg_contracts_post(api_key, api_secret, uri, params=None):
    if params is None:
        params = {}

    headers = {
        "Accept": "application/json",
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
    }

    sign_headers = __hbg_contracts_sign(api_key, api_secret, 'POST', uri)
    query = urllib.parse.urlencode(sign_headers)
    uri_with_query = f'{uri}?{query}'
    aio_session = await get_aio_session()
    response = await aio_session.post(uri_with_query, headers=headers, json=params)
    response = await response.json()
    return response
