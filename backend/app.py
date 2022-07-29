import falcon
import falcon.asgi

from git_handler import GitHandler


git_handler = GitHandler("D:\\git\\")


app = falcon.asgi.App()
app.add_route("/", git_handler)
