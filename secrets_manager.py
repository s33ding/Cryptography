from shared_func.boto3_class import * 
import os
import sys

obj = Boto()
secret_name = obj.get_input()
secret = obj.get_secret(secret_name)
print(secret)
