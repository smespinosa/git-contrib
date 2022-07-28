import datetime

from git import Repo

class GitLogParse:
    repo: str

    def __init__(self, repo: str):
        self.repo = repo

    def parse(self):
        repo = Repo(self.repo)
        assert not repo.bare

        head = repo.head
        main_ref = head.reference
        log = main_ref.log()

        resp = {}

        for git_log in log:
            actor = str(git_log.actor)
            if actor not in resp.keys():
                resp[actor] = []

            fixed_date = datetime.datetime.fromtimestamp(git_log.time[0] - git_log.time[1]).isoformat()
            resp[actor].append(fixed_date)
        return resp
