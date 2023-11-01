import requests
import sys

phone = "+84" + sys.argv[1]

param = {
    "username": phone,
    "smsvcode": "",
    "pwd": "GiaMinh123",
    "regtype": "",
    "invitecode": "Qs35D611400",
    "domainurl": "92lottery.com",
    "phonetype": "0",
    "language": "vi"
}

response = requests.post('https://82vn82vnapi.com/api/webapi/Register', data=param)
response = response.json()
if (response['success'] is True):
    print(response['data']['UserId'])
    print(response['data']['Sign'])
else:
    print(response)