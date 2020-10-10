-- creating table with one column as array type.
CREATE TABLE IF NOT EXISTS "emp" (
  "id"                 BIGSERIAL PRIMARY KEY,
  "name"               VARCHAR   NOT NULL    CHECK (INITCAP("name")    = "name"),
  "surname"            VARCHAR   NOT NULL    CHECK (INITCAP("surname") = "surname"),
  "contactNumberArray" VARCHAR [9],
  "email"              VARCHAR   UNIQUE      CHECK (LOWER("email")     = "email")
);

-- inserting array data into table.
INSERT INTO "emp" (
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
FROM "emp";

-- concatenating table columns using CONCAT function
-- and showing column output in title case.
SELECT
  *,
  INITCAP(CONCAT("name", ' ', "surname")) AS "fullName"
FROM "emp"
WHERE
      "name"    IS NOT NULL
  AND "name"    != ''
  AND "surname" IS NOT NULL
  AND "surname" != ''
LIMIT 5;

-- droping exist table.
DROP TABLE IF EXISTS "emp" CASCADE;

-- updating array data into table.
UPDATE "emp"
SET "contactNumberArray"[1] = '9884098840'
WHERE "id" = 101;

-- selecting table column array length.
SELECT
  ARRAY_LENGTH("contactNumberArray", 1) AS "contactNumberArrayLength"
FROM "emp";

-- selecting table column array index 1 values.
SELECT
  INITCAP(CONCAT("name", ' ', "surname")) AS "fullName",
  "contactNumberArray"[1]
FROM "emp";

-- selecting expanded array in to multiple rows.  
SELECT
  INITCAP(CONCAT("name", ' ', "surname")) AS "fullName",
  UNNEST("contactNumberArray")
FROM "emp";

-- violating unique constraint and handling exception.
INSERT INTO "emp" (
  "name",
  "surname",
  "contactNumberArray",
  "email"
)
VALUES (
  'Raj',
  'Pokala',
  ARRAY ['9885098850', '9848012345'],
  'radha.krishna@gmail.com'
)
ON CONFLICT(email)
DO NOTHING;

-- violating unique constraint and handling exception.
-- upsert (update + insert)
INSERT INTO "emp" (
  "name",
  "surname",
  "contactNumberArray",
  "email"
)
VALUES (
  'Sakshi',
  'Dhoni',
  ARRAY ['9885098850', '9848012345'],
  'radha.krishna@gmail.com'
)
ON CONFLICT("email")
DO
  UPDATE SET "name" = EXCLUDED."name", "surname" = EXCLUDED."surname";


-- violating unique constraint and handling exception.
-- upsert (update + insert)
INSERT INTO "emp" (
  "name",
  "surname",
  "contactNumberArray",
  "email"
)
VALUES (
  'Sakshi',
  'Dhoni',
  ARRAY ['9885098850', '9848012345'],
  'radha.krishna@gmail.com'
)
ON CONFLICT("email")
DO
  UPDATE SET "email" = CONCAT(EXCLUDED."email", ';', "emp"."email");


-- 
SELECT
  country,
  STRING_AGG(DISTINCT city, ',' ORDER BY city ASC) AS cities
FROM country
JOIN city USING (country_id)
GROUP BY country
LIMIT 4;
