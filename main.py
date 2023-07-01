# Please download the V2ray-config-bot from the following link: https://github.com/virnow/V2ray-config-bot

from pyrogram import (Client, filters,idle,errors)
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,InlineKeyboardButton)
import os
import json
import time
from random import choice
from config import *


# CLIENT BOT
bot = Client("V2ray-config",Api_id,Api_hash,bot_token=TOKEN)
bot.start()
BOTD = bot.get_me()
print("Start Bot V2ray Config :","@"+BOTD.username) 


# Memory Data
Step = dict()
USERS = dict()
PRO = dict() 
SLP = dict()


# Defs Script
def RandomLineFile(path):
    with open(path,"r",encoding="utf-8") as f:
        return choice(f.read().splitlines())

def users(method="get",id=""):
    if method == "get":
        with open("users.json","r",encoding="utf-8") as f:
            return json.load(f)
    elif method == "add":
        data = users()
        with open("users.json","w",encoding="utf-8") as f:
            data["users"].append(int(id))
            json.dump(data,f,ensure_ascii=False)
            return True

def userpro(id=""):
    data = users()
    with open("users.json","w",encoding="utf-8") as f:
        data["pro"].append(int(id))
        json.dump(data,f,ensure_ascii=False)
        return True


# Telegram methods
async def check_join(user_id):
    global channels
    ls = []
    for i in channels:
        try:
            await bot.get_chat_member(i, user_id)
            continue
        except errors.exceptions.bad_request_400.UserNotParticipant:
            ls.append([InlineKeyboardButton("📢 Join Channel {}".format(len(ls)+1),url="https://t.me/{}".format(i.replace("@", '')))])
            continue
        except errors.exceptions.bad_request_400.ChatAdminRequired:
            await bot.send_message(admins[0],"**⛔️ The robot is not an admin in the {} channel**".format(i))
            continue
        except errors.exceptions.bad_request_400.UsernameNotOccupied:
            await bot.send_message(admins[0],"**⛔️ There is no registered {} channel**".format(i))
            continue
        except Exception as e:
            print(i,user_id)
            print(e)
        finally:continue
    return ls


# Keyborad Panel
panelKEY = ReplyKeyboardMarkup(
        [
            ["📊 Status Bot","🗂 Source"],
            ["👥 Send ALL","👥 Forward ALL"],
            ["◀️back"],
        ],
        resize_keyboard=True
    )

backP = ReplyKeyboardMarkup(
        [
            ["◀️"],
        ],
        resize_keyboard=True
    )

home = ReplyKeyboardMarkup(
        [
            ["📡 Config Free","📡 Config File"],
            ["⬆️ Upgrade Account"],
            ["👤 Account","📣 Sponsors"],
        ],
        resize_keyboard=True
    )

back = ReplyKeyboardMarkup(
        [
            ["◀️back"],
        ],
        resize_keyboard=True
    )

configKEY = ReplyKeyboardMarkup(
        [
            ["📡 NORMAL","📡 BASE64"],
            ["📡 CLASH","📡 CLASH.Meta"],
            ["◀️back"]
        ],
        resize_keyboard=True
    )

configsKEY = ReplyKeyboardMarkup(
        [
            ["🔗 VMESS","🔗 VLESS"],
            ["🔗 REALITY","🔗 TROJAN"],
            ["🔗 ShadowSocks"],
            ["◀️back"]
        ],
        resize_keyboard=True
    )

def memmber(link):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🤖 Open Bot 🤖",
                    url=link
                ),
            ],
        ]
    )


# Load Data form File
USERS = users()
PRO = USERS["pro"]


# Def Main Bot message
@bot.on_message(filters.private & filters.text)
async def Main(client, message):
    global Step,USERS,PRO,SLP
    from_id = message.from_user.id
    text = message.text
    message_id = message.id
    telegram_date = message.date
    if from_id not in Step:
        Step[from_id] = ""
    ck = await check_join(from_id)
    if ck != []:
        await bot.send_message(from_id,"**❤️ Please join our sponsors channels first.\n\n✅ Then restart the bot : /start**",reply_markup=InlineKeyboardMarkup(ck))
        return False
    if text.startswith("/start "):
        id = text.split(" ")[1]
        if id.isdigit():
            id = int(id)
            if id != from_id and from_id not in USERS["users"]:
                await bot.send_message(from_id,"**🤖 Welcome To V2ray Config Bot🤖\n\n🔰 Choose the section you want :**",reply_markup=home,reply_to_message_id=message_id)
                USERS["users"].append(from_id)
                users("add",from_id)
                try:
                    await bot.send_message(id,"**🎉 User [{0}](tg://user?id{0}) joined the bot with your link.**".format(id))
                    PRO.append(id)
                    userpro(id)
                except:pass
                return False
            else:
                await bot.send_message(from_id,"**🤖 Welcome To V2ray Config Bot🤖\n\n🔰 Choose the section you want :**",reply_markup=home,reply_to_message_id=message_id)
                USERS["users"].append(from_id)
                users("add",from_id)
                return False
        else:
            await bot.send_message(from_id,"**🤖 Welcome To V2ray Config Bot🤖\n\n🔰 Choose the section you want :**",reply_markup=home,reply_to_message_id=message_id)
            USERS["users"].append(from_id)
            users("add",from_id)
            return False
    if from_id not in USERS["users"]:
        USERS["users"].append(from_id)
        users("add",from_id)
    if text in ['/start','◀️back']:
        Step[from_id] = "None"
        await bot.send_message(from_id,"**🤖 Welcome To V2ray Config Bot🤖\n\n🔰 Choose the section you want :**",reply_markup=home,reply_to_message_id=message_id)
        return False
    elif text == "📡 Config Free":
        if from_id not in PRO:
            if from_id in SLP:
                if SLP[from_id] > int(time.time()):
                    await bot.send_message(from_id,"**⚠️ Please upgrade your account by (⬆️ Upgrade Account) or wait for {} seconds.**".format(SLP[from_id]-int(time.time())),reply_markup=back,reply_to_message_id=message_id)
                    return False
        Step[from_id] = "freeconfig2|"+"NORMAL"
        await bot.send_message(from_id,"**📡 Select Your Config Type :**",reply_markup=configsKEY,reply_to_message_id=message_id)
        return False
    elif text == "📡 Config File":
        if from_id not in PRO:
            await bot.send_message(from_id,"**⚠️ To use this section, you need to upgrade your account by (⬆️ Upgrade Account)**",reply_markup=back,reply_to_message_id=message_id)
            return False
        Step[from_id] = "fileconfig"
        await bot.send_message(from_id,"**📡 Select Your Config Subscription :**",reply_markup=configKEY,reply_to_message_id=message_id)    
        return False
    elif text == "⬆️ Upgrade Account":
        Step[from_id] = "upgrade"
        link = memmber("https://t.me/{}?start={}".format(BOTD.username,from_id))
        msg = await bot.send_message(from_id,"**⚡️ Free config bot\n💯 The best V2ray services\n🚀 Maximum speed and without any interruptions\n👤 No limit on the number of users\n📱 Can be connected on Android, iOS, Windows, MacOS and Linux\n🧪 Completely free account\n\nto start bot👇🏻**",reply_markup=link)    
        await msg.reply_text("**⭐️ Send the above message to your friends to upgrade your account.**",True,reply_markup=back)
        return False
    elif text == "👤 Account":
        Step[from_id] = "account"
        if from_id in PRO:tp = "Pro"
        else:tp = "Free"
        await bot.send_message(from_id,"**🆔 User ID :** `{}`\n**👤 Account Type :** `{}`\n**📅 Date :** `{}`\n\n**🤖 @{}**".format(from_id,tp,telegram_date,BOTD.username),reply_markup=back,reply_to_message_id=message_id)
        return False
    elif text == "📣 Sponsors":
        Step[from_id] = "spons"
        Tex = "💜 Sponsors Channels :\n\n"
        for i in channels:
            Tex += "🏆 {}\n".format(i)
        await bot.send_message(from_id,"**{}\n\n\n**🤖 @{}**".format(Tex,BOTD.username),reply_markup=back,reply_to_message_id=message_id)
        return False
    elif Step[from_id] == "fileconfig":
        Step[from_id] = "fileconfig2|"+text.replace("🔗 ","")
        await bot.send_message(from_id,"**📡 Select Your Config Type :**",reply_markup=configsKEY,reply_to_message_id=message_id)
        return False
    elif "freeconfig2|" in Step[from_id] and text in ["🔗 VMESS","🔗 VLESS","🔗 REALITY","🔗 TROJAN","🔗 ShadowSocks"]:
        SLP[from_id] = int(time.time()) + int(timefree)
        cnf = Step[from_id].split("|")[1].replace("📡 ", "").replace(".", "")
        typ = text.replace("🔗 ", "")
        if os.path.isfile("configs/"+typ+"/"+cnf+".txt"):
            con = RandomLineFile("configs/"+typ+"/"+cnf+".txt")
            await bot.send_message(from_id,"**📡 Config : (**`{}`**)\n🖥 Type : **`{}`\n📅**Date :** `{}`\n**⚠️The configurations are not tested and the bot is only a publisher.\n\n🤖 @{}**".format(con,typ,telegram_date,BOTD.username),reply_markup=back,reply_to_message_id=message_id)
        else:
            await bot.send_message(from_id,"**❌ Currently v2ray configs are not available to provide, try again later**",reply_markup=back,reply_to_message_id=message_id)
        Step[from_id] = "None"
        return False
    elif "fileconfig2|" in Step[from_id] and text in ["🔗 VMESS","🔗 VLESS","🔗 REALITY","🔗 TROJAN","🔗 ShadowSocks"]:
        cnf = Step[from_id].split("|")[1].replace("📡 ", "").replace(".", "")
        typ = text.replace("🔗 ", "")
        if os.path.isfile("configs/"+typ+"/"+cnf+".txt"):
            await bot.send_document(from_id,"configs/"+typ+"/"+cnf+".txt",caption="**📡 Subscription :** `{}`\n**🖥 Type : **`{}`\n📅**Date :** `{}`\n**⚠️The configurations are not tested and the bot is only a publisher.\n\n🤖 @{}**".format(cnf,typ,telegram_date,BOTD.username),reply_markup=back,reply_to_message_id=message_id)
        else:
            await bot.send_message(from_id,"**❌ Currently v2ray configs are not available to provide, try again later**",reply_markup=back,reply_to_message_id=message_id)
        Step[from_id] = "None"
        return False
    elif text in ["/panel","Panel","panel","/Panel","◀️"] and from_id in admins:
        Step[from_id] = "panel"
        await bot.send_message(from_id,"**🌹 Welcome to the admin panel of the Config V2ray Bot\n\n🔰 Choose the section you want :**",reply_markup=panelKEY,reply_to_message_id=message_id)
        return False
    elif text == "📊 Status Bot" and from_id in admins:
        Step[from_id] = "StatusBot"
        msg = await bot.send_message(from_id,"**♻️ please wait ...**",reply_markup=backP,reply_to_message_id=message_id)
        chn = ""
        for i in channels:
            try:mmb = await bot.get_chat_members_count(i)
            except:mmb = "Error"
            chn += "📢 {} : 👥 {}\n".format(i,mmb)
        await msg.delete()
        await bot.send_message(from_id,"**👤 Number Of Users : {}\n⭐️ Number Of Users Pro : {}\n💜 Connected Channels : {}\n\n{}**".format(len(USERS["users"]),len(PRO),len(channels),chn),reply_markup=backP,reply_to_message_id=message_id)
        return False
    elif text == "🗂 Source" and from_id in admins:
        Step[from_id] = "github"
        await bot.send_message(from_id,"**GitHub link : github.com/virnow/V2ray-config-bot\n\n😉 Don't forget to like❤️!**",reply_markup=backP,reply_to_message_id=message_id,disable_web_page_preview=True)
        return False
    elif text == "👥 Send ALL" and from_id in admins:
        Step[from_id] = "SendALL"
        await bot.send_message(from_id,"**✅ Send your message :**",reply_markup=backP,reply_to_message_id=message_id)
        return False
    elif text == "👥 Forward ALL" and from_id in admins:
        Step[from_id] = "ForwardALL"
        await bot.send_message(from_id,"**✅ Forward your message :**",reply_markup=backP,reply_to_message_id=message_id)
        return False
    elif Step[from_id] == "SendALL":
        Step[from_id] = "None"
        await bot.send_message(from_id,"**⚙️ Start sending , Please wait until the end!**",reply_markup=backP,reply_to_message_id=message_id)
        ok,bad = 0 , 0
        for i in users()["users"]:
            try:await message.copy(i);ok+=1;print("Send to ",i)
            except:bad+=1
        await bot.send_message(from_id,"**✅ {} messages sent!\n❌ {} messages failed!**".format(ok,bad),reply_markup=backP,reply_to_message_id=message_id)
        return False
    elif Step[from_id] == "ForwardALL":
        Step[from_id] = "None"
        await bot.send_message(from_id,"**⚙️ Start forwarding , Please wait until the end!**",reply_markup=backP,reply_to_message_id=message_id)
        ok,bad = 0 , 0
        for i in users()["users"]:
            try:await message.copy(i);ok+=1;print("Forward to ",i)
            except:bad+=1
        await bot.send_message(from_id,"**✅ {} messages sent!\n❌ {} messages failed!**".format(ok,bad),reply_markup=backP,reply_to_message_id=message_id)
        return False

            


idle()
bot.stop()

# Please download the V2ray-config-bot from the following link: https://github.com/virnow/V2ray-config-bot