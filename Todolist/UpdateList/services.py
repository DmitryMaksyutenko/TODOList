from Database.DatabaseFunctionsManager import FunctionManager


class UpdateManager(FunctionManager):
    """Class for updating the list."""

    def __init__(self):
        self._sql_query = "CALL update_list_with_tasks(%s, %s)"

    def update(self, data):
        """Updates data."""
        self._execute_query(data)
