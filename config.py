import configparser
import os

conf_files = [file for file in os.listdir("conf") if file.startswith("lava") and file.endswith(".ini")]
rpcs = []
for file in conf_files:
    rpc = configparser.ConfigParser()
    rpc.read(f"conf/{file}")
    rpcs.append(rpc)

with open("conf/address_pool.txt", "r") as file:
    AddressSet = [row.strip() for row in file]
    print(f"加载地址池成功，地址池中共有 {len(AddressSet)} 个地址")
