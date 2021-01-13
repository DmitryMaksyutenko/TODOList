from django.test import TestCase
from django.db import connection

from CreateList.services import InsertManager
from LoadList.services import List
import utils.tst_db_setup as tst_db


class InsertManagerTestCase(TestCase):
    """Test data insertion."""

    def setUp(self):
        with connection.cursor() as cursor:
            cursor.execute(tst_db.SQL_DB_SETUP)
            cursor.execute(tst_db.SQL_INSERT_FUNCS)

    def test_insert_list_with_task(self):
        """Insert list with one task."""
        InsertManager().insert(tst_db.TEST_LIST_WITH_TASK)
        lst = List(tst_db.TEST_LIST_WITH_TASK[0]["title"])

        self.assertEqual(tst_db.TEST_LIST_WITH_TASK, lst.get_as_list())

    def test_insert_list_with_tasks(self):
        """Insert list with tasks."""
        InsertManager().insert(tst_db.TEST_LIST_WITH_TASKS)
        lst = List(tst_db.TEST_LIST_WITH_TASKS[0]["title"])

        self.assertEqual(tst_db.TEST_LIST_WITH_TASKS, lst.get_as_list())
