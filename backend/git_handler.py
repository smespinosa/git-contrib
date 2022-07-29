import falcon
import json
import os

from git_parse import GitLogParse


class GitHandler:
    os_path: str

    def __init__(self, os_path: str):
        self.os_path = os_path

    async def on_get(self, req: falcon.Request, resp: falcon.Response):
        dirs = [f.path for f in os.scandir(self.os_path) if f.is_dir()]

        git_results = []
        for maybe_git_dir in dirs:
            try:
                git_log_parse = GitLogParse(maybe_git_dir)
                result = git_log_parse.parse()

                git_results.append(result)
            except Exception as e:
                pass

        resp.text = json.dumps(git_results)
        resp.status = falcon.HTTP_200
