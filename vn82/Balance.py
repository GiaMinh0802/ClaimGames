import json
import requests

file_path = "vn82/key.json"

with open(file_path, 'r') as file:
    data = json.load(file)

for number in data:
    if (int(number) > 100):
        break
    param = {'uid' : data[number]['uid'],
            'sign' : data[number]['sign'],
            'language': 'vi'}

    response = requests.post('https://82vn82vnapi.com/api/webapi/GetUserInfo', data=param)
    response = response.json()
    print(str(int(response['data']['Amount']/1000)))