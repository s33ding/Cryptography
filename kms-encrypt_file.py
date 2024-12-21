from shared_func.kms_func import *
import sys

# Define function for input path
input_path_func = lambda: sys.argv[1] if len(sys.argv) > 1 else input("file_path: ")

input_path = input_path_func()

if len(sys.argv) >1:
    output_path_func = lambda : sys.argv[2] if len(sys.argv) > 2 else sys.argv[1]
    output_path = output_path_func()
else:
    output_path = input("output_path:")


encrypt_file(
        input_path, 
        output_path
        )
