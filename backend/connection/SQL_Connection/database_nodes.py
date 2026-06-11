import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dotenv import load_dotenv
from os import getenv

load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")
user = os.getenv("USER")
database = os.getenv("DATABASE")
password = os.getenv("PASSWORD")

nodes = [
    {
        "type": "Main Database",
        "host": host,
        "port": port,
        "user": user,
        "database": database,
        "password": password
    }
]

