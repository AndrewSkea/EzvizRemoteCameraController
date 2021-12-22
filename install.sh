pip3 install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
sudo mkdir -p ~/logs
sudo chmod -R 777 ~/logs
sudo cp controller.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable controller.service
sudo systemctl start controller.service
