import json

from django.test import TestCase

from rest_framework.test import APIRequestFactory

from Api.views import (
    get_all_lists,
    get_list,
    insert_list,
    update_list,
    delete_list,
    does_list_exists
)
from LoadList.services import List, ListsSet
import utils.tst_db_setup as tst_db

TEST_DATA = [
    {"title": tst_db.TEST_LIST[0]},
    {"tasks": {
                0: {"content": tst_db.TEST_TASKS[0]["content"],
                    "condition": tst_db.TEST_TASKS[0]["condition"]},
                1: {"content": tst_db.TEST_TASKS[1]["content"],
                    "condition": tst_db.TEST_TASKS[1]["condition"]},
              }
     }
]

INSERT_TEST_DATA = [
    {"title": tst_db.TEST_LIST[1]},
    {"tasks": {
                0: {"content": tst_db.TEST_TASKS[0]["content"],
                    "condition": tst_db.TEST_TASKS[0]["condition"]},
                1: {"content": tst_db.TEST_TASKS[1]["content"],
                    "condition": tst_db.TEST_TASKS[1]["condition"]},
              }
     }
]

UPDATE_TEST_DATA = [
    {"title": tst_db.TEST_LIST[0]},
    {"tasks": {
                0: {"content": tst_db.TEST_TASKS[1]["content"],
                    "condition": tst_db.TEST_TASKS[1]["condition"]},
                1: {"content": tst_db.TEST_TASKS[2]["content"],
                    "condition": tst_db.TEST_TASKS[2]["condition"]},
              }
     }
]


class ApiViewsTestCase(TestCase):
    """Test views for API."""

    def setUp(self):
        self.factory = APIRequestFactory()
        tst_db.set_up_test_database()
        tst_db.set_up_test_list([(TEST_DATA[0]["title"],)])
        tst_db.set_up_test_tasks(
            [
                (TEST_DATA[1]["tasks"][0]["content"],
                 TEST_DATA[1]["tasks"][0]["condition"],
                 1),
                (TEST_DATA[1]["tasks"][1]["content"],
                 TEST_DATA[1]["tasks"][1]["condition"],
                 1)
             ]
        )

    def test_get_all_lists(self):
        request = self.factory.get("/get-all-lists")
        lists = [{"title": tst_db.TEST_LIST[0]}]

        response = get_all_lists(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, lists)

    def test_get_list_with_tasks(self):
        request = self.factory.get("/get-list")

        response = get_list(request, tst_db.TEST_LIST[0])

        self.assertEqual(response.data, TEST_DATA)

    def test_insert_list(self):
        request = self.factory.post(
            "/insert",
            json.dumps(INSERT_TEST_DATA),
            content_type="application/json"
        )

        response = insert_list(request)

        lst = List(INSERT_TEST_DATA[0]["title"]).get_as_list()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(INSERT_TEST_DATA, lst)

    def test_update_list(self):
        request = self.factory.post(
            "/update",
            json.dumps(UPDATE_TEST_DATA),
            content_type="application/json"
        )

        response = update_list(request)

        lst = List(UPDATE_TEST_DATA[0]["title"]).get_as_list()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(UPDATE_TEST_DATA, lst)

    def test_delete_list(self):
        request = self.factory.post(
            "/delete",
            json.dumps({"title": TEST_DATA[0]["title"]}),
            content_type="application/json"
        )

        response = delete_list(request)

        lst = ListsSet().get_as_list()

        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(lst) == 0)

    def test_does_list_exists(self):
        request = self.factory.get("existance/")
        response_1 = does_list_exists(request,
                                      {"title": TEST_DATA[0]["title"]})
        response_2 = does_list_exists(request,
                                      {"title": "Test title"})

        self.assertEqual(response_1.status_code, 200)
        self.assertTrue(response_1.data["exists"])
        self.assertFalse(response_2.data["exists"])
