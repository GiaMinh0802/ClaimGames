import execjs
from datetime import datetime
import requests
import sys

with open("main.js", "r") as file:
    js_code = file.read()

js_lib = execjs.compile(js_code)

invitecode = "2238699785"
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

def GetMyIp():
    response = requests.get('https://httpbin.org/ip')
    if response.status_code == 200:
        data = response.json()
        return data['origin']

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

    ip = GetMyIp()
    print(ip)

    # Yêu cầu POST
    post_url = "https://vn168api.com/api/webapi/Register"
    post_headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en",
        "Ar-Real-Ip": ip,
        "Authorization": "",
        "Content-Length": "315",
        "Content-Type": "application/problem+json; charset=UTF-8",
        "Origin": "https://vn168-1.com",
        "Referer": "https://vn168-1.com/",
        "Sec-Ch-Ua": '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        "Sec-Ch-Ua-mobile": "?0",
        "Sec-Ch-Ua-platform": "Windows",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

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

    post_response = requests.post(post_url, headers=post_headers, json=post_data)

    return post_response

print(Register(result[1], result[0], phone))