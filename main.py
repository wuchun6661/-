# -*- coding:utf-8 -*-
"""
作者：Wcy
日期：2021年12月29日
时间：20:21:24
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # 基本套接字类型，允许广播，级别

port = 8080

network = '<broadcast>'
s.sendto("我是服务器，向你发送了广播，请告诉我你的名字~".encode('utf-8'), (network, port))

data, address = s.recvfrom(1024)
print("收到了来自 {}:{}".format(address, data.decode('utf-8')))
