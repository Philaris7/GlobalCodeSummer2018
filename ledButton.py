#! /usr/bin/python3

#Simple script to lit LED usin g python 
from gpiozero import LED
from  time import sleep
from gpiozero import Button
from signal import pause

led = LED(17)
but = Button(2)

#while True:
#	led.on()
#	sleep(5)
#	led.off()
#	sleep(1)



but.when_pressed = led.on()
but.when_released = led.off()

pause()


