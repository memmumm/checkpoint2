from pprint import pprint

import requests

response = requests.get("https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json")
data = response.json()
pprint(data)
print(data['items'][0]['parameter'])

for d in sorted(data['items'], key=lambda x: x['parameter'], reverse=True):
    print(f'{d["parameter"]}')

    f = open('checkpoint.txt', 'w')
    print((f'{d["parameter"]}'), file=f)