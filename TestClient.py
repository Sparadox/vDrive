#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ServeurVitesse
import time
import socket

hote = "localhost"
port = 12800

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((hote, port))

while True:
    msgEnv = "bite"
    msgEnv = msgEnv.encode()

    sock.send(msgEnv)
    msg = sock.recv(1024)
    print(msg.decode())
    print(" km/h\n")
    time.sleep(2)
