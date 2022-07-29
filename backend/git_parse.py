import datetime

from git import Repo

from data_context import db_context as db


class GitLogParse:
    repo: str
    repo_id: int

    def __init__(self, repo: str):
        self.repo = repo

    def parse(self):
        repo = Repo(self.repo)
        assert not repo.bare

        self.repo_id = db.create_or_select_repo(self.repo)

        commits = repo.iter_commits("--all")

        db.purge_contributions_by_repo_id(self.repo_id)

        for commit in commits:
            actor = commit.committer.email

            fixed_date = datetime.datetime.fromtimestamp(
                commit.committed_date
            ).strftime("%Y-%m-%d")

            db.insert_contribution(self.repo_id, actor, fixed_date)
