import configparser
import json

RPC = configparser.ConfigParser()
RPC1 = configparser.ConfigParser()
RPC2 = configparser.ConfigParser()
RPC3 = configparser.ConfigParser()
RPC4 = configparser.ConfigParser()
RPC5 = configparser.ConfigParser()
RPC6 = configparser.ConfigParser()
RPC7 = configparser.ConfigParser()
RPC8 = configparser.ConfigParser()
RPC9 = configparser.ConfigParser()

RPC.read("conf/lava.ini")
RPC1.read("conf/lava1.ini")
RPC2.read("conf/lava2.ini")
RPC3.read("conf/lava3.ini")
RPC4.read("conf/lava4.ini")
RPC5.read("conf/lava5.ini")
RPC6.read("conf/lava6.ini")
RPC7.read("conf/lava7.ini")
RPC8.read("conf/lava8.ini")
RPC9.read("conf/lava9.ini")

with open("conf/address_pool.txt", "r") as file:
    AddressSet = [row.strip() for row in file]
    print("加载地址池成功，地址池中共有 {} 个地址".format(len(AddressSet)))
