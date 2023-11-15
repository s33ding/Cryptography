import pandas as pd
import sys
from shared_func.pandas_class import Pd
from shared_func.blackMagic import *


def encrypty_col(df, lst_cols=[]):
    lst_cols = []
    if lst_cols == []:
        col = input("COLUMN_NAME:")
        lst_cols.append(col)
    for x in lst_cols:
        df[x]= df[x].apply(lambda x: encrypt_str(x))
    return df  

def decrypty_col(df, lst_cols=[]):
    lst_cols = []
    if lst_cols == []:
        col = input("COL:")
        lst_cols.append(col)
    for x in lst_cols:
        df[x]= df[x].apply(lambda x: decrypt_str(x))
    return df

def save(df,fl_nm):
    df.to_csv(fl_nm, index=False)

try:
    fl_nm=sys.argv[1] 
except:
    fl_nm=input("FILE: ")

eng = Pd()
df = eng.read_file()
df = decrypty_col(df)
eng.write_file(df)
print(df)
