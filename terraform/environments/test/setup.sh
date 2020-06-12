#! /bin/bash
                
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install python3-pip unzip expect -y

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg --install google-chrome-stable_current_amd64.deb
sudo apt install --assume-yes --fix-broken

pip3 install --user selenium

wget https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_linux64.zip
unzip chromedriver*.zip
sudo mv chromedriver -f /usr/bin
