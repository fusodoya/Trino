CREATE SCHEMA IF NOT EXISTS metastore.postgres
WITH (location = 's3://trino/');

CREATE TABLE IF NOT EXISTS metastore.postgres.score (
  id VARCHAR(10),
  student_id VARCHAR(10),
  subject_id VARCHAR(10),
  score DOUBLE
) WITH (
  external_location = 's3://trino/data',
  format = 'PARQUET'
);