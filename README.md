# Blade Time Lapse
This project contains the code for a Raspberry Pi time lapse camera. There are three main files included; the Python script for taking the photos, a System D service definition and an install Shell script to move evrything into the right place and activate the service etc.

## Hardware Install Instructions
Using a Lisiparoi IR LED Module and a NoIR Raspberry Pi Camera, connect up your hardware as per this diagram:
![Wiring Diagram](/images/wiring.png)
The GPIO for the LED should be on GPIO 2 and the LED needs a 5V power input. Beware that these LED modules can get quite hot during normal operation!
## Software Install instructions
1. Clone the repository
2. cd into the repository directory
3. run ```sudo install.sh``` and follow the instructions to install the service
4. run ```sudo shutdown now -hP```
Your time lapse will start after 5 minutes from the next time you power on your Pi.
