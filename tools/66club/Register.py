import requests
import sys
import random
from requests.auth import HTTPProxyAuth

listInvite = ['276923', '565590']
inviteCode = random.choice(listInvite)
phone = sys.argv[1]

param = {
    "username": phone,
    "smsvcode": "",
    "pwd": "GiaMinh123",
    "regtype": "1",
    "invitecode": inviteCode,
    "domainurl": "66club.com",
    "phonetype": "0",
    "language": "vi"
}

with open('../proxy.txt', 'r') as file:
    listProxy = file.readlines()

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

response = requests.post('https://66clubapiapi.com/api/webapi/Register', data=param, proxies=proxy, auth=auth)
response = response.json()

if (response['success'] is True):
    with open('data/uid.txt', 'a') as uid_file:
        uid_file.write(str(response['data']['UserId']) + '\n')
    with open('data/sign.txt', 'a') as sign_file:
        sign_file.write(str(response['data']['Sign']) + '\n')
else:
    print(response)