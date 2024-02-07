import json
import re

phone_path = "data/tk.txt"
json_path = "data/key.json"
input_file = "data/signature.txt"

with open(input_file, "r") as file:
    auth = file.read()

with open(json_path, 'r') as file:
    data = json.load(file)

random_values = re.findall(r'"random":"(.*?)"', auth)
signature_values = re.findall(r'"signature":"(.*?)"', auth)

for rand, sign, number in zip(random_values, signature_values, data):
    data[number]["balance"]["random"] = rand
    data[number]["balance"]["sign"] = sign
    formatted_json = json.dumps(data, indent=4, sort_keys=False)
    with open(json_path, 'w') as file:
        file.write(formatted_json)