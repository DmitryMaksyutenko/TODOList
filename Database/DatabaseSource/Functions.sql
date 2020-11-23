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


CREATE FUNCTION is_list_exists(title VARCHAR)
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