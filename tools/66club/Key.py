import json
import requests

with open("data/tk.txt", 'r') as file:
    phones = file.readlines()

with open('data/key.json', 'r') as f:
    data = json.load(f)

for phone, number in zip(phones, data):
    param = {
            "username" : phone.strip(),
            'pwd' : "GiaMinh123",
            'phonetype': "0",
            'language': 'vi'
        }

    response = requests.post('https://66clubapiapi.com/api/webapi/UserLogin', data=param)
    response = response.json()
    try:
        sign = response['data']['Sign']
        uid = response['data']['UserId']
        data[number]['uid'] = uid
        data[number]['sign'] = sign
    except:
        print(phone.strip() + ": " + response['msg'])
formatted_json = json.dumps(data, indent=4, sort_keys=False)
with open('data/key.json', 'w') as file:
    file.write(formatted_json)