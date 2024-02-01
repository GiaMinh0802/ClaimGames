from telethon import TelegramClient, events
from lottery.Redpage import lotteryRedpage
# from vn82.Redpage import vn82Redpage
from vesovn.Redpage import vesovnRedpage
from vn168.Redpage import vn168Redpage
# from club66.Redpage import clubRedpage
import time

listReceived = []

print('Started')

api_id = '28222709'
api_hash = 'cbe0badef0a05463b386cac35dbfb4e9'
client = TelegramClient('anon', api_id, api_hash)

async def get_chat_name(chat_id):
    entity = await client.get_entity(chat_id)
    return entity.title
#, -1001634428201, -1001749468867
@client.on(events.NewMessage(chats=[-1001172657538, -1001842592179, -1001886568136, -1001887175434, -1001958370435, -1001966552444, -1001975632908, -1001925286709, -1001935258958, -1001808293140, -1001761532313, -1001822029296, -1002116803365, -1001918719770]))
async def my_event_handler(event):
    msg = str(event.raw_text)
    text = msg.split("\n")
    chat_id = event.chat_id
    chat_name = await get_chat_name(chat_id)
    for mess in text:
        mess = mess.rstrip()
        if (len(mess) == 32 or len(mess) == 25) and (" " not in mess) and ("/" not in mess) and (mess not in listReceived):

            listReceived.append(mess)
            
            if (chat_id in [-1001172657538, -1001842592179, -1001886568136]):
                print('----------92LOTTERY----------')
                lotteryRedpage(mess)
            
            if (chat_id in [-1001887175434, -1001958370435, -1001966552444]):
                print('----------VN168----------')
                vn168Redpage(mess)
                
            if (chat_id in [-1001975632908, -1001925286709]):
                print('----------VESOVN----------')
                vesovnRedpage(mess)

            # if (chat_id in [-1001935258958, -1001808293140, -1001761532313, -1001822029296, -1002116803365, -1001918719770]):
            #     print('----------82VN----------')
            #     vn82Redpage(mess)

            # if (chat_id in [-1001634428201, -1001749468867]):
            #     print('----------66CLUB----------')
            #     clubRedpage(mess)

            await client.send_message('claimgame0802', chat_name + ": " + mess)

client.start()
client.run_until_disconnected()
