import getpass

# Encryption function
def encrypt(password):
    return ''.join(chr(ord(char) + 1) for char in password)

# Decryption function
def decrypt(encrypted_password):
    return ''.join(chr(ord(char) - 1) for char in encrypted_password)

# Function to encrypt a password based on input string
def encrypt_password(input_str, password):
    return encrypt(input_str + password)

# Function to decrypt a password based on input string
def decrypt_password(encrypted_password, input_str):
    return decrypt(encrypted_password)[len(input_str):]

# Example usage
def main():
    password = "teste"
    input_str = getpass.getpass("Enter password to hide your message: ")

    encrypted_password = encrypt_password(input_str, password)
    decrypted_password = decrypt_password(encrypted_password, input_str)

    print("Original Password:", password)
    print("Encrypted Password:", encrypted_password)
    print("Decrypted Password:", decrypted_password)

if __name__ == "__main__":
    main()
