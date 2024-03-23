import sys
import json
import pandas as pd
import os
import sys

# Ensure the directory containing your module is in sys.path
pth = f"{os.environ["CRYPTOGRAPHY"]}/shared_func"
sys.path.append(pth)

from mysql_class import MySQL

db = MySQL()
print("------------------------")
#input: query, the default value for query is None
df = db.qry()
