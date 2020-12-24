from django.urls import path, re_path

from .views import (
    get_all_lists,
    get_list,
    insert_list,
    update_list,
    delete_list
)

app_name = "Api"

urlpatterns = [
    path("lists/", get_all_lists),
    re_path(r"list/(?P<title>[a-zA-z0-9 -]+)", get_list),
    re_path("insert/", insert_list),
    re_path("update/", update_list),
    re_path("delete/", delete_list)
]
