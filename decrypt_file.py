import os
import sys
pth = f"{os.environ["CRYPTOGRAPHY"]}/shared_func"
sys.path.append(pth)
from blackMagic import *
import sys

# Lambda functions to get arguments or prompt the user
input_file_func = lambda: sys.argv[1] if len(sys.argv) > 1 else input("Enter input file path: ")
output_file_func = lambda: sys.argv[2] if len(sys.argv) > 2 else f"{os.path.splitext(input_file_func())[0]}_encrypted{os.path.splitext(input_file_func())[1]}"

# Get file names using lambda functions
input_file = input_file_func()
output_file = output_file_func()

# Perform encryption
decrypt_file(input_file, output_file)


