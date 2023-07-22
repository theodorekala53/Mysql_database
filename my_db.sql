-- Active: 1689979111842@@127.0.0.1@3306

DROP DATABASE IF EXISTS user_db;

CREATE DATABASE user_db;
DEFAULT CHARACTER SET = 'utf8mb4';

USE user_db;

-- Hier können Sie Ihre SQL-Befehle eingeben, z. B. CREATE TABLE, INSERT, SELECT usw.
CREATE TABLE benutzer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    benutzername VARCHAR(50) NOT NULL,
    passwort VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

INSERT INTO benutzer (benutzername, passwort, email) VALUES
    ('theodore', 'theodore123', 'theodorekala@yahooo.fr'),
    ('Therese', 'therese123', 'noubissikala@yahooo.fr'),
    ('Ericka', 'Martine', 'Erickamartine@yahooo.fr');

SELECT * FROM benutzer;