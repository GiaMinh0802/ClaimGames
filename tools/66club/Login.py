import requests

param = {
    "username" : "0396600487",
    'pwd' : "GiaMinh123",
    'regtype': '1',
    'phonetype': "0",
    'language': 'vi'
}

response = requests.post('https://66clubapiapi.com/api/webapi/UserLogin', data=param)
response = response.json()
try:
    print(response['data']['Sign'])
    print(response['data']['UserId'])
except:
    print(response)
