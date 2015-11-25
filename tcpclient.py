#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

target_host = "127.0.0.1"
target_port = 3345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send("GET / HTTP/1.1\r\nHOST: baidu.com\r\n\r\n")

response = client.recv(4096)

print response
