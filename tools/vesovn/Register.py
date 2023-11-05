from pythonmonkey import require as js_require

js_lib = js_require('./main')

invitecode = ""
phone = ""

payload = {
    "captchaId": "",
    "domainurl": "www.vesovn.cc",
    "invitecode": invitecode,
    "language": 0,
    "phonetype": 0,
    "pwd": "GiaMinh123",
    "random": "4345f1e8759c42719cbd3bd2dbbc0d78",
    "registerType": "mobile",
    "regtype": "",
    "smsvcode": "",
    "track": "",
    "username": "84" + phone
}

print(type(js_lib.getSignature(payload)))