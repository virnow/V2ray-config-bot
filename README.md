# V2ray-config-bot
> A bot that provides free V2Ray configurations, connected to multiple repositories for receiving up-to-date servers, with mandatory joining in the channel and subgrouping for unlimited configuration access and increasing channel members.

# Automatic Installation
- Open your terminal and first enter the following command:
```bash
sudo su
```
- Then, after entering your server password, enter the following command and wait:
```bash
bash <(curl -Ls https://raw.githubusercontent.com/virnow/V2ray-config-bot/main/run.bash)
```
During the configuration editing step, save the configuration with the inserted specifications and wait for the installation process to continue.
Finally, your robot will run in the background, and you can close the terminal, but do not kill the processes.

# Manual Installation
- First, download the [Source Code](https://github.com/virnow/V2ray-config-bot/archive/refs/heads/main.zip)!
- Extract the zip file.
```bash
cd V2ray-config-bot-main
```
- Then, install the Python libraries with the following command:
```bash
pip3 install -r requirements.txt
```
- Next, edit the config.py file and enter your information:
```bash
nano config.py
```
Finally, run the main.py and update.py files!
```bash
(python3 main.py &) && (python3 update.py &)
```

# Screenshots
<div>
    <img src="https://raw.githubusercontent.com/virnow/V2ray-config-bot/main/scr/1.png" alt="Image 1" width="300" height="600">
    <img src="https://raw.githubusercontent.com/virnow/V2ray-config-bot/main/scr/2.png" alt="Image 2" width="300" height="600">
    <img src="https://raw.githubusercontent.com/virnow/V2ray-config-bot/main/scr/3.png" alt="Image 3" width="300" height="600">
    <img src="https://raw.githubusercontent.com/virnow/V2ray-config-bot/main/scr/4.png" alt="Image 4" width="300" height="600">
    <img src="https://raw.githubusercontent.com/virnow/V2ray-config-bot/main/scr/5.png" alt="Image 5" width="300" height="600">
    <img src="https://raw.githubusercontent.com/virnow/V2ray-config-bot/main/scr/6.png" alt="Image 6" width="300" height="600">
</div>

# Resources
- [@Python3_channel](https://t.me/python3_channel)
- [V2ray Collector](https://github.com/yebekhe/TelegramV2rayCollector)
