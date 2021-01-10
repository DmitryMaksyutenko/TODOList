from django.urls import path, re_path

from .views import (
    get_all_lists,
    get_list,
    insert_list,
    update_list,
    delete_list,
    does_list_exists
)

app_name = "Api"

urlpatterns = [
    re_path(r"list/(?P<title>[a-zA-z0-9 -]+)", get_list),
    re_path(r"exists/(?P<title>[a-zA-z0-9 -]+)", does_list_exists),
    path("lists/", get_all_lists),
    path("insert/", insert_list),
    path("update/", update_list),
    path("delete/", delete_list)
]
