import sys
import os

repo_folder = os.environ['CRYPTOGRAPHY']
sys.path.append(f"{repo_folder}")

import json
import pandas as pd
from shared_func.mysql_class import MySQL

db = MySQL()
df = db.qry()
print(df)
