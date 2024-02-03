import requests
from datetime import datetime
import json

json_path = "vn168/key.json"
with open(json_path, 'r') as file:
    data = json.load(file)
    
def GetBanlance(random, sign, token):
    # Yêu cầu OPTIONS
    options_url = "https://vn168api.com/api/webapi/GetUserInfo"
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
    post_url = "https://vn168api.com/api/webapi/GetUserInfo"
    post_headers = {
        "authority": "vn168api.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "authorization": "Bearer " + token,
        "content-type": "application/problem+json; charset=UTF-8",
        "origin": "https://vn168.com",
        "referer": "https://vn168.com/",
        "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    post_data = {
        "signature": sign,
        "language": 2,
        "random": random,
        "timestamp": int(datetime.now().timestamp()) 
    }

    post_response = requests.post(post_url, headers=post_headers, json=post_data).json()

    amount = None

    try:
        amount = str(int(post_response['data']['amount']/1000))
    except:
        amount = None

    return amount

for number in data:

    token = data[number]['token']

    balance_random = data[number]['balance']['random']
    balance_sign = data[number]['balance']['sign']

    balance = GetBanlance(balance_random, balance_sign, token)

    print(balance)
