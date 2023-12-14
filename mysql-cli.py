import sys
import json
import os
repo_folder = os.environ['CRYPTOGRAPHY']
sys.path.append(f"{repo_folder}/shared_func")
from mysql_class import MySQL

obj = MySQL()
host = obj.cred.get("host")
port = obj.cred.get("port")
user = obj.cred.get("user")
password = obj.cred.get("password")

cmd = f"""mysql -h "{host}" -P "{port}" -u "{user}" -p"{password}" """
print(
        f"""
            # Connect to MySQL and perform some operations
            🐬 Connecting to MySQL...
            👤 User: {user}
            🌐 Host: {host}
            🔌 Port: {port}
        """
    )


os.system(cmd)
