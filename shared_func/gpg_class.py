import os
import sys

class GPG:
    def __init__(self, file_name=None, folder_name=None):

        self.recipient_email = os.environ.get("GPG_RECIPIENT_EMAIL")
        self.file_name = file_name

        if self.recipient_email is None:
            print("GPG_RECIPIENT_EMAIL not found in environment variables.")
            return False 
        else:
            self.get_file()
            if self.folder_name is not None:
                print("ENCRYPTING FILES IN A FOLDER:")
                for fl in os.listdir():
                    print("processing:", fl)
                    self.process(fl)
            else:
                file_name = self.file_name
                print("processing:", file_name)
                self.process(file_name)


    def get_file(self): 
        if self.file_name is None:
            if len(sys.argv) > 1:
                self.file_name = sys.argv[1]
                if self.file_name == ".":
                    self.folder_name = os.getcwd()
            else:
                self.file_name = input("input_file:",)
                self.folder_name = None



    def encrypt_file(self, file_name):
        self.file_name = file_name
        self.output_file = f"{self.file_name}.gpg"

        # Encrypt the file
        command = f'gpg -e -r {self.recipient_email} {self.file_name}'
        print("cmd:",command)
        os.system(command)

        # Delete the original file after encryption
        print("rmv:",self.file_name)
        os.remove(self.file_name)

    def decrypt_file(self, file_name):
        self.file_name = file_name
        self.output_file = file_name.replace(".gpg","")

        # Decrypt the file
        command = f'gpg -d {self.file_name} > {self.output_file}'
        print("cmd:",command)
        os.system(command)

        # Delete the encrypted file after decryption
        print("rmv:",self.file_name)
        os.remove(self.file_name)

    def process(self, file_name):
        if file_name.endswith(".gpg"):
            # Decrypt a file and delete the original
            self.decrypt_file(file_name)
        else:
            # Encrypt a file and delete the original
            self.encrypt_file(file_name)

