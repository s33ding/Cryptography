import getpass

# Password encryption lambda function
encrypt_password = lambda password, input_str: encrypt(input_str + password)

# Password decryption lambda function
decrypt_password = lambda encrypted_password, input_str: decrypt(encrypted_password)[len(input_str):]

# Encryption function
encrypt = lambda password: ''.join(chr(ord(char) + 1) for char in password)

# Decryption function
decrypt = lambda encrypted_password: ''.join(chr(ord(char) - 1) for char in encrypted_password)

# Example usage
password = "teste"
input_str = getpass.getpass("Enter password to hide your message: ")

encrypted_password = encrypt_password(password, input_str)
decrypted_password = decrypt_password(encrypted_password, input_str)

print("Original Password:", password)
print("Encrypted Password:", encrypted_password)
print("Decrypted Password:", decrypted_password)

key = decrypt("encrypted_key")
password = decrypt("encrypted_password")
