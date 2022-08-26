import json


json_file = open("webinars.json", "r")
data = json.load(json_file)
for dat in data:
    print(dat["speaker"])