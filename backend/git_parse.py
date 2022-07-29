import datetime

from git import Repo


class GitLogParse:
    repo: str

    def __init__(self, repo: str):
        self.repo = repo

    def parse(self):
        repo = Repo(self.repo)
        assert not repo.bare

        commits = repo.iter_commits("--all")

        resp = {
            "repo": repo.git_dir,
            "commits": {},
        }

        for commit in commits:
            actor = commit.committer.email
            if actor not in resp["commits"].keys():
                resp["commits"][actor] = []

            fixed_date = datetime.datetime.fromtimestamp(
                commit.committed_date
            ).isoformat()
            resp["commits"][actor].append(fixed_date)
        return resp
