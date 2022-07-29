import os
import falcon
import falcon.asgi

from dotenv import load_dotenv
from git_handler import GitHandler


load_dotenv()

PG_CONN = os.getenv("PG_CONN")

git_handler = GitHandler("D:\\git\\")


app = falcon.asgi.App()
app.add_route("/", git_handler)
