import boto3

s3buck = boto3.resource('s3')
buck_name = 'setting-scripts'


# Print out bucket names
for bucket in s3buck.buckets.all():
    print(bucket.name)
