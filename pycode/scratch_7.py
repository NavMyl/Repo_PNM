import json

with open('states.json') as st_json:
    data = json.load(st_json)

for state in data['states']:
    print (state['name'],state['abbreviation'])