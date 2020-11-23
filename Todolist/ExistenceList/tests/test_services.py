from django.test import TestCase

import utils.tst_db_setup as tst_db
from ExistenceList.services import ExistenceManager


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


class ExistanceManagerTestCase(TestCase):

    def setUp(self):
        tst_db.set_up_test_database()
        tst_db.set_up_test_list(TEST_LIST_DATA)
        tst_db.set_up_test_tasks(TEST_TAKS_DATA)

    def test_list_existence(self):
        mngr = ExistenceManager()
        res_1 = mngr.exists({"title": TEST_LIST_DATA[0][0]})
        res_2 = mngr.exists({"title": "No title"})

        self.assertTrue(res_1)
        self.assertFalse(res_2)
