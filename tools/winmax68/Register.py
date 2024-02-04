import requests
import sys
import random

listInvite = ['yGHdK328434', 'NdsSP682839', 'eMpFq22085', 'frZys365681', 'CQnkK884979', 'KWZZw54956']
invitecode = random.choice(listInvite)

phone = sys.argv[1]

requests.post('https://winmax68.club/api/sent/otp/verify', data={'phone':phone})

for otp in range(19):
    data = {
        'username': phone,
        'pwd': 'GiaMinh123',
        'invitecode': invitecode,
        'otp': str(otp)
    }
    try:
        registerResponse = requests.post('https://winmax68.club/api/webapi/register', data=data)
        registerResponse = registerResponse.json()
        if (registerResponse['status'] == True):
            break
    except:
        print(registerResponse.content)