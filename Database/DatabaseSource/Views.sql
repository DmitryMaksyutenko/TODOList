CREATE OR REPLACE VIEW lists AS
SELECT  title
FROM list;


CREATE OR REPLACE VIEW list_with_tasks AS
SELECT title, content, condition
FROM list JOIN task ON
    list.list_id = task.list_id;
