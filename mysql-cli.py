import sys
import json
import os
from shared_func.mysql_class import MySQL
from shared_func.boto3_class import Boto

b3 = Boto()
obj = MySQL()

if len(sys.argv) > 1:
    if sys.argv[1] == "master":
        secret = os.environ.get("MYSQL_MASTER_SECRET")
        obj.cred  = b3.get_secret(secret)

    if sys.argv[1] == "master2":
        secret = os.environ.get("MYSQL_MASTER_SECRET2")
        obj.cred  = b3.get_secret(secret)
else:
    secret = os.environ.get("MYSQL_READ_SECRET")
    obj.cred  = b3.get_secret(secret)

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
