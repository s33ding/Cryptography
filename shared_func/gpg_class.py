import os

class GPG:
    def __init__(self, recipient_email):
        self.recipient_email = recipient_email

    def encrypt_file(self, input_file):
        # Encrypt the file
        command = f'gpg -e -r {self.recipient_email} {input_file}'
        print(command)
        os.system(command)

        # Delete the original file after encryption
        print("rmv:",input_file)
        os.remove(input_file)

    def decrypt_file(self, input_file_gpg):
        # Decrypt the file
        output_file = input_file_gpg.replace(".gpg","")
        command = f'gpg -d {input_file_gpg} > {output_file}'
        print(command)
        os.system(command)

        # Delete the encrypted file after decryption
        print("rmv:",input_file_gpg)
        os.remove(input_file_gpg)
