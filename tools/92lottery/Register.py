import requests
import sys
import random

listInvite = ['Qtckx364592', 'Mcv7n462062','996427','21QCq5958','4PPxk189497','rb89R284037','UaUdr352255']
inviteCode = random.choice(listInvite)
phone = sys.argv[1]

param = {
    "username": "+84" + phone,
    "smsvcode": "",
    "pwd": "GiaMinh123",
    "regtype": "",
    "invitecode": inviteCode,
    "domainurl": "92lottery.com",
    "phonetype": "0",
    "language": "vi"
}

response = requests.post('https://92lotteryapi.com/api/webapi/Register', data=param)
response = response.json()

if (response['success'] is True):
    with open('data/uid.txt', 'a') as uid_file:
        uid_file.write(str(response['data']['UserId']) + '\n')
    with open('data/sign.txt', 'a') as sign_file:
        sign_file.write(str(response['data']['Sign']) + '\n')
else:
    print(response)