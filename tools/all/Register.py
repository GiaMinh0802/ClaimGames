import execjs
from datetime import datetime
import requests
import random
from requests.auth import HTTPProxyAuth
import time

def Register92LOTTERY(random, sign, phone, invitecode, proxy, auth):
    # Yêu cầu OPTIONS
    options_url = "https://92lotteryapi.com/api/webapi/Register"
    options_headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en",
        "Accept-Control-Request-Headers": "ar-real-ip,authorization,content-type",
        "Accept-Control-Request-Method": "POST",
        "Origin": "https://92lottery.com",
        "Referer": "https://92lottery.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    requests.options(options_url, headers=options_headers, proxies=proxy, auth=auth)

    # Yêu cầu POST
    post_url = "https://92lotteryapi.com/api/webapi/Register"

    post_data = {
        "captchaId": "",
        "domainurl": "92lottery.com",
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

def RegisterVN168(random, sign, phone, invitecode, proxy, auth):
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
    requests.options(options_url, headers=options_headers, proxies=proxy, auth=auth)

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

    post_response = requests.post(post_url, json=post_data, proxies=proxy, auth=auth).json()

    return post_response

def RegisterVESOVN(random, sign, phone, invitecode, proxy, auth):
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

def Register82VN(random, sign, phone, invitecode, proxy, auth):
    # Yêu cầu OPTIONS
    options_url = "https://82vn82vnapi.com/api/webapi/Register"
    options_headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en",
        "Accept-Control-Request-Headers": "ar-real-ip,authorization,content-type",
        "Accept-Control-Request-Method": "POST",
        "Origin": "https://82vn.com",
        "Referer": "https://82vn.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    requests.options(options_url, headers=options_headers, proxies=proxy, auth=auth)

    # Yêu cầu POST
    post_url = "https://82vn82vnapi.com/api/webapi/Register"

    post_data = {
        "captchaId": "",
        "domainurl": "82vn.com",
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

def Register66CLUB(random, sign, phone, invitecode, proxy, auth):
    # Yêu cầu OPTIONS
    options_url = "https://66clubapiapi.com/api/webapi/Register"
    options_headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en",
        "Accept-Control-Request-Headers": "ar-real-ip,authorization,content-type",
        "Accept-Control-Request-Method": "POST",
        "Origin": "https://66club.com",
        "Referer": "https://66club.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    requests.options(options_url, headers=options_headers, proxies=proxy, auth=auth)

    # Yêu cầu POST
    post_url = "https://66clubapiapi.com/api/webapi/Register"

    post_data = {
        "captchaId": "",
        "domainurl": "66club.com",
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

with open('../proxy.txt', 'r') as file:
    listProxy = file.readlines()

with open("main.js", "r") as file:
    js_code = file.read()

with open('tk.txt', 'r') as file:
    phones = file.readlines()

js_lib = execjs.compile(js_code)

listInvite92LOTTERY = ['Qtckx364592', 'Mcv7n462062','21QCq5958','4PPxk189497','rb89R284037','UaUdr352255']
listInviteVN168 = ['8166453508', '2238699785', '21133245946', '72128193292', '8323612301', '452724918']
listInviteVESOVN = ['PGVUr61117', '36637182173', '36564308741', '85633148506', '18612390808', '66156336331', '56753157697', 'DUyNp84108']
listInvite82VN = ['443896', '200666', '230165', '564887', '192824', '595459', '242172', '48753']
listInvite66CLUB = ['276923', '565590', '76571679700', '18272261298', '596951', '110646', '291826']

def Run(phone, proxy, auth, game):
    if game == '92lottery':
        invitecode = random.choice(listInvite92LOTTERY)
        domain = '92lottery.com'
    elif game == 'vn168':
        invitecode = random.choice(listInviteVN168)
        domain = 'vn168-1.com'
    elif game == 'vesovn':
        invitecode = random.choice(listInviteVESOVN)
        domain = 'vesovn.cc'
    elif game == '82vn':
        invitecode = random.choice(listInvite82VN)
        domain = '82vn.com'
    else:
        invitecode = random.choice(listInvite66CLUB)
        domain = '66club.com'
  
    pre_payload = {
        "captchaId": "",
        "domainurl": domain,
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
    
    if game == '92lottery':
        response = Register92LOTTERY(result[1], result[0], phone, invitecode, proxy, auth)['msg']
    elif game == 'vn168':
        response = RegisterVN168(result[1], result[0], phone, invitecode, proxy, auth)['msg']
    elif game == 'vesovn':
        response = RegisterVESOVN(result[1], result[0], phone, invitecode, proxy, auth)['msg']
    elif game == '82vn':
        response = Register82VN(result[1], result[0], phone, invitecode, proxy, auth)['msg']
    else:
        response = Register66CLUB(result[1], result[0], phone, invitecode, proxy, auth)['msg']
  
    if (response != "Succeed"):
        print(response)
    else:
        print(game)

for phone in phones:
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

    phone = phone.strip()
    
    print(phone)

    Run(phone, proxy, auth, '92lottery')
    Run(phone, proxy, auth, 'vn168')
    Run(phone, proxy, auth, 'vesovn')
    Run(phone, proxy, auth, '82vn')
    Run(phone, proxy, auth, '66club')
    
    print('---------------') 
    
    time.sleep(random.randint(120,300))