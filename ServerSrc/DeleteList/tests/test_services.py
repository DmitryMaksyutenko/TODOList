from django.test import TestCase

from DeleteList.services import DeleteManager
from LoadList.services import List
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


class DeleteListTestCase(TestCase):
    """Test list deletion."""

    def setUp(self):
        tst_db.set_up_test_database()
        tst_db.set_up_test_list(TEST_LIST_DATA)
        tst_db.set_up_test_tasks(TEST_TAKS_DATA)

    def test_delete_list(self):
        """Deletion list with tasks."""
        list_to_del = {"title": TEST_LIST_DATA[0][0]}

        mngr = DeleteManager()
        mngr.delete(list_to_del)

        exists = List(tst_db.TEST_LIST[0]).exists()

        self.assertFalse(exists)

    def test_list_not_exists(self):
        """Test if list for deletein doesn't exists."""
        list_to_del = {"title": "Fake list tittle."}

        mngr = DeleteManager()
        result = mngr.delete(list_to_del)

        self.assertFalse(result)
