import pandas as pd
import os
import json
import mysql.connector
import sys
repo_folder = os.environ['CRYPTOGRAPHY']
sys.path.append(f"{repo_folder}/shared_func")
from file_handler_class import *
from blackMagic import *
import boto3  

def get_secret(secret_name):
        client = boto3.client('secretsmanager')
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        dct = json.loads(get_secret_value_response['SecretString'])
        return dct

class MySQL:
    def __init__(self, root_user=False):
        self.root_user = root_user
        cred = self.get_mysql_cred()
        self.cred = cred

    def get_mysql_cred(self, secret_manager=os.environ["BD_SECRET"]):
        if secret_manager is not None:
            return get_secret(secret_manager)
        else:
            if self.root_user:
                environ_name = "MYSQL_MASTER_CRED"
                if environ_name in os.environ:
                     credential_pth = os.environ[environ_name]
            else:
                environ_name = "MYSQL_CRED"
                if "MYSQL_CRED" in os.environ:
                     credential_pth = os.environ[environ_name]

            obj = FileHandler(credential_pth)
            data = obj.read_file()
            key_file = os.environ.get("BLACK_KEY")
            cred = decrypt_json_fernet(data, key_file)
            return cred


    def connect_to_mysql(self):
        try:
            db_cred = self.cred
            print("------------------------------")
            print("login as:", db_cred.get("user"))
            print("------------------------------")
            connection = mysql.connector.connect(
                host=db_cred.get('host'),  
                user=db_cred.get('user'),    
                password=db_cred.get('password') 
            )

            if connection.is_connected():
                print("Connected to the database!")
                return connection
            else:
                print("Connection failed.")
                return None

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def execute_sql_queries(self, queries):
        connection = self.connect_to_mysql()
        cursor = connection.cursor()
        len_lst = len(queries)
        print("len_lst_stmt:",len_lst)
        try:
            cursor.execute("START TRANSACTION")
            for i,query in enumerate(queries):
                print(f"====={i}/{len_lst}")
                print(query)
                query = query.replace("\n"," ")
                query = query.replace("  "," ")
                cursor.execute(query)
            cursor.execute("COMMIT")
            print(f"Successfully executed {len(queries)} SQL queries.")
        except Exception as e:
            print("Error executing SQL queries:", e)
            cursor.execute("ROLLBACK")
            raise e
        finally:
            cursor.close()
            connection.close()

    exec_stmt = execute_sql_queries

    def generate_insert_statements(df, table_name):
        engine = self.connect_to_mysql(db_cred)
        query = f"DESCRIBE {table_name}"
        sch = pd.read_sql(query, engine)
        sch = sch[["Field", "Type"]]
        sch = sch.to_dict('records')
        sch = {row['Field']: row['Type'].split('(')[0] for row in sch}
        insert_statements = []
        for index, row in df.iterrows():
            values = []
            for col in df.columns:
                if pd.isna(row[col]):
                    values.append('NULL')
                else:
                    if sch[col] in ['int', 'bigint', 'decimal', 'float', 'double']:
                        values.append(str(row[col]))
                    elif sch[col] in ['varchar', 'char', 'text', 'mediumtext', 'longtext']:
                        escaped_value = escape_value(row[col])
                        values.append("'{}'".format(escaped_value))
                    elif sch[col] in ['date', 'datetime', 'timestamp']:
                        values.append("'{}'".format(str(row[col])))
                    else:
                        escaped_value = escape_value(row[col])
                        values.append("'{}'".format(escaped_value))
            values_str = ','.join(values)
            insert_statements.append(f'INSERT INTO {table_name} ({", ".join(df.columns)}) VALUES ({values_str})')
        return insert_statements

    def qry(self, query=None):
        try:
            if query is None:
                query = input("QUERY: ")
                # Split the input into lines
                lines = query.split('\n')

                # Remove any empty lines from the input
                lines = [line.strip() for line in lines if line.strip()]

                # Join the non-empty lines into a single string
                query = '\n'.join(lines)

                print("------------------------------")
                print("stmt:")
                print(query)
            else:
                print("stmt:")
                print(query)
            engine_ms = self.connect_to_mysql()
            df = pd.read_sql(query, engine_ms)
            print("------------------------------")
            print("df:")
            print(df)
            print("------------------------------")
            return df
        except mysql.connector.Error as e:
            return f"Error connecting to MySQL: {e}"

