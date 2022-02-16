import boto3

s3bk = boto3.client('s3')

########List objs in a bucket
objectdata = s3bk.list_objects(Bucket='demotechbucket')
#print(objectdata)

for i in objectdata['Contents']:
    print(i["Key"])

