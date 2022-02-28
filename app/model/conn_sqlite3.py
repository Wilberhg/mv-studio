from contextlib import contextmanager
from typing import Union
import sqlite3
import sys
import os


class Database:

    def __init__(self, server: str, database: str) -> None:
        self.server = server
        self.database = database

    @contextmanager
    def _open_db_connection(self, db_pathfile: str = os.getcwd(), commit: bool = None) -> sqlite3.Cursor:
        connection = sqlite3.connect(db_pathfile)
        cursor = connection.cursor()
        try:
            yield cursor
        except sqlite3.DatabaseError as err:
            error, _ = err.args
            sys.stderr.write(error.message)
            cursor.execute('ROLLBACK')
            raise err
        else:
            if commit is True:
                cursor.execute("COMMIT")
            elif commit is False:
                cursor.execute('ROLLBACK')
        finally:
            cursor.close()
            connection.close()

    def do_select(self, queries: Union[str, list]) -> list:
        try:
            with self._open_db_connection() as cursor:
                if type(queries) == list:
                    for query in queries:
                        cursor.execute(query)
                else:
                    cursor.execute(queries)
                result = cursor.fetchall()
        except:
            result = []
        return result

    def do_insert_update(self, query: str, values: Union[str, list] = None) -> bool:
        try:
            with self._open_db_connection(commit=True) as cursor:
                if values:
                    cursor.executemany(query, values)
                else:
                    cursor.execute(query)
            return True
        except:
            return False

