#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import math
import socket

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)

speed = 0
t = t0 = time.time()
d=0

"""Connexion au socket de communication sur le localhost"""
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion.connect(('localhost', 12800))

while True:
	GPIO.wait_for_edge(11, GPIO.RISING)
	nt = time.time()
	speed = 0.4*3.6*30*math.pi/180/(nt - t)
	d += speed * (nt - t)
	t = nt	
	
	msg = "{0};{1};{2}\n".format(speed, d/(t-t0), d).encode()
	connexion.send(msg)
	msgBack = connexion.recv(1024)
	print(msgBack.decode())
	#print("Vitesse = {0} km/h \t\t\t Vmoy = {1} km/h \t\t\t s = {2} m\n\n".format(speed, d/(t-t0), d))
