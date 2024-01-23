import json

with open('data/uid.txt', 'r') as f:
    uids = f.readlines()

with open('data/sign.txt', 'r') as f:
    signs = f.readlines()

with open('data/number.txt', 'r') as f:
    numbers = f.readlines()

with open('data/key.json', 'r') as f:
    data = json.load(f)

for uid, sign, number in zip(uids, signs, numbers):
    uid = int(uid.strip())
    sign = sign.strip()
    number = number.strip()
    data[number]['uid'] = uid
    data[number]['sign'] = sign

formatted_json = json.dumps(data, indent=4, sort_keys=False)
with open('data/key.json', 'w') as file:
    file.write(formatted_json)