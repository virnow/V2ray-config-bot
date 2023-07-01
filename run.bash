#!/bin/bash

wget https://github.com/virnow/V2ray-config-bot/archive/refs/heads/main.zip
unzip main.zip
cd V2ray-config-bot-main
pip3 install -r V2ray-config-bot-main/requirements.txt
echo "Edit config File"
nano V2ray-config-bot-main/config.py
echo "Now Run Bot in background"
tmux new -d 'python3 V2ray-config-bot-main/main.py > main.log'
tmux new -d 'python3 V2ray-config-bot-main/update.py > update.log'
exit
