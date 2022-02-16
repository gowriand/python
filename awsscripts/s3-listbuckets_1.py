import boto3

s3bk = boto3.client('s3')
response = s3bk.list_buckets()



### Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(bucket["Name"])
