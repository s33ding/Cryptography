from shared_func.file_handler_class import *
from shared_func.blackMagic import *
import sys
import json

obj = FileHandler()
data = obj.read_file()
encrypted_data = encrypt_json_fernet(data)
obj.write_file(encrypted_data)
