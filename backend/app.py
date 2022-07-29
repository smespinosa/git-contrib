import os
import falcon
import falcon.asgi

from dotenv import load_dotenv
from git_handler import GitHandler
from data_context import DataContext


load_dotenv()

PG_CONN = os.getenv("PG_CONN")

git_handler = GitHandler("D:\\git\\")

# db_connection = DataContext(PG_CONN)


app = falcon.asgi.App()
app.add_route("/", git_handler)
