-- 1.1

IF DB_ID(N'library_db') IS NULL CREATE DATABASE library_db;

SELECT name FROM sys.databases

-- 1.2

CREATE DATABASE library_db;

-- 1.3

IF DB_ID(N'college_db') IS NULL CREATE DATABASE college_db;

ALTER DATABASE college_db COLLATE Cyrilic_General_CI_AS;

SELECT name, collation_name FROM sys.databases

-- 1.4

USE library_db;

SELECT DB_NAME(); 

USE college_db;

SELECT DB_NAME(); 

-- 1.5

USE college_db;

DROP DATABASE college_db;

-- 1.6

DROP DATABASE test_db IF EXISTS db;

IF DB_ID(N'test_db') IS NULL CREATE DATABASE test_db;

USE test_db;

-- 1.7

CREATE DATABASE shop_dev; 
CREATE DATABASE shop_test; 
CREATE DATABASE shop_prod;

DROP DATABASE shop_dev, shop_test;

SELECT name FROM sys.databases;

-- 2.1

USE library_db;

SELECT name FROM sys.schemas

-- 2.2

CREATE SCHEMA catalog;
CREATE SCHEMA readers;
CREATE SCHEMA loans;

-- 2.3

IF SCHEMA_ID(N'reports') IS NULL 
	EXEC(N'CREATE SCHEMA reports');

-- 2.4

CREATE SCHEMA temp_data;

DROP SCHEMA IF EXISTS temp_data;

-- 2.5

CREATE SCHEMA archive;

CREATE TABLE archive.old_books (
	book_id INT, 
	title   NVARCHAR(200));

DROP TABLE archive.old_books;

DROP SCHEMA IF EXISTS archive;

-- 2.6

CREATE SCHEMA old_schema;

CREATE TABLE old_schema.notes (
	note_id INT
	);

ALTER SCHEMA dbo TRANSFER old_schema.notes;

DROP SCHEMA IF EXISTS old_schema;

-- 3.3

USE library_db; -- 1
-- 2
CREATE TABLE dbo.type_test (
    small_num TINYINT,
    short_text VARCHAR(5),
    price DECIMAL(5,2)
);

-- Последовательно для таблицы
-- 1
INSERT INTO dbo.type_test (small_num, short_text, price) VALUES (255, 'abc', 999.99); -- Это будет в таблице

-- 2
INSERT INTO dbo.type_test (small_num, short_text, price) VALUES (256, 'abc', 10);

-- 3
INSERT INTO dbo.type_test (small_num, short_text, price) VALUES (-1, 'abc', 10);

-- 4
INSERT INTO dbo.type_test (small_num, short_text, price) VALUES (10, 'abcdefgh', 10);

-- 5
INSERT INTO dbo.type_test (small_num, short_text, price) VALUES (10, 'abc', 1000);

-- 6
INSERT INTO dbo.type_test (small_num, short_text, price) VALUES (10, 'abc', 12.345); -- Это будет в таблице

-- Проверка

SELECT * FROM dbo.type_test

-- 3.4

-- 1
CREATE TABLE dbo.name_test (
    a VARCHAR(50),
    b NVARCHAR(50)
);
INSERT INTO dbo.name_test VALUES (N'Иван', N'Иван'); -- 2
INSERT INTO dbo.name_test VALUES (N'東京', N'東京'); -- 3
SELECT * FROM dbo.name_test; -- 4

-- 4.1

USE test_db; -- 1
-- 2
CREATE TABLE dbo.specialties (
    specialty_id INT IDENTITY(1,1) NOT NULL
        CONSTRAINT pk_specialties PRIMARY KEY,
    code  NVARCHAR(20)  NOT NULL
        CONSTRAINT uq_specialties_code UNIQUE,
    title NVARCHAR(150) NOT NULL
);

-- 4.2

-- 1
CREATE TABLE dbo.study_groups (
    group_id     INT IDENTITY(100, 10) NOT NULL
        CONSTRAINT pk_study_groups PRIMARY KEY,
    group_name   NVARCHAR(50)  NOT NULL
        CONSTRAINT uq_study_groups_name UNIQUE,
    course       TINYINT       NOT NULL
        CONSTRAINT df_study_groups_course  DEFAULT 1
        CONSTRAINT ck_study_groups_course  CHECK (course BETWEEN 1 AND 4),
    max_students TINYINT       NOT NULL
        CONSTRAINT df_study_groups_max     DEFAULT 25
        CONSTRAINT ck_study_groups_max     CHECK (max_students BETWEEN 1 AND 30),
    is_budget    BIT           NOT NULL
        CONSTRAINT df_study_groups_budget  DEFAULT 1,
    created_at   DATETIME2     NOT NULL
        CONSTRAINT df_study_groups_created DEFAULT SYSDATETIME()
);

-- Проверка автонумерации
-- 1
INSERT INTO dbo.study_groups (group_name, course)
VALUES (N'ИС-21', 1), (N'ИС-22', 2);
-- 2
SELECT group_id, group_name, course, max_students, is_budget, created_at
FROM dbo.study_groups;

-- 4.3

-- 1
CREATE TABLE dbo.students (
    student_id   INT IDENTITY(1,1) NOT NULL
        CONSTRAINT pk_students PRIMARY KEY,
    last_name    NVARCHAR(100) NOT NULL,
    first_name   NVARCHAR(100) NOT NULL,
    middle_name  NVARCHAR(100) NULL,
    birth_date   DATE          NOT NULL
        CONSTRAINT ck_students_birth_date CHECK (birth_date >= '1950-01-01'),
    email        NVARCHAR(100) NULL
        CONSTRAINT uq_students_email UNIQUE,
    group_id     INT           NULL
        CONSTRAINT fk_students_group
        FOREIGN KEY REFERENCES dbo.study_groups(group_id)
);
-- Проверка работы FK
INSERT INTO dbo.students (last_name, first_name, birth_date, group_id)
VALUES (N'Иванов', N'Иван', '2005-04-12', 100);   -- OK
INSERT INTO dbo.students (last_name, first_name, birth_date, group_id)
VALUES (N'Петров', N'Пётр', '2004-09-30', 999);   -- ошибка

-- 4.4

EXEC sp_help 'dbo.students'; -- 1

DROP TABLE IF EXISTS dbo.students; -- 2
--3
CREATE TABLE dbo.students (
    student_id   INT IDENTITY(1,1) NOT NULL
        CONSTRAINT pk_students PRIMARY KEY,
    last_name    NVARCHAR(100) NOT NULL,
    first_name   NVARCHAR(100) NOT NULL,
    middle_name  NVARCHAR(100) NULL,
    birth_date   DATE          NOT NULL
        CONSTRAINT ck_students_birth_date CHECK (birth_date >= '1950-01-01'),
    email        NVARCHAR(100) NULL
        CONSTRAINT uq_students_email UNIQUE,
    group_id     INT           NULL
        CONSTRAINT fk_students_group
        FOREIGN KEY REFERENCES dbo.study_groups(group_id)
);

EXEC sp_help 'dbo.students'; -- 3

-- 4.5

-- 1
CREATE TABLE dbo.grades (
    student_id   INT           NOT NULL,
    subject_name NVARCHAR(100) NOT NULL,
    exam_date    DATE          NOT NULL,
    grade        TINYINT       NOT NULL
        CONSTRAINT ck_grades_value CHECK (grade BETWEEN 2 AND 5),
    CONSTRAINT pk_grades PRIMARY KEY (student_id, subject_name),
    CONSTRAINT fk_grades_student
        FOREIGN KEY (student_id) REFERENCES dbo.students(student_id)
);
--ВАЖНО!! по очереди! Так как мы удалили таблицу студента не находит и связь не создаётся нормально
-- 1. Создаём студента
INSERT INTO dbo.students (last_name, first_name, birth_date)
VALUES (N'Иванов', N'Иван', '2005-04-12');

-- 2. Узнаём его id
DECLARE @sid INT = SCOPE_IDENTITY();

-- 3. Первая оценка — пройдёт
INSERT INTO dbo.grades VALUES (@sid, N'Математика', '2024-06-15', 5);

-- 4. Вторая по тому же предмету — упадёт на pk_grades
INSERT INTO dbo.grades VALUES (@sid, N'Математика', '2024-06-20', 4);

-- 2 по очереди Проверка составного ключа
INSERT INTO dbo.grades VALUES (1, N'Математика', '2024-06-15', 5);  -- OK
INSERT INTO dbo.grades VALUES (1, N'Математика', '2024-06-20', 4);  -- ошибка

SELECT * FROM dbo.grades;

-- 4.6

-- 1
CREATE TABLE dbo.teachers (
    teacher_id   INT IDENTITY(1,1) NOT NULL
        CONSTRAINT pk_teachers PRIMARY KEY,
    full_name    NVARCHAR(150) NOT NULL,
    phone_number VARCHAR(20)   NULL,
    hire_date    DATE          NULL,
    salary       DECIMAL(10,2) NOT NULL
        CONSTRAINT ck_teachers_salary CHECK (salary > 0),
    CONSTRAINT idx_teachers_full_name UNIQUE (full_name)
);

-- 2 проверка
SELECT i.name AS index_name, c.name AS column_name
FROM sys.indexes i
JOIN sys.index_columns ic ON ic.object_id = i.object_id AND ic.index_id = i.index_id
JOIN sys.columns c ON c.object_id = ic.object_id AND c.column_id = ic.column_id
WHERE i.object_id = OBJECT_ID(N'dbo.teachers');

-- 4.7

DROP TABLE dbo.study_groups; -- 1 ошибка Пояснение: на study_groups ссылается students через fk_students_group. SQL Server не позволяет повесить дочерние строки без родителя.

DROP TABLE dbo.grades; -- 2
DROP TABLE dbo.students;
DROP TABLE dbo.study_groups;

-- study_groups (из 4.2)
CREATE TABLE dbo.study_groups (
    group_id     INT IDENTITY(100, 10) PRIMARY KEY,
    group_name   NVARCHAR(50)  NOT NULL UNIQUE,
    course       TINYINT       NOT NULL DEFAULT 1 CHECK (course BETWEEN 1 AND 4),
    max_students TINYINT       NOT NULL DEFAULT 25 CHECK (max_students BETWEEN 1 AND 30),
    is_budget    BIT           NOT NULL DEFAULT 1,
    created_at   DATETIME2     NOT NULL DEFAULT SYSDATETIME()
);

-- students (из 4.4)
CREATE TABLE dbo.students (
    student_id   INT IDENTITY(1,1) PRIMARY KEY,
    last_name    NVARCHAR(100) NOT NULL,
    first_name   NVARCHAR(100) NOT NULL,
    middle_name  NVARCHAR(100) NULL,
    birth_date   DATE          NOT NULL CHECK (birth_date >= '1950-01-01'),
    email        NVARCHAR(100) NULL UNIQUE,
    group_id     INT           NULL REFERENCES dbo.study_groups(group_id)
);

-- grades (из 4.5)
CREATE TABLE dbo.grades (
    student_id   INT           NOT NULL,
    subject_name NVARCHAR(100) NOT NULL,
    exam_date    DATE          NOT NULL,
    grade        TINYINT       NOT NULL CHECK (grade BETWEEN 2 AND 5),
    PRIMARY KEY (student_id, subject_name),
    FOREIGN KEY (student_id) REFERENCES dbo.students(student_id)
);

-- 4.8

-- 1.1
CREATE TABLE dbo.logs (
    log_id  INT IDENTITY(1,1) NOT NULL
        CONSTRAINT pk_logs PRIMARY KEY,
    message NVARCHAR(200) NOT NULL
);

-- 1.2
INSERT INTO dbo.logs (message) VALUES (N'первое'), (N'второе'), (N'третье');
SELECT * FROM dbo.logs;

-- 2
TRUNCATE TABLE dbo.logs;
INSERT INTO dbo.logs (message) VALUES (N'четвёртое');
SELECT * FROM dbo.logs;

-- 3
DROP TABLE dbo.logs; -- удаление
SELECT * FROM dbo.logs; -- ошибка

-- 5.1

USE library_db; -- 1



