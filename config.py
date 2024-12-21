import os

path_boto3_cred = os.environ["AWS_TEMP_CRED"]
kms_key_alias = "default"
token_duration = 60*60*24
