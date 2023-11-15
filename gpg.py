from shared_func.gpg_class import * 
import os
import sys

# Retrieve recipient_email from the GPG_RECIPIENT_EMAIL environment variable
recipient_email = os.environ.get("GPG_RECIPIENT_EMAIL")
gpg_handler = GPG(recipient_email)

if recipient_email is None:
    print("GPG_RECIPIENT_EMAIL not found in environment variables.")

if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = input("input_file:",)

if input_file.endswith(".gpg"):
    # Decrypt a file and delete the original
    input_file_gpg = input_file
    gpg_handler.decrypt_file(input_file_gpg)

else:
    # Encrypt a file and delete the original
    gpg_handler = GPG(recipient_email)
    gpg_handler.encrypt_file(input_file)
