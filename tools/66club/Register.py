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

listInvite = ['276923', '565590']
inviteCode = random.choice(listInvite)
phone = sys.argv[1]

param = {
    "username": phone,
    "smsvcode": "",
    "pwd": "GiaMinh123",
    "regtype": "1",
    "invitecode": inviteCode,
    "domainurl": "66club.com",
    "phonetype": "0",
    "language": "vi"
}

ResetDcom("Cellular 7")

response = requests.post('https://66clubapiapi.com/api/webapi/Register', data=param)
response = response.json()

if (response['success'] is True):
    print(response['data']['UserId'])
    print(response['data']['Sign'])
    with open('data/uid.txt', 'a') as file:
        file.write(response['data']['UserId'] + '\n')

    with open('data/sign.txt', 'a') as file:
        file.write(response['data']['Sign'] + '\n')

    with open('data/tk.txt', 'a') as file:
        file.write(phone + '\n')
else:
    print(response)