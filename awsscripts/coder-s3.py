import requests
import boto3
from botocore import UNSIGNED
from botocore.client import Config

s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))

bukt='coderbytechallengesandbox'

objectlist = s3.list_objects(Bucket=bukt)
#print(objectlist)
for i in objectlist['Contents']:
    obj = i["Key"]
    print(obj)
    s3.download_file('coderbytechallengesandbox', obj, 'OBJECT')
    with open('OBJECT', 'r') as f:
        print(f.read())

