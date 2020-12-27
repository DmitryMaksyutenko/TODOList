from django.db import models


class Lists(models.Model):
    """Class for get_lists view."""
    title = models.CharField(max_length=50, primary_key=True)

    class Meta:
        managed = False
        db_table = 'lists'


class ListWithTasks(models.Model):
    """Class for get_list_with_tasks view."""
    title = models.CharField(max_length=50, primary_key=True)
    content = models.CharField(max_length=100)
    condition = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = "list_with_tasks"
