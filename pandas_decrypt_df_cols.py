import pandas as pd
import sys
from shared_func.pandas_class import Pd
from shared_func.blackMagic import *

eng = Pd()
df = eng.read_file()
df = decrypty_col(df)
eng.write_file(df)
print(df)
