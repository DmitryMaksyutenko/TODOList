CREATE ROLE todolist_role WITH CREATEDB LOGIN;


CREATE TABLESPACE todolist_space
OWNER todolist_role
LOCATION '/todolist_db';


CREATE DATABASE todolist
OWNER todolist_role
ENCODING = 'UTF-8'
TABLESPACE = todolist_space;
