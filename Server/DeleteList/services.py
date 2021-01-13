from django.db import connection

from Database.DatabaseFunctionsManager import FunctionManager


class DeleteManager(FunctionManager):
    """Class for list deletion."""

    def __init__(self):
        self._sql_query = "CALL delete_list(%s);"

    def delete(self, data):
        """Delete the list with corresponding title."""
        self._execute_query(data)

    def _execute_query(self, data):
        title = self._get_title(data)
        with connection.cursor() as cursor:
            cursor.execute(self._sql_query, (title,))

    def _get_title(self, data):
        return data["title"]

    def _get_tasks(self, data):
        pass
