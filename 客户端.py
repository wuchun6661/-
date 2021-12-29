# -*- coding:utf-8 -*-
"""
作者：Wcy
日期：2021年12月29日
时间：20:26:33
"""
import socket

hard_name = "硬件1号"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # 基本套接字类型，允许广播，级别

port = 8080
ip = socket.gethostbyname(socket.gethostname())  # 获取自身ip

s.bind((ip, port))
print("本设备的IP和端口号为:[{},{}]".format(ip, port))
print("正在等待接受信息......\n")

data, address = s.recvfrom(1024)
s.sendto("我是:{}".format(hard_name).encode('utf-8'), address)
print("Server received from {}:{}".format(address, data.decode('utf-8')))
