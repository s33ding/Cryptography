import sys
import json
import os
from shared_func.mysql_class import MySQL

obj = MySQL()
host = obj.cred.get("host")
port = obj.cred.get("port")
user = obj.cred.get("user")
password = obj.cred.get("password")

print(
        f"""
            # Connect to MySQL and perform some operations
            🐬 Connecting to MySQL...
            👤 User: {user}
            🌐 Host: {host}
            🔌 Port: {port}
        """
    )

cmd = f"""mysql -h "{host}" -P "{port}" -u "{user}" -p"{password}" """
os.system(cmd)
