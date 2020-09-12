CREATE TABLE IF NOT EXISTS "Emp" (
  "id"   SERIAL       PRIMARY KEY,
  "name" VARCHAR(50)  NOT NULL,
  "dob"  TIMESTAMP    NOT NULL,
  "sal"  NUMERIC(5,2) NOT NULL
);

INSERT INTO "Emp" ("name", "dob", "sal") VALUES ('Ram', '1985-08-31', 123.45)
