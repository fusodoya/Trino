CREATE TABLE IF NOT EXISTS student (
  id VARCHAR(10),
  name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS subject (
  id VARCHAR(10),
  name VARCHAR(100) NOT NULL,
  credit INT NOT NULL
);

TRUNCATE TABLE student;
TRUNCATE TABLE subject;

INSERT INTO student (id, name) VALUES
('student001', 'Alice'),
('student002', 'Bob'),
('student003', 'Charlie');

INSERT INTO subject (id, name, credit) VALUES
('subject001', 'Math', 3),
('subject002', 'Physics', 4),
('subject003', 'Literature', 2),
('subject004', 'Chemistry', 3),
('subject005', 'Biology', 3),
('subject006', 'IT', 2);
