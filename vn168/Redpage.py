import requests
from datetime import datetime
import json
import re
import threading
import subprocess
import jwt

input_file = "vn168/signature.txt"
json_path = "vn168/key.json"

def GetRedpage(giftcode, random, sign, token):
    # Yêu cầu OPTIONS
    options_url = "https://vn168api.com/api/webapi/ConversionRedpage"
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
    post_url = "https://vn168api.com/api/webapi/ConversionRedpage"
    post_headers = {
        "authority": "vn168api.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "authorization": "Bearer " + token,
        "content-type": "application/problem+json; charset=UTF-8",
        "origin": "https://vn168.com",
        "referer": "https://vn168.com/",
        "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    post_data = {
        "giftcode": giftcode,
        "language": 2,
        "random": random,
        "signature": sign,
        "timestamp": int(datetime.now().timestamp()) 
    }

    post_response = requests.post(post_url, headers=post_headers, json=post_data).json()

    return post_response

def RunCode(rand, sign, number, giftcode, data):
    token = data[number]['token']
    response = GetRedpage(giftcode, rand, sign, token)
    print(number + ":" + response['msg'])

def vn168Redpage(giftcode):
    from vn168.Token import Token
    with open(json_path, 'r') as file:
        data = json.load(file)

    token = data["1"]['token']
    try:
        decoded_token = jwt.decode(token, verify=False)
        expiration_time = datetime.fromtimestamp(int(decoded_token['exp']))
        current_time = datetime.now()
        if current_time > expiration_time:
            Token()
    except Exception as e:
            print(e)

    result = subprocess.run(["node", 'vn168/main.js', giftcode], capture_output=True, text=True, check=True)

    output = result.stdout.strip()

    with open(input_file, "w") as file:
        file.writelines(output)

    with open(input_file, "r") as file:
        auth = file.read()

    random_values = re.findall(r'"random":"(.*?)"', auth)
    signature_values = re.findall(r'"signature":"(.*?)"', auth)

    threads = []

    with open(json_path, 'r') as file:
        data = json.load(file)

    for rand, sign, number in zip(random_values, signature_values, data):
        thread = threading.Thread(target=RunCode, args=(rand, sign, number, giftcode, data))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

def main():
    from Token import Token
    print("------VN168------")
    giftcode = input("Mã lì xì: ")

    with open(json_path, 'r') as file:
        data = json.load(file)

    token = data["1"]['token']
    try:
        decoded_token = jwt.decode(token, verify=False)
        expiration_time = datetime.fromtimestamp(int(decoded_token['exp']))
        current_time = datetime.now()
        if current_time > expiration_time:
            Token()
    except Exception as e:
            print(e)

    result = subprocess.run(["node", 'vn168/main.js', giftcode], capture_output=True, text=True, check=True)

    output = result.stdout.strip()

    with open(input_file, "w") as file:
        file.writelines(output)

    with open(input_file, "r") as file:
        auth = file.read()

    random_values = re.findall(r'"random":"(.*?)"', auth)
    signature_values = re.findall(r'"signature":"(.*?)"', auth)

    threads = []

    with open(json_path, 'r') as file:
        data = json.load(file)

    for rand, sign, number in zip(random_values, signature_values, data):
        thread = threading.Thread(target=RunCode, args=(rand, sign, number, giftcode, data))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
