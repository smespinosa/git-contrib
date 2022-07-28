import falcon
import falcon.asgi

import json

from git_parse import GitLogParse

class GitHandler:
    async def on_get(self, req, resp):
        git_log_parse = GitLogParse("D:\\git\git-contrib\git-contrib.git")
        result = git_log_parse.parse()

        resp.text = json.dumps(result)
        resp.status = falcon.HTTP_200

app = falcon.asgi.App()

# Resources are represented by long-lived class instances
git_handler = GitHandler()

# things will handle all requests to the '/things' URL path
app.add_route('/', git_handler)