# Time Lapse
This project contains the code for a Raspberry Pi time lapse camera. There are three main files included; the Python script for taking the photos, a System D service definition and an install Shell script to move everything into the right place and activate the service etc.

## Hardware Install Instructions
Using a Lisiparoi IR LED Module and a NoIR Raspberry Pi Camera, connect up your hardware as per this diagram:
<img src="/docs/blade-wiring_bb.png" alt="Wiring Diagram" width="350"><br />
The GPIO for the LED should be on GPIO 2 and the LED needs a 5V power input. Beware that these LED modules can get quite hot during normal operation!

Attach your NoIR Raspberry Pi camera module into the Lisipario as described here: http://www.lisiparoi.com/how-to-use/ and then attach your NoIR Raspberry Pi camera to the Pi as usual. 
## Software Install instructions
1. Enable your PiCamera:
   1. ```sudo raspi-config```
   1. Select ```5 Interfacing Options```
   1. Select ```P1 Camera```
   1. Select ```Yes```
   1. Select ```OK```
   1. Select ```Finish```
   1. Select ```Yes``` to reboot now
1. Move into your home directory ```cd ~```
1. Clone the repository ```git clone https://github.com/HullRaspJam/Blade_Time_Lapse.git```
1. Move into the repository directory ```cd Blade_Time_Lapse/```
1. Run ```./install.sh``` to create the required directories, copy the files into the correct place and enable teh service
1. Run ```sudo shutdown now -hP```
Your time lapse will start after 5 minutes from the next time you power on your Pi.
