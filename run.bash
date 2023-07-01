wegt https://github.com/virnow/V2ray-config-bot/archive/refs/heads/main.zip
tar -xvf main.zip
cd V2ray-config-bot-main
pip3 install -r requirements.txt
echo "Edit config File"
input("Press any key to continue...")
nano config.py
echo "Now Run Bot in background"
tmux new -d 'python3 main.py > main.log'
tmux new -d 'python3 update.py > update.log'
exit