import threading
import time

from config import *
from rpc import *
import random


def query_balance_eth(eth_rpc_endpoint, address):
    balance = eth_get_balance(eth_rpc_endpoint, address)
    if balance is not None:
        print(f"通过 lava-RPC {eth_rpc_endpoint} \n 查询账户{address} 余额为 {balance} eth")
    else:
        print(f"调用 lava-RPC {eth_rpc_endpoint} 失败，请确认你的 RPC 地址")


def query_eth_block_number(eth_rpc_endpoint):
    block_number = eth_block_number(eth_rpc_endpoint)
    if block_number is not None:
        print(f"通过 lava-RPC {eth_rpc_endpoint} \n 查询当前区块高度为 {block_number}")
    else:
        print(f"调用 lava-RPC {eth_rpc_endpoint} 失败，请确认你的 RPC 地址")


def query_eth_gas_price(eth_rpc_endpoint):
    gas_price = eth_gas_price(eth_rpc_endpoint)
    if gas_price is not None:
        print(f"通过 lava-RPC {eth_rpc_endpoint} \n 查询当前 gas price 为 {gas_price} gwei")
    else:
        print(f"调用 lava-RPC {eth_rpc_endpoint} 失败，请确认你的 RPC 地址")


def sleep_for_a_while():
    time.sleep(random.randint(1, 10))


def query_rpc(rpc_info):
    if "ETH" not in rpc_info or "Mainnet" not in rpc_info["ETH"]:
        print("缺少 lava 的 ETH-RPC-Endpoint，请先配置你的地址")
        exit(1)
    print("======开始运行脚本======")
    print(f"======使用信息为 {rpc_info}======")

    try:
        rpc_address = rpc_info["ETH"]["Mainnet"]
        while True:
            eth_address = random.choice(AddressSet)
            query_balance_eth(rpc_address, eth_address)
            sleep_for_a_while()
            query_eth_block_number(rpc_address)
            sleep_for_a_while()
            query_eth_gas_price(rpc_address)
            sleep_for_a_while()

    except Exception as e:
        print(f"出现异常，异常信息为 {e}")
        exit(1)


def main():
    thread_list = []
    for current_rpc in rpcs:
        thread = threading.Thread(target=query_rpc, args=(current_rpc,))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()


if __name__ == '__main__':
    main()
