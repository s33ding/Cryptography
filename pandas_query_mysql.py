import sys
import json
import pandas as pd
from shared_func.mysql_class import MySQL

db = MySQL()
df = db.qry()
print(df)
