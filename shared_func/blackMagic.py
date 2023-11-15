from getpass import getpass
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from cryptography.fernet import Fernet
import pandas as pd
import numpy as np
import json
import os


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

def encrypty_col(df, lst_cols=[]):
    lst_cols = []
    if lst_cols == []:
        col = input("COLUMN_NAME:")
        lst_cols.append(col)
    for x in lst_cols:
        df[x]= df[x].apply(lambda x: encrypt_str(x))
    return df

def decrypty_col(df, lst_cols=[]):
    lst_cols = []
    if lst_cols == []:
        col = input("COLUMN_NAME:")
        lst_cols.append(col)
    for x in lst_cols:
        df[x]= df[x].apply(lambda x: decrypt_str(x))
    return df, lst_cols  
