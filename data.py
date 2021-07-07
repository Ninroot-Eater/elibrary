import json

f= open("data.json","r")
x = json.load(f)
x['mm'] = "sp"
f.close()
open("data.json","w").write(json.dumps(x))





