CREATE TABLE task
(
    task_id       SERIAL          NOT NULL,
    context       VARCHAR(100)    NOT NULL,
    condition     BOOLEAN         NOT NULL DEFAULT FALSE,
    list_id       INT             NOT NULL,

    PRIMARY KEY (task_id),
    FOREIGN KEY (list_id) REFERENCES list (list_id) ON DELETE CASCADE
);