from Database.DatabaseFunctionsManager import FunctionManager


class InsertManager(FunctionManager):
    """Manage list insertion in to database."""

    def __init__(self):
        self._sql_query = "CALL insert_list_with_tasks(%s, %s)"

    def insert(self, data):
        """Inserts data."""
        self._execute_query(data)
