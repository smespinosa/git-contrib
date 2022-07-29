import os
import falcon
import falcon.asgi

import json

from git_parse import GitLogParse

class GitHandler:
    def __init__(self, git_path: str):
        self.git_path = git_path

    async def on_get(self, req, resp):
        dirs =  [ f.path for f in os.scandir(self.git_path) if f.is_dir() ]
        
        git_results = [];
        for maybe_git_dir in dirs:
            try:
                git_log_parse = GitLogParse(maybe_git_dir)
                result = git_log_parse.parse()

                git_results.append(result)
            except Exception as e:
                pass

        resp.text = json.dumps(git_results)
        resp.status = falcon.HTTP_200

app = falcon.asgi.App()

git_handler = GitHandler("D:\\git\\")

app.add_route('/', git_handler)