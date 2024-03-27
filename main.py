import time

import threading
from config import *
from rpc import *
import random

QPS = 10


def query_balance_eth(eth_rpc, address):
    balance = eth_get_balance(eth_rpc, address)
    if balance is not None:
        print("通过lava-RPC {} \n 查询账户{} 余额为 {} eth".format(eth_rpc, address, balance))
    else:
        print("调用lava-RPC {} 失败，请确认你的RPC地址".format(eth_rpc))

def quertFunc(rpc):
    if "ETH" not in rpc or "Mainnet" not in rpc["ETH"]:
        print("缺少lava的ETH-RPC-Endpoint，请先配置你的地址")
        exit(1)
    while True:
        r = random.randint(0, len(AddressSet)-1) % len(AddressSet)
        address = AddressSet[r]
        query_balance_eth(rpc["ETH"]["Mainnet"], address)
        time.sleep(1 / QPS)

def main(): 
    threads = []
    for rpc in rpcs:
        thread = threading.Thread(target=quertFunc, args=(rpc,))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()



if __name__ == '__main__':
    main()
