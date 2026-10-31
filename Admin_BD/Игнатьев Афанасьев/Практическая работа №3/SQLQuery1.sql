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




