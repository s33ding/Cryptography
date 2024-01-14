from cryptography.fernet import Fernet
import pandas as pd
import numpy as np
import json
import os
import sys


key_file = os.environ.get("BLACK_KEY")

def gen_fernet_key(key_file='fernet.bin'):
    key = Fernet.generate_key()
    with open(key_file,'wb') as f:
        f.write(key) 

def get_fernet_key(key_file=key_file):
    with open(key_file,'rb') as f:
        key = f.read()
    return key

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
