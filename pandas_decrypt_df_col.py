import os
import sys
pth = f"{os.environ["CRYPTOGRAPHY"]}/shared_func"
sys.path.append(pth)

import pandas as pd
from pandas_class import Pd
from blackMagic import *

eng = Pd()
df = eng.read_file()
df = decrypty_col(df)
eng.write_file(df)
print(df)
