import jicson
import json 
import requests

result = jicson.fromFile('./basic.ics')
print(result)
print(json.dumps(result))

