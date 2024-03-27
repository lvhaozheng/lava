import configparser
import json

rpcs = []
idx = 11
for i in range (1, idx):
    rpc = configparser.ConfigParser()
    rpc.read("conf/lava{}.ini".format(i))
    rpcs.append(rpc)

with open("conf/address_pool.txt", "r") as file:
    AddressSet = [row.strip() for row in file]
    print("加载地址池成功，地址池中共有 {} 个地址".format(len(AddressSet)))
