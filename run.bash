#!/bin/bash
sudo apt-get install wget
wget https://github.com/virnow/V2ray-config-bot/archive/refs/heads/main.zip
sudo apt-get install unzip
unzip main.zip
sleep 2
sudo apt-get install python3-pip
pip3 install -r V2ray-config-bot-main/requirements.txt
echo "Edit config File"
sleep 2
nano V2ray-config-bot-main/config.py
echo "Now Run Bot in background"
sleep 2
(cd V2ray-config-bot-main && python3 main.py &)
(cd V2ray-config-bot-main && python3 update.py &)
echo "End"
exit
