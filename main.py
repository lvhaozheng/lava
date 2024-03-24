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
    thread = threading.Thread(target=quertFunc, args=(RPC,))
    thread1 = threading.Thread(target=quertFunc, args=(RPC1,))
    thread2 = threading.Thread(target=quertFunc, args=(RPC2,))
    thread3 = threading.Thread(target=quertFunc, args=(RPC3,))
    thread4 = threading.Thread(target=quertFunc, args=(RPC4,))
    thread5 = threading.Thread(target=quertFunc, args=(RPC5,))
    thread6 = threading.Thread(target=quertFunc, args=(RPC6,))
    thread7 = threading.Thread(target=quertFunc, args=(RPC7,))
    thread8 = threading.Thread(target=quertFunc, args=(RPC8,))
    thread9 = threading.Thread(target=quertFunc, args=(RPC9,))
    thread.start()
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread.join()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()



if __name__ == '__main__':
    main()
