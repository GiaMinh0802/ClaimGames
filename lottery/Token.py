import requests
from datetime import datetime
import threading
import json
from requests.auth import HTTPProxyAuth

phone_path = "lottery/tk.txt"
with open(phone_path, 'r') as file:
    phones = file.readlines() 

json_path = "lottery/key.json"
with open(json_path, 'r') as file:
    data = json.load(file)

with open('proxy.txt', 'r') as file:
    listProxy = file.readlines()

def GetToken(phone, random, sign, proxy, auth):
    # Yêu cầu OPTIONS
    options_url = "https://92lotteryapi.com/api/webapi/Login"
    options_headers = {
        "authority": "92lotteryapi.com",
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "access-control-request-headers": "authorization,content-type",
        "access-control-request-method": "POST",
        "origin": "https://92lotteryapi.com",
        "referer": "92lotteryapi.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    requests.options(options_url, headers=options_headers)

    # Yêu cầu POST
    post_url = "https://92lotteryapi.com//api/webapi/Login"
    post_headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "authorization": "Bearer",
        "content-type": "application/problem+json; charset=UTF-8",
        "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site"
    }
    post_data = {
        "language": 2,
        "logintype": "mobile",
        "phonetype": -1,
        "pwd": "GiaMinh123",
        "random": random,
        "signature": sign,
        "timestamp": int(datetime.now().timestamp()),
        "username": "84" + phone
    }
    post_response = requests.post(post_url, headers=post_headers, json=post_data).json()

    return post_response['data']['token']

def RunCode(number, phone, login_random, login_sign, data, json_path, proxy, auth):
    try:
        token = GetToken(phone, login_random, login_sign, proxy, auth)
        data[number]['token'] = token

        formatted_json = json.dumps(data, indent=4, sort_keys=False)
        with open(json_path, 'w') as file:
            file.write(formatted_json)
    except Exception as e:
        print(number + ":" + str(e))

def Token():
    threads = []

    for number, proxyRaw in zip(data, listProxy):
        phone = phones[int(number)-1].strip()
        login_random = data[number]['login']['random']
        login_sign = data[number]['login']['sign']

        ip = proxyRaw[0]
        port = proxyRaw[1]
        user = proxyRaw[2]
        pwd = proxyRaw[3]
        proxy = {
            'http': 'http://' + ip + ":" + port,
            'https': 'http://' + ip + ":" + port
        }
        auth = HTTPProxyAuth(user, pwd)

        thread = threading.Thread(target=RunCode, args=(number, phone, login_random, login_sign, data, json_path, proxy, auth))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

def main():
    threads = []

    for number, proxyRaw in zip(data, listProxy):
        phone = phones[int(number)-1].strip()
        login_random = data[number]['login']['random']
        login_sign = data[number]['login']['sign']

        ip = proxyRaw[0]
        port = proxyRaw[1]
        user = proxyRaw[2]
        pwd = proxyRaw[3]
        proxy = {
            'http': 'http://' + ip + ":" + port,
            'https': 'http://' + ip + ":" + port
        }
        auth = HTTPProxyAuth(user, pwd)

        thread = threading.Thread(target=RunCode, args=(number, phone, login_random, login_sign, data, json_path, proxy, auth))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
