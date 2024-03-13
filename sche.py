import schedule
import time
from lottery.Token import Token as lotteryToken
from vn168.Token import Token as vn168Token

def job():
    print(time.strftime("%H:%M:%S"))
    lotteryToken()
    print('92LOTTERY -> DONE')
    vn168Token()
    print('VN168 -> DONE')

def create_schedule():
    schedule.every().day.at("14:20").do(job)
    schedule.every().day.at("14:50").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

create_schedule()