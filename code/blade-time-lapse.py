#!/bin/python3

from time import sleep
from gpiozero import LED
from picamera import PiCamera
from os import system

cam = PiCamera()
led = LED(2)

system('mkdir /home/pi/captures')

led.on()

for i in range(10):
    cam.capture('/home/pi/captures/image{0:07d}.jpg'.format(i))
led.off()

