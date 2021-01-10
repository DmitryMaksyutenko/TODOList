from Database.models import (Lists,
                             ListWithTasks)


class ListsSet:
    """Class for Lists titles."""

    def __init__(self):
        self.titles = Lists.objects.values_list("title", flat=True)

    def count(self):
        """Return number of lists."""
        return self.titles.count()

    def _get_list(self):
        """Return the Python list of titles."""
        return [elem for elem in self.titles]

    def get_as_list(self):
        """Return the lists titles in json format."""
        tmp_list = self._get_list()
        titles_list = [{"title": i} for i in tmp_list]
        return titles_list


class List:
    """Class for tasks inside the list."""

    def __init__(self, list_title):
        self.list = ListWithTasks.objects.filter(title=list_title)
        self.count = self.list.count()
        self.search_title = list_title

    def get_as_list(self):
        """Return the Python list with List title and task(s)."""
        lst_title = self._get_list_title()
        tasks = self._get_tasks_for_title()
        return [lst_title, tasks]

    def _get_list_title(self):
        """Return list titile as dict."""
        return {
            "title": self.list.filter(title=self.search_title).first().title
        }

    def _get_tasks_for_title(self):
        """Return tasks for corresponding title as dict."""
        tasks = {"tasks": {}}
        for i in range(self.count):
            tasks["tasks"].setdefault(
                i,
                {"content": self.list[i].content,
                 "condition": self.list[i].condition}
            )
        return tasks
