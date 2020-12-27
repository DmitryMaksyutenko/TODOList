CREATE TABLE IF NOT EXISTS task
(
    task_id       SERIAL          NOT NULL,
    content       VARCHAR(100)    NOT NULL,
    condition     BOOLEAN         NOT NULL DEFAULT FALSE,
    list_id       INT             NOT NULL,

    PRIMARY KEY (task_id),
    FOREIGN KEY (list_id) REFERENCES list (list_id) ON DELETE CASCADE
);
