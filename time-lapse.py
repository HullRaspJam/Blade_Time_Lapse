#!/bin/python3

from time import sleep
from gpiozero import LED
from picamera import PiCamera

cam = PiCamera()
led = LED(2)

led.on()

for i in range(10):
    cam.capture('/home/pi/captures/image{0:07d}.jpg'.format(i))
    sleep(5)
led.off()

