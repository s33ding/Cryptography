import sys
import json
import pandas as pd
import pymysql
import mysql.connector
import os
from shared_func.mysql_class import MySQL
from shared_func.blackMagic import *
db = MySQL()
df = db.qry("select id from tisaude_app.agendamentos limit 1;")
print(df)
