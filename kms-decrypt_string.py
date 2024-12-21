from shared_func.kms_func import *
from shared_func.argv_parser import *

secret = "testing KMS"
print("secret:", secret)
res = encrypt_string(secret)
encrypted_secret = res

print("encrypted secret:", encrypted_secret)

res = decrypt_string(encrypted_secret)

print("secret decrypted:", res)

