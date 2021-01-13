from django.test import (TestCase)

from LoadList.services import (ListsSet,
                               List)
import utils.tst_db_setup as tst_db

 
TEST_LIST_DATA = [
    (tst_db.TEST_LIST[0],),
    (tst_db.TEST_LIST[1],),
    (tst_db.TEST_LIST[2],)
]
TEST_TAKS_DATA = [
    (tst_db.TEST_TASKS[1]["content"],
     tst_db.TEST_TASKS[1]["condition"],
     2),
    (tst_db.TEST_TASKS[0]["content"],
     tst_db.TEST_TASKS[0]["condition"],
     2),
    (tst_db.TEST_TASKS[2]["content"],
     tst_db.TEST_TASKS[2]["condition"],
     1)
]

LISTSET_FROM_DB = [
    {"title": tst_db.TEST_LIST[0]},
    {"title": tst_db.TEST_LIST[1]},
    {"title": tst_db.TEST_LIST[2]}
]


class ListsTestCase(TestCase):
    """Buiseness logic of Lists testing."""
    def setUp(self):
        tst_db.set_up_test_database()
        tst_db.set_up_test_list(TEST_LIST_DATA)
        tst_db.set_up_test_tasks(TEST_TAKS_DATA)

    def test_get_lists_from_db(self):
        """Test lists retrieving."""
        lists = ListsSet()

        lists_number = lists.count()

        self.assertNotEqual(lists_number, 0)
        self.assertEqual(lists_number, len(tst_db.TEST_LIST))

    def test_get_as_python_list(self):
        """Test list returning."""
        lists = ListsSet()

        as_list = lists.get_as_list()

        self.assertIsInstance(as_list, list)
        self.assertListEqual(as_list, LISTSET_FROM_DB)


class ListWithTasksTestCase(TestCase):
    """Buiseness logic of ListWithTasks testing."""

    def setUp(self):
        tst_db.set_up_test_database()
        tst_db.set_up_test_list(TEST_LIST_DATA)
        tst_db.set_up_test_tasks(TEST_TAKS_DATA)

    def tets_does_list_exists(self):
        """Test list existings."""
        lst_exist = List(tst_db.TEST_LIST[0])
        lst_not_exist = List("Some title.")

        res_1 = lst_exist.exists()
        res_2 = lst_not_exist.exists()

        self.assertTrue(res_1)
        self.assertFalse(res_2)

    def test_get_list_with_tasks_as_python_list(self):
        """Test returning the list with tasks as Python list."""
        lst_with_tsks = List(tst_db.TEST_LIST[1])
        lst_with_tsk = List(tst_db.TEST_LIST[0])

        lst_1 = lst_with_tsks.get_as_list()
        lst_2 = lst_with_tsk.get_as_list()

        self.assertIsInstance(lst_1, list)
        self.assertEqual(lst_1, tst_db.TEST_LIST_WITH_TASKS)
        self.assertIsInstance(lst_2, list)
        self.assertEqual(lst_2, tst_db.TEST_LIST_WITH_TASK)
