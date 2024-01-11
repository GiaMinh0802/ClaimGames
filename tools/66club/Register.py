import requests
import sys
import random
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

# ResetDcom("")

response = requests.post('https://66clubapiapi.com/api/webapi/Register', data=param)
response = response.json()

if (response['success'] is True):
    with open('data/uid.txt', 'a') as uid_file:
        uid_file.write(str(response['data']['UserId']) + '\n')
    with open('data/sign.txt', 'a') as sign_file:
        sign_file.write(str(response['data']['Sign']) + '\n')
else:
    print(response)