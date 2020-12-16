from django.http import HttpResponse
from django.db.utils import IntegrityError

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from LoadList.services import ListsSet, List
from CreateList.services import InsertManager
from UpdateList.services import UpdateManager
from DeleteList.services import DeleteManager
from ExistenceList.services import ExistenceManager


@api_view(["GET"])
def get_all_lists(request):
    if request.method == "GET":
        data = ListsSet().get_as_list()
        return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_list(request, title):
    if request.method == "GET":
        try:
            data = List(title).get_as_list()
        except AttributeError:
            return HttpResponse("There are no '%s'" % title)
        return Response(data, status=status.HTTP_200_OK)


@api_view(["POST"])
def insert_list(request):
    if request.method == "POST":
        try:
            mngr = InsertManager()
            mngr.insert(request.data)
            return Response({}, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({}, status=status.HTTP_200_OK)


@api_view(["POST"])
def update_list(request):
    if request.method == "POST":
        mngr = UpdateManager()
        mngr.update(request.data)
        return Response({}, status=status.HTTP_200_OK)


@api_view(["POST"])
def delete_list(request):
    if request.method == "POST":
        del_obj = DeleteManager()
        del_obj.delete(request.data)
        return Response({}, status=status.HTTP_200_OK)


@api_view(["GET"])
def does_list_exists(request, data):
    if request.method == "GET":
        mngr = ExistenceManager()
        result = mngr.exists(data)
        return Response({"exists": result}, status=status.HTTP_200_OK)
