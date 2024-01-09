import requests
import sys
import random
import win32com.shell.shell as shell
import time

def ResetDcom(nameDcom):
    commands = 'netsh interface set interface "' + nameDcom + '" disable'
    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c ' + commands)
    time.sleep(1)
    commands = 'netsh interface set interface "' + nameDcom + '" enable'
    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c ' + commands)
    ip = ""
    i = 0
    while ip == "":
        if (i == 5):
            commands = 'netsh interface set interface "' + nameDcom + '" disable'
            shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c ' + commands)
            time.sleep(1)
            commands = 'netsh interface set interface "' + nameDcom + '" enable'
            shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c ' + commands)
            i = 0
        try:
            ip = requests.get('https://api.ipify.org/?format=json').json()["ip"]
            i = i + 1
        except:
            pass

listInvite = ['Qtckx364592', 'Mcv7n462062','996427','21QCq5958','4PPxk189497','rb89R284037','UaUdr352255']
inviteCode = random.choice(listInvite)
phone = sys.argv[1]

param = {
    "username": phone,
    "smsvcode": "",
    "pwd": "GiaMinh123",
    "regtype": "",
    "invitecode": inviteCode,
    "domainurl": "92lottery.com",
    "phonetype": "0",
    "language": "vi"
}
ResetDcom("Cellular 7")

response = requests.post('https://92lotteryapi.com/api/webapi/Register', data=param)
response = response.json()

if (response['success'] is True):
    with open('data/uid.txt', 'a') as uid_file:
        uid_file.write(str(response['data']['UserId']) + '\n')
    with open('data/sign.txt', 'a') as sign_file:
        sign_file.write(str(response['data']['Sign']) + '\n')
else:
    print(response)