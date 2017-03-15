#!/usr/bin/python3

# import our libraries
from time import sleep
from gpiozero import LED
from picamera import PiCamera

# set up our camera and LED
cam = PiCamera()
led = LED(2)

# We want full resolution from our v2 camera!
cam.resolution = (3280, 2464)

# sleep for a bit to wait for the action to start!
sleep(300)

# switch our IR LEDs on
led.on()

# now we loop 2160 times with a 10 second pause
# we want to run this baby for 6 hours!
for i in range(2160):
    cam.capture('/home/pi/timelapse/captures/image{0:07d}.jpg'.format(i))
    sleep(10)

# finished so lets switch off the LED
led.off()

