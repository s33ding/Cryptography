sys.append(f"{os.environ["CRYPTOGRAFY"]}/shared_func")
from blackMagic import *

df = pd.read_csv('dataset/MOCK_DATA.csv')
df['cpf_enc'] = df.cpf.apply(lambda x: encrypt_str(x))
df['cpf_dec'] = df.cpf_enc.apply(lambda x: decrypt_str(x))

df.head()
