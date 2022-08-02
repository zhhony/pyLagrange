import conn
import json
import io


class Conf():
    def __init__(self, file: io) -> None:
        self.file = file

    def getTablesAll(self, database: str):
        with conn(self.file) as cur:
            sql = f"""select * form {database}"""
            cur.execute(sql)
            return cur.fetchall()

    def load(self):
        ...
