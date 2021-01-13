import json

from django.db import connection


class FunctionManager:

    _sql_query = ""

    def _execute_query(self, data):
        title = self._get_title(data)
        tasks = self._get_tasks(data)
        with connection.cursor() as cursor:
            cursor.execute(self._sql_query, (title, tasks))

    def _get_title(self, data):
        """Retrieve title from json."""
        return data[0]["title"]

    def _get_tasks(self, data):
        """Retrieve tasks from json."""
        tasks = data[1]["tasks"].values()
        return json.dumps(list(tasks))
