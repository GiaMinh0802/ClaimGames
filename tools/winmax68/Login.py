import requests
import json

json_path = 'data/key.json'
with open(json_path, 'r') as file:
    data = json.load(file)

with open('data/tk.txt', 'r') as file:
    phones = file.readlines()

for phone, number in zip(phones, data):
    phone = phone.strip()
    payload = {
        'username': phone,
        'pwd': 'GiaMinh123',
    }
    loginResponse = requests.post('https://winmax68.club/api/webapi/login', data=payload).json()

    data[number]['auth'] = loginResponse['value']
    data[number]['token'] = loginResponse['token']

formatted_json = json.dumps(data, indent=4, sort_keys=False)
with open(json_path, 'w') as file:
    file.write(formatted_json)
