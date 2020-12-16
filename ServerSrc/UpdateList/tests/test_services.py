from django.test import TestCase

from LoadList.services import List
from UpdateList.services import UpdateManager
import utils.tst_db_setup as tst_db


TEST_LIST_DATA = [
    (tst_db.TEST_LIST[0],),
    (tst_db.TEST_LIST[1],),
    (tst_db.TEST_LIST[2],)
]
TEST_TAKS_DATA = [
    (tst_db.TEST_TASKS[1]["context"],
     tst_db.TEST_TASKS[1]["condition"],
     2),
    (tst_db.TEST_TASKS[0]["context"],
     tst_db.TEST_TASKS[0]["condition"],
     2),
    (tst_db.TEST_TASKS[2]["context"],
     tst_db.TEST_TASKS[2]["condition"],
     1)
]

NEW_LIST = [
    {"title": tst_db.TEST_LIST[0]},
    {
        "tasks": {
            0: {
                "context": "new context 0",
                "condition": 0
            },
            1: {
                "context": "new context 1",
                "condition": 0
            },
            2: {
                "context": "new context 2",
                "condition": 0
            }
        }
    }
]


class UpdateListTestCase(TestCase):
    """Test list updating."""

    def setUp(self):
        tst_db.set_up_test_database()
        tst_db.set_up_test_list(TEST_LIST_DATA)
        tst_db.set_up_test_tasks(TEST_TAKS_DATA)

    def test_update_list(self):
        """Test updating an existing list."""
        mngr = UpdateManager()
        mngr.update(NEW_LIST)

        updated = List(tst_db.TEST_LIST[0]).get_as_list()

        self.assertEqual(NEW_LIST, updated)
