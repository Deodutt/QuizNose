import boto3

client = boto3.client('elb')

# session = boto3.Session(profile_name='default')

paginator = client.get_paginator('describe_load_balancers')


response_iterator = paginator.paginate(
    LoadBalancerNames=[
        'string',
    ],
    PaginationConfig={
        'MaxItems': 123,
        'PageSize': 123,
        'StartingToken': 'string'
    }
)

print(response_iterator)

# import boto3
# s = boto3.Session(profile_name="final")
# c = s.client("sts")
# c.get_caller_identity()