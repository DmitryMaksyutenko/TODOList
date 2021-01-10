from django.db import connection

from Database.DatabaseFunctionsManager import FunctionManager


class ExistenceManager(FunctionManager):

    def __init__(self):
        self._sql_query = "SELECT does_list_exists(%s);"

    def exists(self, data):
        return self._execute_query(data.strip())

    def _execute_query(self, title):
        with connection.cursor() as cursor:
            cursor.execute(self._sql_query, (title,))
            result = cursor.fetchone()[0]
        return result

    def _get_title(self, data):
        pass

    def _get_tasks(self, data):
        pass
