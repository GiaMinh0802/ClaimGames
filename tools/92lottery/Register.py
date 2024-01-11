import requests
import sys
import random
import requests
import win32com.shell.shell as shell
import time

def ResetDcom(nameDcom):
    max_attempts = 5
    attempts = 0
    while attempts < max_attempts:
        commands_disable = f'netsh interface set interface "{nameDcom}" disable'
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c ' + commands_disable)
        time.sleep(1)
        commands_enable = f'netsh interface set interface "{nameDcom}" enable'
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c ' + commands_enable)
        ip = ""
        while ip == "":
            try:
                ip = requests.get('https://api.ipify.org/?format=json').json()["ip"]
            except:
                pass
        if ip != "":
            break
        attempts += 1
    if attempts == max_attempts:
        ResetDcom(nameDcom)

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

ResetDcom("Mobile 2")

response = requests.post('https://92lotteryapi.com/api/webapi/Register', data=param)
response = response.json()

if (response['success'] is True):
    with open('data/uid.txt', 'a') as uid_file:
        uid_file.write(str(response['data']['UserId']) + '\n')
    with open('data/sign.txt', 'a') as sign_file:
        sign_file.write(str(response['data']['Sign']) + '\n')
else:
    print(response)