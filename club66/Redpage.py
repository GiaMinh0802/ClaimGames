import json
import requests
import threading

file_path = "club66/key.json"

def GetRedpage(giftcode, uid, sign):
    param = {
        'uid': uid,
        'sign': sign,
        'giftcode': giftcode,
        'language': 'vi'
    }

    response = requests.post('https://66clubapiapi.com/api/webapi/ConversionRedpage', data=param)
    response = response.json()
    return response

def RunCode(number, item, giftcode):
    uid = item["uid"]
    sign = item["sign"]
    try:
        response = GetRedpage(giftcode, uid, sign)
        print(number + ":" + response['msg'])
    except Exception as e:
        print(number + ":" + str(e))
        
def clubRedpage(giftcode):
    with open(file_path, 'r') as file:
        data = json.load(file)
        
    threads = []

    for number, item in data.items():
        thread = threading.Thread(target=RunCode, args=(number, item, giftcode))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

def main():
    with open(file_path, 'r') as file:
        data = json.load(file)

    print("------66CLUB------")
    giftcode = input("Mã lì xì: ")

    threads = []

    for number, item in data.items():
        thread = threading.Thread(target=RunCode, args=(number, item, giftcode))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()