from django.db import connection


class ExistenceManager:

    def __init__(self):
        self._sql_query = "SELECT does_list_exists(%s);"

    def exists(self, data):
        return self._execute_query(data.strip())

    def _execute_query(self, title):
        with connection.cursor() as cursor:
            cursor.execute(self._sql_query, (title,))
            result = cursor.fetchone()[0]
        return result
