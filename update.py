# Please download the V2ray-config-bot from the following link: https://github.com/virnow/V2ray-config-bot

from requests import get
from time import sleep

def Get_VMESS():
    try:
        NORMAL = get("https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/vmess").text
        with open("configs/VMESS/NORMAL.txt","w",encoding="utf-8") as f:f.write(NORMAL)
        BASE64 = get("https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/vmess_base64").text
        with open("configs/VMESS/BASE64.txt","w",encoding="utf-8") as f:f.write(BASE64)
        CLASH = get("https://github.com/yebekhe/TelegramV2rayCollector/raw/main/clash/vmess.yml").text
        with open("configs/VMESS/CLASH.txt","w",encoding="utf-8") as f:f.write(CLASH)
        CLASHMETA = get("https://github.com/yebekhe/TelegramV2rayCollector/raw/main/meta/vmess.yml").text
        with open("configs/VMESS/CLASHMETA.txt","w",encoding="utf-8") as f:f.write(CLASHMETA)
    except Exception as e:
        print(e)
def Get_VLESS():
    try:
        NORMAL = get("https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/vless").text
        with open("configs/VLESS/NORMAL.txt","w",encoding="utf-8") as f:f.write(NORMAL)
        BASE64 = get("https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/vless_base64").text
        with open("configs/VLESS/BASE64.txt","w",encoding="utf-8") as f:f.write(BASE64)
        CLASHMETA = get("https://github.com/yebekhe/TelegramV2rayCollector/raw/main/meta/vless.yml").text
        with open("configs/VLESS/CLASHMETA.txt","w",encoding="utf-8") as f:f.write(CLASHMETA)
    except Exception as e:
        print(e)
def Get_REALITY():
    try:
        NORMAL = get("https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/reality").text
        with open("configs/REALITY/NORMAL.txt","w",encoding="utf-8") as f:f.write(NORMAL)
        BASE64 = get("https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/reality_base64").text
        with open("configs/REALITY/BASE64.txt","w",encoding="utf-8") as f:f.write(BASE64)
        CLASHMETA = get("https://github.com/yebekhe/TelegramV2rayCollector/raw/main/meta/reality.yml").text
        with open("configs/REALITY/CLASHMETA.txt","w",encoding="utf-8") as f:f.write(CLASHMETA)
    except Exception as e:
        print(e)
def Get_TROJAN():
    try:
        NORMAL = get("https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/trojan").text
        with open("configs/TROJAN/NORMAL.txt","w",encoding="utf-8") as f:f.write(NORMAL)
        BASE64 = get("https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/trojan_base64").text
        with open("configs/TROJAN/BASE64.txt","w",encoding="utf-8") as f:f.write(BASE64)
        CLASH = get("https://github.com/yebekhe/TelegramV2rayCollector/raw/main/clash/trojan.yml").text
        with open("configs/TROJAN/CLASH.txt","w",encoding="utf-8") as f:f.write(CLASH)
        CLASHMETA = get("https://github.com/yebekhe/TelegramV2rayCollector/raw/main/meta/trojan.yml").text
        with open("configs/TROJAN/CLASHMETA.txt","w",encoding="utf-8") as f:f.write(CLASHMETA)
    except Exception as e:
        print(e)
def Get_ShadowSocks():
    try:
        NORMAL = get("https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/shadowsocks").text
        with open("configs/ShadowSocks/NORMAL.txt","w",encoding="utf-8") as f:f.write(NORMAL)
        BASE64 = get("https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/shadowsocks_base64").text
        with open("configs/ShadowSocks/BASE64.txt","w",encoding="utf-8") as f:f.write(BASE64)
        CLASH = get("https://github.com/yebekhe/TelegramV2rayCollector/raw/main/clash/shadowsocks.yml").text
        with open("configs/ShadowSocks/CLASH.txt","w",encoding="utf-8") as f:f.write(CLASH)
        CLASHMETA = get("https://github.com/yebekhe/TelegramV2rayCollector/raw/main/meta/shadowsocks.yml").text
        with open("configs/ShadowSocks/CLASHMETA.txt","w",encoding="utf-8") as f:f.write(CLASHMETA)
    except Exception as e:
        print(e)

def main():
    Get_VMESS()
    Get_VLESS()
    Get_REALITY()
    Get_TROJAN()
    Get_ShadowSocks()
    print("done")

if __name__ == "__main__":
    while True:
        main()
        sleep(3600)

# Please download the V2ray-config-bot from the following link: https://github.com/virnow/V2ray-config-bot
