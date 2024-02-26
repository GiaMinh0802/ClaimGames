import requests
from datetime import datetime
import threading
import json

phone_path = "lottery/tk.txt"
with open(phone_path, 'r') as file:
    phones = file.readlines() 

json_path = "lottery/key.json"
with open(json_path, 'r') as file:
    data = json.load(file)

def GetToken(phone, random, sign):
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

def RunCode(number, phone, login_random, login_sign, data, json_path):
    try:
        token = GetToken(phone, login_random, login_sign)
        data[number]['token'] = token

        formatted_json = json.dumps(data, indent=4, sort_keys=False)
        with open(json_path, 'w') as file:
            file.write(formatted_json)

        with open(json_path, 'r') as file:
            json_text = file.readlines()
        json_text[4401] = '}'
        json_text = json_text[:4402]
        json_correct = ''.join(json_text)
        with open(json_path, 'w') as file:
            file.write(json_correct)
    except Exception as e:
        print(number + ":" + str(e))

def Token():
    threads = []

    for number in data:
        phone = phones[int(number)-1].strip()
        login_random = data[number]['login']['random']
        login_sign = data[number]['login']['sign']

        thread = threading.Thread(target=RunCode, args=(number, phone, login_random, login_sign, data, json_path))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

def main():
    threads = []

    for number in data:
        phone = phones[int(number)-1].strip()
        login_random = data[number]['login']['random']
        login_sign = data[number]['login']['sign']

        thread = threading.Thread(target=RunCode, args=(number, phone, login_random, login_sign, data, json_path))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
