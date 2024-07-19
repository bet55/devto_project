import sqlite3

from exeptions.db import DBException


class DBToolkit:
    DB_PATH = "identifier.sqlite"

    def __init__(self):
        try:
            self.connection = sqlite3.connect(self.DB_PATH)
        except sqlite3.Error as e:
            self.connection.close()
            raise DBException(e)

        self.cursor = self.connection.cursor()

    def _execute(self, sql: str, data: list) -> list:
        try:
            self.cursor.execute(sql, data)
            self.connection.commit()
        except sqlite3.Error as e:
            self.connection.close()
            raise DBException(e)

        result = self.cursor.fetchall()
        if not result:
            self.connection.close()
            raise DBException("Database is empty")

        self.cursor.close()
        self.connection.close()

        return result
