
-- GRANT ALL PRIVILEGES ON *.* TO 'duongdx'@'%' IDENTIFIED BY '${MYSQL_PASSWORD}';
-- GRANT ALL PRIVILEGES ON *.* TO 'duongdx'@'localhost' IDENTIFIED BY '${MYSQL_PASSWORD}';

-- DROP DATABASE IF EXISTS webappdb;
-- CREATE DATABASE webappdb;
-- USE webappdb;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);
