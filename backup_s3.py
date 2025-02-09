import os

def execute_command(cmd):
    """Executes a shell command and prints the command."""
    print(f"Running command: {cmd}")
    os.system(cmd)

def zip_and_encrypt_fd(fd):
    """Handles zipping, encryption, cleanup, and uploading of files."""
    # Zip the directory
    execute_command(f"zip /tmp/{fd}.zip /home/roberto/{fd} -r")

    # Encrypt the zip file
    execute_command(f"python3 /home/roberto/Github/cryptography/encrypt_file.py /tmp/{fd}.zip /tmp/{fd}.zip.encrypted")

    # Remove the original zip file
    execute_command(f"rm /tmp/{fd}.zip")

    # Upload the encrypted file to S3
    execute_command(f"aws s3 cp /tmp/{fd}.zip.encrypted s3://s33ding-bck/")

    # Remove the encrypted zip file
    execute_command(f"rm /tmp/{fd}.zip.encrypted")

def process_files():
    """Process each directory/file from the list."""
    lst_fd = [
        "Documents", "Bitbucket", "Github", "Teste", "Pictures", 
        "Pictures", ".vim", "Videos"
    ]

    for fd in lst_fd:
        zip_and_encrypt_fd(fd)

    lst_fl = ["~/.bashrc"]
    for fl in lst_fl:
        execute_command(f"python3 /home/roberto/Github/cryptography/encrypt_file.py {fl} {fl}.encrypted")
        execute_command(f"aws s3 cp {fl}.encrypted s3://s33ding-bck/")

    execute_command(f"aws s3 sync /home/roberto/Pictures/wallpapers s3://s33ding-wallpapers/ --exclude '.git/*'")
    execute_command(f"aws s3 sync /home/roberto/Github/Obsidian s3://s33ding-obsidian/ --exclude '.git/*'")


process_files()

