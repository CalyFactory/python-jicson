import jicson
import json 

result = jicson.fromFile('./basic.ics')
print(result)
print(json.dumps(result))