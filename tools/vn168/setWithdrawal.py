import requests
import execjs
from datetime import datetime
import openpyxl
import re
import random
import time

def SetWithdrawal(random, sign, name, accNo, email, phone, address, token):
    # Yêu cầu OPTIONS
    options_url = "https://vn168api.com/api/webapi/SetWithdrawalBankCard"
    options_headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en",
        "Accept-Control-Request-Headers": "ar-real-ip,authorization,content-type",
        "Accept-Control-Request-Method": "POST",
        "Origin": "https://vn168-1.com",
        "Referer": "https://vn168-1.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    requests.options(options_url, headers=options_headers)

    # Yêu cầu POST
    post_url = "https://vn168api.com/api/webapi/SetWithdrawalBankCard"
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
        "smsCode": "",
        "ifsccode": "",
        "bankid": 102,
        "beneficiaryname": name,
        "accountno": accNo,
        "email": email,
        "mobileno": "84" + phone,
        "bankcitycode": "",
        "bankprovincecode": "",
        "bankbranchaddress": address,
        "type": "",
        "codeType": 6,
        "language": 2,
        "random": random,
        "signature": sign,
        "timestamp": int(datetime.now().timestamp())
    }

    post_response = requests.post(post_url, json=post_data, headers=post_headers).json()

    return post_response

def GetToken(phone, random, sign):
    # Yêu cầu OPTIONS
    options_url = "https://vn168api.com/api/webapi/Login"
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
    post_url = "https://vn168api.com/api/webapi/Login"
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

with open("main.js", "r") as file:
    js_code = file.read()

js_lib = execjs.compile(js_code)

wb = openpyxl.load_workbook('data/stk.xlsx')

with open('data/signature.txt', 'r') as file:
    auth = file.read()

random_values = re.findall(r'"random":"(.*?)"', auth)
signature_values = re.findall(r'"signature":"(.*?)"', auth)

sheet = wb['Sheet1']
g_all = sheet.values
listInfos = list(g_all)
listInfos = listInfos[1:]
for info, randoms, sign in zip(listInfos, random_values, signature_values):
    pre_payload = {
        "smsCode": "",
        "ifsccode": "",
        "bankid": 102,
        "beneficiaryname": info[1],
        "accountno": info[2],
        "email": info[4],
        "mobileno": "84" + info[3],
        "bankcitycode": "",
        "bankprovincecode": "",
        "bankbranchaddress": info[5],
        "type": "",
        "codeType": 6,
        "language": 2,
    }
    try:
        token = GetToken(info[3], randoms, sign)
    except:
        print(info[3])
        continue
    result = js_lib.call("getSignature", pre_payload)
    response = SetWithdrawal(result[1], result[0], info[1], info[2], info[4], info[3], info[5], token)
    print(response)
    time.sleep(random.randint(10,15))