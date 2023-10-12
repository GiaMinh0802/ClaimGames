import json
import requests

file_path = "lottery/key.json"

with open(file_path, 'r') as file:
    data = json.load(file)

for number in data:
    param = {'uid' : data[number]['uid'],
            'sign' : data[number]['sign'],
            'language': 'vi'}

    response = requests.post('https://92lotteryapi.com/api/webapi/GetUserInfo', data=param)
    response = response.json()
    print(str(int(response['data']['Amount']/1000)))