CREATE VIEW get_lists AS
SELECT  title
FROM list;


CREATE VIEW get_list_with_tasks AS
SELECT title, context, condition
FROM list JOIN task ON
    list.list_id = task.list_id;