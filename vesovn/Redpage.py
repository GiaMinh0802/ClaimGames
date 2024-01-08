import requests
from datetime import datetime
import json
import re
import subprocess
import jwt

phone_path = "vesovn/tk.txt"
input_file = "vesovn/signature.txt"
json_path = "vesovn/key.json"

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

def GetRedpage(giftcode, random, sign, token):
    # Yêu cầu OPTIONS
    options_url = "https://api.ngrbet.com/api/webapi/ConversionRedpage"
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
    post_url = "https://api.ngrbet.com/api/webapi/ConversionRedpage"
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
        "giftCode": giftcode,
        "language": 2,
        "random": random,
        "signature": sign,
        "timestamp": int(datetime.now().timestamp()) 
    }

    post_response = requests.post(post_url, headers=post_headers, json=post_data).json()

    return post_response

def vesovnRedpage(giftcode):
    with open(phone_path, 'r') as file:
        phones = file.readlines() 

    with open(json_path, 'r') as file:
        data = json.load(file)

    result = subprocess.run(["node", 'vesovn/main.js', giftcode], capture_output=True, text=True, check=True)

    output = result.stdout.strip()

    with open(input_file, "w") as file:
        file.writelines(output)

    with open(input_file, "r") as file:
        auth = file.read()

    random_values = re.findall(r'"random":"(.*?)"', auth)
    signature_values = re.findall(r'"signature":"(.*?)"', auth)

    for phone, rand, sign, number in zip(phones, random_values, signature_values, data):
        if (int(number) in []):
            continue
        else:
            token = data[number]['token']
            try:
                decoded_token = jwt.decode(token, verify=False)
                expiration_time = datetime.fromtimestamp(int(decoded_token['exp']))
                current_time = datetime.now()
                if current_time > expiration_time:
                    try:
                        token = GetToken(phone.strip(), data[number]['login']['random'], data[number]['login']['sign'])
                        data[number]['token'] = token

                        formatted_json = json.dumps(data, indent=4, sort_keys=False)
                        with open(json_path, 'w') as file:
                            file.write(formatted_json)
                    except Exception as e:
                        print(number + ":" + str(e))
                        continue
            except Exception as e:
                print(e)
            response = GetRedpage(giftcode, rand, sign, token)
            print(number + ":" + response['msg'])
            if response['msg'] != 'Exchange successful':
                break

def main():
    print("------VESOVN------")
    giftcode = input("Mã lì xì: ")

    with open(phone_path, 'r') as file:
        phones = file.readlines() 

    with open(json_path, 'r') as file:
        data = json.load(file)

    result = subprocess.run(["node", 'vesovn/main.js', giftcode], capture_output=True, text=True, check=True)

    output = result.stdout.strip()

    with open(input_file, "w") as file:
        file.writelines(output)

    with open(input_file, "r") as file:
        auth = file.read()

    random_values = re.findall(r'"random":"(.*?)"', auth)
    signature_values = re.findall(r'"signature":"(.*?)"', auth)

    for phone, rand, sign, number in zip(phones, random_values, signature_values, data):
        if (int(number) in []):
            continue
        else:
            token = data[number]['token']
            try:
                decoded_token = jwt.decode(token, verify=False)
                expiration_time = datetime.fromtimestamp(int(decoded_token['exp']))
                current_time = datetime.now()
                if current_time > expiration_time:
                    try:
                        token = GetToken(phone.strip(), data[number]['login']['random'], data[number]['login']['sign'])
                        data[number]['token'] = token

                        formatted_json = json.dumps(data, indent=4, sort_keys=False)
                        with open(json_path, 'w') as file:
                            file.write(formatted_json)
                    except Exception as e:
                        print(number + ":" + str(e))
                        continue
            except Exception as e:
                print(e)
            response = GetRedpage(giftcode, rand, sign, token)
            print(number + ":" + response['msg'])
            if response['msg'] != 'Exchange successful':
                break

if __name__ == "__main__":
    main()
