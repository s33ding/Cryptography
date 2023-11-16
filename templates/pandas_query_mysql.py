import sys
import json
import pandas as pd
import pymysql
import mysql.connector
import os
from shared_func.mysql_class import MySQL

db = MySQL()
df = db.qry()
print(df)
