import requests


def eth_get_balance(eth_rpc_endpoint, eth_address):
    """
    Returns the account balance for a given account address and Block Number.

    :param eth_rpc_endpoint:
    :param eth_address:
    :return:
    """
    headers = {
        'Content-Type': 'application/json',
    }
    json_data = {
        'jsonrpc': '2.0',
        'method': 'eth_getBalance',
        'params': [
            eth_address,
            "0x0"
        ],
        'id': 1,
    }
    response = requests.post(eth_rpc_endpoint, headers=headers, json=json_data)
    if response.status_code == 200 and "error" not in response.json():
        balance_hex = response.json()["result"]
        return int(balance_hex, 16)
    else:
        print("eth_get_balance_error, endpoint: ", eth_rpc_endpoint, " \nres: ", response.json())
        return None


def eth_block_number(eth_rpc_endpoint):
    """
    Returns the current block height.

    :param eth_rpc_endpoint:
    :return:
    """
    headers = {
        'Content-Type': 'application/json',
    }

    json_data = {
        'jsonrpc': '2.0',
        'method': 'eth_blockNumber',
        'params': [],
        'id': 1,
    }

    response = requests.post(eth_rpc_endpoint, headers=headers, json=json_data)
    if response.status_code == 200 and "error" not in response.json():
        height_hex = response.json()["result"]
        return int(height_hex, 16)
    else:
        print("eth_blockNumber, endpoint: ", eth_rpc_endpoint, " \nres: ", response.json())
        return None


def eth_gas_price(eth_rpc_endpoint):
    """

    :param eth_rpc_endpoint:
    :return: The hexadecimal value of the current gas price in wei
    """
    headers = {
        'Content-Type': 'application/json',
    }

    json_data = {
        'method': 'eth_gasPrice',
        'params': [],
        'id': 1,
        'jsonrpc': '2.0',
    }
    response = requests.post('https://docs-demo.quiknode.pro/', headers=headers, json=json_data)
    if response.status_code == 200 and "error" not in response.json():
        gas_hex = response.json()["result"]
        return int(gas_hex, 16)
    else:
        print("eth_blockNumber, endpoint: ", eth_rpc_endpoint, " \nres: ", response.json())
        return None


def eth_estimate_gas(eth_rpc_endpoint, from_addr, to_addr, value):
    """

    :param eth_rpc_endpoint:
    :param from_addr:
    :param to_addr:
    :param value:
    :return:
    """
    headers = {
        'Content-Type': 'application/json',
    }

    json_data = {
        'jsonrpc': '2.0',
        'method': 'eth_estimateGas',
        'params': [
            {
                'from': from_addr,
                'to': to_addr,
                'value': value,
            },
        ],
        'id': 1,
    }

    response = requests.post(eth_rpc_endpoint, headers=headers, json=json_data)
    if response.status_code == 200 and "error" not in response.json():
        gas_hex = response.json()["result"]
        return int(gas_hex, 16)
    else:
        print("eth_blockNumber, endpoint: ", eth_rpc_endpoint, " \nres: ", response.json())
        return None


def eth_send_raw_transaction(eth_rpc_endpoint, signed_data):
    headers = {
        'Content-Type': 'application/json',
    }

    json_data = {
        'jsonrpc': '2.0',
        'method': 'eth_sendRawTransaction',
        'params': [
            signed_data,
        ],
        'id': 1,
    }
    response = requests.post(eth_rpc_endpoint, headers=headers, json=json_data)
    if response.status_code == 200 and "error" not in response.json():
        tx_hash = response.json()["result"]
        return tx_hash
    else:
        print("eth_blockNumber, endpoint: ", eth_rpc_endpoint, " \nres: ", response.json())
        return None
