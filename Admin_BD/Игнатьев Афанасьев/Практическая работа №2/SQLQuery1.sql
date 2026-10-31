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

IF SCHEMA_ID(N'reports') IS NULL EXEC(N'CREATE SCHEMA reports');

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

-- 2.7