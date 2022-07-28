import string
import typing
from git import Repo


class GitLogParse:
    
    def __init__(self, repo: string):
        self.repo = repo

    def parse(self):
        repo = Repo(self.repo)
        assert not repo.bare

        print(repo)
        resp = repo.log()

        return resp
