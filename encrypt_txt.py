import os
import sys
pth = f"{os.environ["CRYPTOGRAPHY"]}/shared_func"
sys.path.append(pth)

from file_handler_class import *
from blackMagic import *
import sys
import json

obj = FileHandler()
data = obj.read_file()
encrypted_data = encrypt_str(data)
obj.write_file(encrypted_data)
