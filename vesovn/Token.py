import requests
from datetime import datetime
import threading
import json

phone_path = "vesovn/tk.txt"
with open(phone_path, 'r') as file:
    phones = file.readlines() 

json_path = "vesovn/key.json"
with open(json_path, 'r') as file:
    data = json.load(file)

def GetToken(phone, random, sign):
    # Yêu cầu OPTIONS
    options_url = "https://api.ngrbet.com/api/webapi/Login"
    options_headers = {
        "authority": "vn168api.com",
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "access-control-request-headers": "authorization,content-type",
        "access-control-request-method": "POST",
        "origin": "https://vn168.com",
        "referer": "https://vn168.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    requests.options(options_url, headers=options_headers)

    # Yêu cầu POST
    post_url = "https://api.ngrbet.com/api/webapi/Login"
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
        "username": "84" + phone,
        "pwd": "GiaMinh123",
        "logintype": "mobile",
        "phonetype": 0,
        "language": 0,
        "random": random,
        "signature": sign,
        "timestamp": int(datetime.now().timestamp()) 
    }
    post_response = requests.post(post_url, headers=post_headers, json=post_data).json()

    return post_response['data']['token']

def RunCode(number, phone, login_random, login_sign):
    try:
        token = GetToken(phone, login_random, login_sign)
        data[number]['token'] = token

        formatted_json = json.dumps(data, indent=4, sort_keys=False)
        with open(json_path, 'w') as file:
            file.write(formatted_json)
    except Exception as e:
        print(number + ":" + str(e))

def Token():
    threads = []

    for number in data:
        # listBan = [8,9,10,19,30,34,43,55,65,69,82,86,96,127,143,161,183]
        # if (int(number) not in listBan):
        phone = phones[int(number)-1].strip()
        login_random = data[number]['login']['random']
        login_sign = data[number]['login']['sign']

        thread = threading.Thread(target=RunCode, args=(number, phone, login_random, login_sign))
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

        thread = threading.Thread(target=RunCode, args=(number, phone, login_random, login_sign))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
