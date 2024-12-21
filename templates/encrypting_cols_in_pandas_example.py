import os
import sys

repo_folder = os.environ['CRYPTOGRAPHY']
sys.path.append(f"{repo_folder}/shared_func")
from blackMagic import *

pth = f"{repo_folder}/dataset/mock_data.csv"
df = pd.read_csv(pth)
df['cpf_enc'] = df.cpf.apply(lambda x: encrypt_str(x))
df['cpf_dec'] = df.cpf_enc.apply(lambda x: decrypt_str(x))
df = df[["cpf_dec", "cpf_enc"]]
print(df.head())
