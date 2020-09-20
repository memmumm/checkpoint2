from pprint import pprint
import requests
import logging
import boto3
from botocore.exceptions import ClientError

response = requests.get("https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json")
data = response.json()
pprint(data)
print(data['items'][0]['parameter'])

for d in sorted(data['items'], key=lambda x: x['parameter'], reverse=True):
    print(f'{d["parameter"]}')

    f = open('checkpoint.txt', 'a')
    print((f'{d["parameter"]}'), file=f)

def upload_file(file_name, bucket, object_name=None):

    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

print(upload_file('C:\\Users\\Mervi\\PycharmProjects\\checkpoint2UUSI\\vko2\\tehtava1.py', 'mervi-checkpoint2', 'tehtava1.py'))