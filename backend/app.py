import falcon
import falcon.asgi

from contrib_handler import ContribHandler
from git_handler import GitHandler


git_handler = GitHandler("D:\\git\\")
contrib_handler = ContribHandler()

app = falcon.asgi.App()
app.add_route("/parse", git_handler)
app.add_route("/query", contrib_handler)
