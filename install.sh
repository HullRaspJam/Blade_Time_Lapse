mkdir /home/pi/timelapse/
mkdir /home/pi/timelapse/captures/

cp ./code/time-lapse.py /home/pi/timelapse/
sudo cp ./code/timelapse.service /lib/systemd/system/

sudo chmod 644 /lib/systemd/system/timelapse.service
sudo chmod +x /home/pi/timelapse/time-lapse.py

sudo systemctl daemon-reload
sudo systemctl enable timelapse.service
