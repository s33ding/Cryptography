import pandas as pd
from shared_func.pandas_class import Pd
from shared_func.blackMagic import *

eng = Pd()
df = eng.read_file()
df = encrypty_col(df)
eng.write_file(df)
print(df)
