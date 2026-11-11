-- 8.1. Создание базы и схемы

-- исходный код
CREATE DATABASE IF NOT EXISTS hotel_db;
USE hotel_db
CREATE SCHEMA IF NOT EXISTS booking;

-- исправленный код
-- 1
IF DB_ID(N'hotel_db') IS NULL
    CREATE DATABASE hotel_db;
GO

-- 2
USE hotel_db;
GO

-- 3
IF SCHEMA_ID(N'booking') IS NULL
    EXEC(N'CREATE SCHEMA booking');
GO


-- 8.2. Создание таблицы

-- исходный код
CREATE TABLE booking.rooms(
    room_id INT PRIMARY KEY AUTO_INCREMENT,
    room_number VARCHAR(10) NOT NULL UNIQUE,
    price_per_night DECIMAL(8,2) CHECK(price_per_night > 0),
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- исправленный код
CREATE TABLE booking.rooms(
    room_id         INT           PRIMARY KEY IDENTITY(1,1),
    room_number     VARCHAR(10)   NOT NULL UNIQUE,
    price_per_night DECIMAL(8,2)  CHECK(price_per_night > 0),
    is_available    BIT           DEFAULT 1,
    created_at      DATETIME2     DEFAULT SYSDATETIME()
);
GO


-- 8.3. Изменение таблицы

-- исходный код
ALTER TABLE booking.rooms ADD COLUMN floor TINYINT AFTER room_number;
ALTER TABLE booking.rooms MODIFY COLUMN room_number VARCHAR(20);

-- исправленный код
-- 1
ALTER TABLE booking.rooms
    ADD floor TINYINT;
GO

-- 2
ALTER TABLE booking.rooms
    ALTER COLUMN room_number VARCHAR(20);
GO


-- 8.4. Вставка номеров

-- исходный код
INSERT INTO booking.rooms(room_number, price_per_night, is_available)
VALUES(' 101 ', 3500.00, TRUE),
      (' 102 ', 'три тысячи', 1),
      (' 101 ', 4200.50, 0);

-- исправленный код
INSERT INTO booking.rooms(room_number, price_per_night, is_available)
VALUES
    ('101', 3500.00, 1),
    ('102', 3000.00, 1),
    ('103', 4200.50, 0);
GO


-- 8.5. Таблица гостей

-- исходный код
CREATE TABLE booking.guests(
    guest _id INT IDENTITY(1,1) PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    birth_date DATE
);

INSERT INTO booking.guests
VALUES(1, 'Иванов Иван', ' 15.03.1990 ');

-- исправленный код
-- 1
CREATE TABLE booking.guests(
    guest_id   INT           IDENTITY(1,1) PRIMARY KEY,
    full_name  VARCHAR(100)  NOT NULL,
    birth_date DATE
);
GO

-- 2
INSERT INTO booking.guests(full_name, birth_date)
VALUES(N'Иванов Иван', '1990-03-15');
GO


-- 8.6. Удаление схемы (логическая ошибка)

-- исходный код
DROP SCHEMA booking;
DROP TABLE booking.rooms;
DROP TABLE booking.guests;

-- исправленный код
-- 1
DROP TABLE IF EXISTS booking.rooms;
DROP TABLE IF EXISTS booking.guests;
GO

-- 2
DROP SCHEMA IF EXISTS booking;
GO


-- 8.7. Удаление базы (логическая ошибка)

-- исходный код
DROP DATABASE hotel_db;

-- исправленный код
-- 1
USE master;
GO

-- 2
DROP DATABASE IF EXISTS hotel_db;
GO