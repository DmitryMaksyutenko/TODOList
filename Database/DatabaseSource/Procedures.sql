CREATE PROCEDURE insert_tasks(list_id INT, tasks JSONB)
LANGUAGE plpgsql AS
$$
DECLARE
    tasks_number INT := jsonb_array_length(tasks) - 1;
    context VARCHAR;
    condition BOOLEAN;
BEGIN
    FOR i IN 0..tasks_number
    LOOP
        context = tasks->i->>'context';
        condition = tasks->i->'condition';

        INSERT INTO task
        VALUES (default, context, condition, list_id);
    END LOOP;
END;
$$;


CREATE PROCEDURE insert_list_with_tasks(list_title VARCHAR, tasks JSONB)
LANGUAGE plpgsql AS
$$
DECLARE
    list_id INT := insert_into_list_return_list_id(list_title);
BEGIN
    CALL insert_tasks(list_id, tasks);
END;
$$;


CREATE PROCEDURE update_list_with_tasks(list_title VARCHAR, tasks JSONB)
LANGUAGE plpgsql AS
$$
DECLARE
    list_id_to_update INT := (SELECT list.list_id FROM list WHERE list.title = list_title);
BEGIN
    DELETE FROM task
    WHERE task.list_id = list_id_to_update;

    CALL insert_tasks(list_id_to_update, tasks);
END;
$$;


CREATE PROCEDURE delete_list(list_title VARCHAR)
LANGUAGE plpgsql AS
$$
BEGIN
    DELETE FROM list
    WHERE list.title = list_title;
END;
$$;
