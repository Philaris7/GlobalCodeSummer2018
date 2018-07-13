#! /usr/bin/python3

#Simple script to lit LED usin g python 
from gpiozero import LED
from  time import sleep


led = LED(17)
while True:
	led.on()
	sleep(5)
	led.off()
	sleep(1)



