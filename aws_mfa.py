import os
import json
import subprocess
import boto3
from shared_func.file_handler_class import *
from shared_func.blackMagic import *

def select_aws_key():
    aws_key_main = os.environ.get("AWS_KEY_MAIN")
    aws_key_2 = os.environ.get("AWS_KEY_2")

    # Prompt user to select AWS key
    print("☁️  Select an AWS key:")
    print("  0) Work AWS key")
    print("  1) Personal AWS key")
    aws_key_choice = input("> ")

    if aws_key_choice == "0":
        return aws_key_main
    elif aws_key_choice == "1":
        return aws_key_2
    else:
        print("Invalid choice. Exiting.")
        exit(1)

def read_cred(aws_key_path):
    print("aws_key_path:",aws_key_path)
    obj = FileHandler(aws_key_path)
    data = obj.read_file()
    decrypted_data = decrypt_json_fernet(data)
    print("decrypted!")

    id_val = decrypted_data.get('id')
    secret_val = decrypted_data.get('secret')
    arn_val = decrypted_data.get('arn')
    print("id:",id_val)

    return {
        'id': id_val,
        'secret': secret_val,
        'arn': arn_val
    }

def get_temporary_credentials(aws_cred):
    try:
        print("requesting!")
        sts_client = boto3.client(
            'sts',
            aws_access_key_id=aws_cred["id"],
            aws_secret_access_key=aws_cred["secret"],
        )

        aws_token = input('☁️  TOKEN: ')

        response = sts_client.get_session_token(
            DurationSeconds=30000,
            SerialNumber=aws_cred['arn'],
            TokenCode=aws_token
        )

        return {
            "id": response['Credentials']['AccessKeyId'],
            "secret": response['Credentials']['SecretAccessKey'],
            "token": response['Credentials']['SessionToken']
        }

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def print_fun_message():
    print("Access granted.")
    print("May the Python be with you! 🚀👨💻🔥")

aws_key_path = select_aws_key()
aws_cred = read_cred(aws_key_path)
aws_tmp_cred = get_temporary_credentials(aws_cred)

# Write temporary credentials JSON to file
temp_credentials_pth = os.environ.get("AWS_TEMP_CRED")

with open(temp_credentials_pth, 'w') as temp_cred_file:
    json.dump(aws_tmp_cred, temp_cred_file)

# Remove existing credentials from file using os.system
#export AWS_CRED="$USR_HOME/.aws/credentials"
credentials_file = os.environ["AWS_CRED"]
os.system(f'echo "" > {credentials_file}')

# Rewrite AWS default credentials file with new values
with open(credentials_file, 'a') as cred_file:
    cred_file.write("[default]\n")
    cred_file.write(f"aws_access_key_id = {aws_tmp_cred['id']}\n")
    cred_file.write(f"aws_secret_access_key = {aws_tmp_cred['secret']}\n")
    cred_file.write(f"aws_session_token = {aws_tmp_cred['token']}\n")

if temporary_credentials:
    print_fun_message()
    #testing
    subprocess.run(["aws", "s3", "ls"])
else:
    print("Failed to obtain temporary credentials.")