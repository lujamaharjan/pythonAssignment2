"""
18) 
"""
import json
import requests 
with open('ram.json') as json_file:
    data = json.load(json_file)
    print(data)

with open('shyam.json', 'w') as json_file1:
    user = {
            "name":'sachin',
            'age':23
            }
    json.dump(user,json_file1)

