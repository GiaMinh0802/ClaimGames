import execjs
from datetime import datetime
import requests
import sys
import random
from requests.auth import HTTPProxyAuth

with open('../proxy.txt', 'r') as file:
    listProxy = file.readlines()

proxyRaw = random.choice(listProxy).strip().split(":")

ip = proxyRaw[0]
port = proxyRaw[1]
user = proxyRaw[2]
pwd = proxyRaw[3]

proxy = {
   'http': 'http://' + ip + ":" + port,
   'https': 'http://' + ip + ":" + port
}
auth = HTTPProxyAuth(user, pwd)

with open("main.js", "r") as file:
    js_code = file.read()

js_lib = execjs.compile(js_code)

listInvite = ['PGVUr61117', '36637182173', '36564308741', '85633148506', '18612390808', '66156336331', '56753157697', 'DUyNp84108']
invitecode = random.choice(listInvite)

phone = sys.argv[1]

pre_payload = {
    "captchaId": "",
    "domainurl": "vesovn.cc",
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
    options_url = "https://api.ngrbet.com/api/webapi/Register"
    options_headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en",
        "Accept-Control-Request-Headers": "ar-real-ip,authorization,content-type",
        "Accept-Control-Request-Method": "POST",
        "Origin": "https://vesovn.cc",
        "Referer": "https://vesovn.cc",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    requests.options(options_url, headers=options_headers, proxies=proxy, auth=auth)

    # Yêu cầu POST
    post_url = "https://api.ngrbet.com/api/webapi/Register"

    post_data = {
        "captchaId": "",
        "domainurl": "vesovn.cc",
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

    post_response = requests.post(post_url, json=post_data, proxies=proxy, auth=auth).json()

    return post_response

response = Register(result[1], result[0], phone)['msg']
if (response != "Succeed"):
    print(response)