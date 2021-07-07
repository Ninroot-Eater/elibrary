import json

with open("data.json","r") as f:
    x = json.load(f)
    x['ok'] = "ok"
    json.dumps(x,f)


