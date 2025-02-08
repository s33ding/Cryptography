import boto3
import json
import base64





# AWS KMS settings
kms_key_alias = "default"
path_boto3_cred = "~/.aws/.tmp.json"

token_duration = 60 * 60 * 24  # 24 hours
key_file =  None
binary_key =  None
secret_name = "s33ding"
key_name_in_secret_manager = "binary_key"
