import execjs
from datetime import datetime
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

with open("main.js", "r") as file:
    js_code = file.read()

js_lib = execjs.compile(js_code)

listInvite = ['8166453508', '2238699785', '21133245946', '72128193292', '8323612301', '452724918']
invitecode = random.choice(listInvite)

phone = sys.argv[1]

pre_payload = {
    "captchaId": "",
    "domainurl": "vn168-1.com",
    "invitecode": invitecode,
    "language": 2,
    "phonetype": 0,
    "pwd": "GiaMinh123",
    "registerType": "mobile",
    "regtype": "",
    "smsvcode": "",
    "track": "",
    "username": "84" + phone
}

result = js_lib.call("getSignature", pre_payload)

def Register(random, sign, phone):
    # Yêu cầu OPTIONS
    options_url = "https://vn168api.com/api/webapi/Register"
    options_headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en",
        "Accept-Control-Request-Headers": "ar-real-ip,authorization,content-type",
        "Accept-Control-Request-Method": "POST",
        "Origin": "https://vn168-1.com",
        "Referer": "https://vn168-1.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    requests.options(options_url, headers=options_headers)

    # Yêu cầu POST
    post_url = "https://vn168api.com/api/webapi/Register"

    post_data = {
        "captchaId": "",
        "domainurl": "vn168-1.com",
        "invitecode": invitecode,
        "language": 2,
        "phonetype": 0,
        "pwd": "GiaMinh123",
        "random": random,
        "registerType": "mobile",
        "regtype": "",
        "signature": sign,
        "smsvcode": "",
        "timestamp": int(datetime.now().timestamp()) ,
        "track": "",
        "username": "84" + phone
    }

    post_response = requests.post(post_url, json=post_data).json()

    return post_response

# ResetDcom("")
print(Register(result[1], result[0], phone)['msg'])