from shared_func.file_handler_class import *
from shared_func.blackMagic import *
import sys
import json

obj = FileHandler()
data = obj.read_file()
decrypted_data = decrypt_json_fernet(data)
obj.write_file(decrypted_data)
