import sqlite3
from functools import wraps

import mysql.connector



def open_close_connection(repository_method):
    @wraps(repository_method)
    def wrapper(self, *args, **kwargs):
        try:
            self.conn = mysql.connector.connect(
                host="127.0.0.1",
                port="3306",
                user='root',
                password="mislnipr",
                auth_plugin='mysql_native_password'
            )
            # sqlite3.connect(BaseRepository.DATABASE_URL, uri=True)
            result = repository_method(self, *args, **kwargs)
        except Exception as e:
            print(e)
            return e
        finally:
            if self.conn.is_connected():
                self.conn.cursor().close()
                self.conn.close()
        return result
    return wrapper
