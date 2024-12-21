import sys
import os
pth = f"{os.environ["CRYPTOGRAPHY"]}/shared_func"
sys.path.append(pth)
from file_handler_class import *
from blackMagic import *
import json

obj = FileHandler()
data = obj.read_file()
decrypted_data = decrypt_json_fernet(data)
obj.write_file(decrypted_data)