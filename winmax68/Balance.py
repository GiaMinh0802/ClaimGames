import requests
import json

json_path = 'winmax68/key.json'

with open(json_path, 'r') as file:
    data = json.load(file)

for number in data:
    auth = data[number]['auth']
    token = data[number]['token']

    headers = {
        'Cookie': 'token=' + token + '; auth=' + auth
    }
    userInfo = requests.get('https://winmax68.club/api/webapi/GetUserInfo', headers=headers).json()
    try:
        amount = str(int(userInfo['data']['money_user']/1000))
    except:
        amount = None
    print(amount)