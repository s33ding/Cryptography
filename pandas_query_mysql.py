import sys
import json
import pandas as pd
import os
import sys

# Ensure the directory containing your module is in sys.path
pth = f"{os.environ["CRYPTOGRAPHY"]}/shared_func"
sys.path.append(pth)

from mysql_class import MySQL
from boto3_class import Boto

db = MySQL()
b3 = Boto()
db.cred = b3.get_secret(os.environ["MYSQL_READ_SECRET"])
print("------------------------")
#input: query, the default value for query is None
df = db.qry()
