-- creating table with one column as array type.
CREATE TABLE IF NOT EXISTS "Emp" (
  "id"                 BIGSERIAL PRIMARY KEY,
  "name"               VARCHAR NOT NULL CHECK (INITCAP("name") = "name"),
  "surname"            VARCHAR NOT NULL CHECK (INITCAP("surname") = "surname"),
  "contactNumberArray" VARCHAR [9] NOT NULL,
  "email"              VARCHAR UNIQUE CHECK (LOWER("email") = "email"),
  "active"             BOOLEAN DEFAULT TRUE,
  "insertTime"         TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- creating temporary table based on existing table.
CREATE TEMP TABLE IF NOT EXISTS "empActive"
AS
  SELECT
    "id",
    INITCAP(CONCAT("name", ' ', "surname")) AS "fullName"
  FROM "Emp"
  WHERE "active" IS TRUE;

-- inserting array data into table.
INSERT INTO "Emp" (
  "name",
  "surname",
  "contactNumberArray",
  "email"
)
VALUES (
  'Radha',
  'Krishna',
  ARRAY ['9885098850', '9848012345'],
  'radha.krishna@gmail.com'
);

-- selecting table records.
SELECT *
FROM "Emp";

-- concatenating table columns using CONCAT function
-- and showing column output in title case.
SELECT
  *,
  INITCAP(CONCAT("name", ' ', "surname")) AS "fullName"
FROM "Emp"
WHERE
      "name"    IS NOT NULL
  AND "name"    != ''
  AND "surname" IS NOT NULL
  AND "surname" != ''
LIMIT 5;

-- truncate table.
TRUNCATE TABLE "Emp" RESTART IDENTITY;

-- droping exist table.
DROP TABLE IF EXISTS "Emp" CASCADE;

-- rename existing table.
ALTER TABLE "Emp" RENAME TO "Emp2";

-- 
DELETE FROM "Emp" CASCADE;

DELETE FROM "Emp"
WHERE "active" IS FALSE
RETURNING *;

-- 
TRUNCATE "Emp" CASCADE RESTART IDENTITY;

-- updating array data into table.
UPDATE "Emp"
SET "contactNumberArray"[1] = '9884098840'
WHERE "id" = 101;

-- selecting table column array length.
SELECT
  ARRAY_LENGTH("contactNumberArray", 1) AS "contactNumberArrayLength"
FROM "Emp";

-- selecting table column array index 1 values.
SELECT
  INITCAP(CONCAT("name", ' ', "surname")) AS "fullName",
  "contactNumberArray"[1]
FROM "Emp";

-- selecting expanded array in to multiple rows.  
SELECT
  INITCAP(CONCAT("name", ' ', "surname")) AS "fullName",
  UNNEST("contactNumberArray")
FROM "Emp";

-- violating unique constraint and handling exception.
INSERT INTO "Emp" (
  "name",
  "surname",
  "contactNumberArray",
  "email"
)
VALUES (
  'Radha',
  'Krishna',
  ARRAY ['9885098850', '9848012345'],
  'radha.krishna@gmail.com'
)
ON CONFLICT(email)
DO NOTHING;

-- violating unique constraint and handling exception.
-- upsert (update + insert)
INSERT INTO "Emp" (
  "name",
  "surname",
  "contactNumberArray",
  "email"
)
VALUES (
  'Radha',
  'Krishna',
  ARRAY ['9885098850', '9848012345'],
  'radha.krishna@gmail.com'
)
ON CONFLICT("email")
DO
  UPDATE SET "name" = EXCLUDED."name", "surname" = EXCLUDED."surname";

-- violating unique constraint and handling exception.
-- upsert (update + insert)
INSERT INTO "Emp" (
  "name",
  "surname",
  "contactNumberArray",
  "email"
)
VALUES (
  'Radha',
  'Krishna',
  ARRAY ['9885098850', '9848012345'],
  'radha.krishna@gmail.com'
)
ON CONFLICT("email")
DO
  UPDATE SET "email" = CONCAT(EXCLUDED."email", ';', "emp"."email");

-- date example start

CREATE TABLE IF NOT EXISTS "dateDemo" ("insertDate" TIMESTAMP WITHOUT TIME ZONE);

INSERT INTO "dateDemo" VALUES(TO_TIMESTAMP(1525745241));

SELECT
  "insertDate",
  EXTRACT(EPOCH FROM "insertDate") AS "insertDate2"
FROM "dateDemo";

SELECT
  "insertDate",
  "insertDate" AT TIME ZONE 'UTC' AT TIME ZONE 'Asia/Calcutta' AS "insertDateIst"
FROM "dateDemo";

-- PostgreSQL supported time zones.
SELECT * FROM pg_timezone_names;

-- date example end

-- 
SELECT
  country,
  STRING_AGG(DISTINCT city, ',' ORDER BY city ASC) AS cities
FROM country
JOIN city USING (country_id)
GROUP BY country
LIMIT 4;


SELECT TO_TIMESTAMP(insertDateInNs / 1000000000)::TIMESTAMP AS "insertDate"

-- selecting first event for each user for that day.
-- common table expression.
WITH _event AS (
  SELECT
    ROW_NUMBER() OVER (PARTITION BY "id" ORDER BY "name" DESC) AS "rowNumber",
    *
  FROM "event"
  WHERE "insertDate" = '2020-10-10 00:00:00.000'::TIMESTAMP

SELECT *
FROM _event
WHERE "rowNumber" = 1
