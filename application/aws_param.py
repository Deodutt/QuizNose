import boto3

def get_ssm_param(param_name: str):
    """Returns SSM value given a parameter name"""
    ssm = boto3.client("ssm")  # selecting what service

    parameter = ssm.get_parameter(
        Name=param_name, WithDecryption=True
    )  # grabbing the paramaeter that has the name/prod/db/password
    return parameter["Value"]
