import requests
import json

json_path = 'winmax68/key.json'

with open(json_path, 'r') as file:
    data = json.load(file)

print("------WINMAX68------")
giftcode = input("Mã lì xì: ")

for number in data:
    auth = data[number]['auth']
    token = data[number]['token']

    payload = {
        'code': giftcode
    }
    headers = {
        'Cookie': 'token=' + token + '; auth=' + auth
    }
    redPage = requests.post('https://winmax68.club/api/webapi/use/redenvelope', headers=headers, data=payload).json()
    print(number + ":" + redPage['message'])