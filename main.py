from telethon import TelegramClient, events
from lottery.Redpage import lotteryRedpage
from vn82.Redpage import vn82Redpage
from vesovn.Redpage import vesovnRedpage
from vn168.Redpage import vn168Redpage
from club66.Redpage import clubRedpage


print('Started')

api_id = '28222709'
api_hash = 'cbe0badef0a05463b386cac35dbfb4e9'
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage(chats=['doclenh92lottery', 'Sukien92Lottery', 'BOTWINGO92', 'doclenhvn168', 'sukien168vn', 'hinhanhdangbaivn168', 'vngolenh3phut', 'lenh3p82vnk3', 'sukienvessovn', 'VESOVN5PHUT', -1001749468867, -1001634428201]))
async def my_event_handler(event):
    msg = str(event.raw_text)
    text = msg.split("\n")
    try:
        sender = await event.get_sender()
        sender_name = sender.username
    except:
        pass
    for mess in text:
        mess = mess.rstrip()
        if (len(mess) == 32 or len(mess) == 25) and (" " not in mess) and ("/" not in mess):
            if (sender_name is None):
                print('----------66CLUB----------')
                clubRedpage(mess)
                await client.send_message('claimgame0802', "66club: " + mess)
            else:
                await client.send_message('claimgame0802', sender_name + ": " + mess)
            if (sender_name == 'doclenhvn168' or sender_name == 'sukien168vn' or sender_name == 'hinhanhdangbaivn168'):
                print('----------VN168----------')
                vn168Redpage(mess)
            if (sender_name == 'doclenh92lottery' or sender_name == 'Sukien92Lottery' or sender_name == 'BOTWINGO92'):
                print('----------92LOTTERY----------')
                lotteryRedpage(mess)
            if (sender_name == 'sukienvessovn' or sender_name == 'VESOVN5PHUT'):
                print('----------VESOVN----------')
                vesovnRedpage(mess)
            if (sender_name == 'vngolenh3phut' or sender_name == 'lenh3p82vnk3'):
                print('----------82VN----------')
                vn82Redpage(mess)

client.start()
client.run_until_disconnected()
