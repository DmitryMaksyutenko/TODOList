CREATE TABLE IF NOT EXISTS list
(
    list_id  SERIAL       NOT NULL,
    title    VARCHAR(50)  NOT NULL UNIQUE CHECK(title ~ '^[A-Z]'),

    PRIMARY KEY (list_id)
);

