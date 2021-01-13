from django.db import connection

from psycopg2.extras import execute_values


def set_up_test_database():
    """Function execute raw SQL for tests."""
    with connection.cursor() as cursor:
        cursor.execute(SQL_DB_SETUP)
        cursor.execute(SQL_INSERT_FUNCS)


def set_up_test_list(data):
    """Inserting data in to List for tests."""
    with connection.cursor() as cursor:
        execute_values(cursor, SQL_TEST_DATA_FOR_LIST, data)


def set_up_test_tasks(data):
    """Inserting data in to Task for tests."""
    with connection.cursor() as cursor:
        execute_values(cursor, SQL_TEST_DATA_FOR_TASK, data)


TEST_LIST = [
    "Some List.",
    "Some Onter List.",
    "Some New List."
]

TEST_TASKS = [
    {"content": "content 1", "condition": False},
    {"content": "content 2", "condition": True},
    {"content": "content 3", "condition": False}
]

TEST_LIST_WITH_TASKS = [
    {"title": TEST_LIST[1]},
    {
        "tasks": {
            0: {
                "content": TEST_TASKS[1]["content"],
                "condition": TEST_TASKS[1]["condition"]
            },
            1: {
                "content": TEST_TASKS[0]["content"],
                "condition": TEST_TASKS[0]["condition"]
            }
        }
    }
]

TEST_LIST_WITH_TASK = [
    {"title": TEST_LIST[0]},
    {
        "tasks": {0: {
            "content": TEST_TASKS[2]["content"],
            "condition": TEST_TASKS[2]["condition"]
            },
        }
    }
]

SQL_DB_SETUP = """
CREATE TABLE IF NOT EXISTS list
(
    list_id  SERIAL        NOT NULL,
    title    VARCHAR(50)   NOT NULL UNIQUE CHECK(title ~ '^[A-Z]'),

    PRIMARY KEY (list_id)
);

CREATE TABLE IF NOT EXISTS task
(
    task_id       SERIAL          NOT NULL,
    content       VARCHAR(100)    NOT NULL,
    condition     BOOLEAN         NOT NULL DEFAULT FALSE,
    list_id       INT             NOT NULL,

    PRIMARY KEY (task_id),
    FOREIGN KEY (list_id) REFERENCES list (list_id) ON DELETE CASCADE
);

CREATE OR REPLACE VIEW lists AS
SELECT  title
FROM list;

CREATE OR REPLACE VIEW list_with_tasks AS
SELECT title, content, condition
FROM list JOIN task ON
    list.list_id = task.list_id;
"""

SQL_TEST_DATA_FOR_LIST = """
INSERT INTO list (title)
VALUES %s;
"""

SQL_TEST_DATA_FOR_TASK = """
INSERT INTO task (content, condition, list_id)
VALUES %s;
"""

SQL_INSERT_FUNCS = """
CREATE FUNCTION insert_into_list_return_list_id(list_title  VARCHAR)
RETURNS INT
LANGUAGE plpgsql AS
$$
DECLARE
    next_list_id INT;
BEGIN
    next_list_id = nextval('list_list_id_seq');

    INSERT INTO list
    VALUES (next_list_id, list_title);

    RETURN next_list_id;
END;
$$;

 CREATE PROCEDURE insert_tasks(list_id INT, tasks JSONB)
LANGUAGE plpgsql AS
$$
DECLARE
    tasks_number INT := jsonb_array_length(tasks) - 1;
    content VARCHAR;
    condition BOOLEAN;
BEGIN
    FOR i IN 0..tasks_number
    LOOP
        content = tasks->i->>'content';
        condition = tasks->i->'condition';

        INSERT INTO task
        VALUES (default, content, condition, list_id);
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

CREATE FUNCTION does_list_exists(title VARCHAR)
RETURNS BOOLEAN
LANGUAGE plpgsql AS
$$
BEGIN
    IF title IN (SELECT list.title FROM list)
    THEN
        RETURN 1;
    ELSE
        RETURN 0;
    END IF;
END;
$$;

"""
