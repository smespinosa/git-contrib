from dotenv import load_dotenv
import psycopg
import os


class DataContext:
    __connection: psycopg.Connection

    def __init__(self):
        self.__get_connection()

    def __get_connection(self):
        load_dotenv()

        PG_CONN = os.getenv("PG_CONN")

        self.__connection = psycopg.connect(PG_CONN)

    def purge_contributions_by_repo_id(self, repo_id: int):
        self.__connection.execute(
            "DELETE FROM contributions WHERE repo_id = %s", (repo_id,)
        )
        self.__connection.commit()

    def get_repo_id_by_name(self, repo_name: str) -> int | None:
        result = self.__connection.execute(
            "SELECT id FROM repos WHERE name = %s", (repo_name,)
        ).fetchone()

        if result is not None:
            return result[0]

        return None

    def create_or_select_repo(self, repo_name: str):
        repo_id = self.get_repo_id_by_name(repo_name)

        if repo_id is None:
            self.__connection.execute("INSERT INTO repos (name) VALUES (%s)")
            self.__connection.commit()
            repo_id = self.get_repo_id_by_name(repo_name, (repo_name,))

        return repo_id

    def insert_contribution(self, repo_id: int, email: str, date: str):
        self.__connection.execute(
            "INSERT INTO contributions (repo_id, email, date) VALUES (%s, %s, %s)",
            (repo_id, email, date),
        )
        self.__connection.commit()

    def get_contributions_by_contributor(self, email: str, year: int) -> list:
        query = """
            SELECT
                date,
                count(date) as count
            FROM
                contributions
            WHERE
                date >= make_date(%s, 1, 1)
                AND date < date_trunc('year', make_date(%s, 1, 1) + interval '1 year')
                AND email = %s
            GROUP BY date
            ORDER BY date
            """
        result = self.__connection.execute(query, (year, year, email)).fetchall()

        return result


db_context = DataContext()
