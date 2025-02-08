from cryptography.fernet import Fernet
import pandas as pd
import numpy as np
import json
import sys
import os
import boto3
import json
import base64

# Get the parent directory of 'shared_func'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now you can import config.py
import config

key_file = config.key_file
binary_key = config.binary_key
secret_name = config.secret_name
key_name = config.key_name_in_secret_manager

def get_binary_key_in_secret_manager(secret_name,key_name):
    session = boto3.Session()
    secrets_manager = session.client("secretsmanager")
    secret_value = secrets_manager.get_secret_value(SecretId=secret_name)
    return json.loads(secret_value["SecretString"])[key_name]

def get_fernet_key(key_file=key_file):
    if binary_key is not None:
        return binary_key
    elif key_file is not None:
       with open(key_file,'rb') as f:
           key = f.read()
       return key
    else:
       return get_binary_key_in_secret_manager(secret_name,key_name)


def encrypt_str(text = '', key_file=key_file):
    if text==None:
        return None
    text = str(text)
    key = get_fernet_key(key_file=key_file)
    fernet = Fernet(key)
    encMessage = fernet.encrypt(text.encode())
    return encMessage.decode()

def decrypt_str(text, key_file=key_file):
    key = get_fernet_key(key_file=key_file)
    fernet = Fernet(key)
    encMessage = text.encode()
    decMessage = fernet.decrypt(encMessage).decode()
    return decMessage

def encrypt_json_fernet(data,key_file=key_file):
    print("encrypting!")
    for key,value in data.items():
        data[key] = encrypt_str(text = value, key_file=key_file)
    return data
    
def decrypt_json_fernet(data,key_file=key_file):
    print("decrypting!")
    for key,value in data.items():
        data[key] = decrypt_str(text = value, key_file=key_file)
    return data


def get_col(col):
    if col is not None:
        return col
    else:
        if len(sys.argv) > 2:
            return sys.argv[2]
        else:
            return input("col name:")

def encrypty_col(df, col=None):
    col = get_col(col)
    df[col]= df[col].apply(lambda x: encrypt_str(x))
    return df

def decrypty_col(df, col = None): 
    col = get_col(col)
    df[col]= df[col].apply(lambda x: decrypt_str(x))
    return df

# Function to encrypt a file
def encrypt_file(input_file, output_file=None, key_file="secret.key"):
    key = get_fernet_key(key_file)
    fernet = Fernet(key)

    with open(input_file, "rb") as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(output_file, "wb") as enc_file:
        enc_file.write(encrypted_data)

    print(f"File '{input_file}' encrypted successfully as '{output_file}'")

# Function to decrypt a file
def decrypt_file(input_file, output_file=None, key_file="secret.key"):
    key = get_fernet_key(key_file)
    fernet = Fernet(key)

    with open(input_file, "rb") as enc_file:
        encrypted_data = enc_file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    if output_file is None:
        if input_file.endswith(".enc"):
            output_file = input_file[:-4]  # Remove .enc extension
        else:
            output_file = input_file + ".dec"

    with open(output_file, "wb") as dec_file:
        dec_file.write(decrypted_data)

    print(f"File '{input_file}' decrypted successfully as '{output_file}'")
