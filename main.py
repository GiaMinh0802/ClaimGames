from telethon import TelegramClient, events
import os
import platform
from lottery.Redpage import lotteryRedpage
from vn82.Redpage import vn82Redpage
from vesovn.Redpage import vesovnRedpage
from vn168.Redpage import vn168Redpage

print('Started')

api_id = '28222709'
api_hash = 'cbe0badef0a05463b386cac35dbfb4e9'
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage(chats=['doclenh92lottery', 'doclenhvn168', 'vngolenh3phut', 'sukienvessovn']))
async def my_event_handler(event):
    msg = str(event.raw_text)
    text = msg.split("\n")
    sender = await event.get_sender()
    sender_name = sender.username
    for mess in text:
        mess = mess.rstrip()
        if (len(mess) == 32) and (" " not in mess):
            await client.send_message('claimgame0802', sender_name + ": " + mess)
            if platform.system() == 'Windows':
                os.system('cls')
            else:
                os.system('clear')
            if (sender_name == 'doclenhvn168'):
                vn168Redpage(mess)
            if (sender_name == 'doclenh92lottery'):
                lotteryRedpage(mess)
            if (sender_name == 'sukienvessovn'):
                vesovnRedpage(mess)
            if (sender_name == 'vngolenh3phut'):
                vn82Redpage(mess)

client.start()
client.run_until_disconnected()