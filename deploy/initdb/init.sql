-- init.sql

-- Sunucu bilgilerini tutacak bir tablo oluşturuyoruz
CREATE TABLE IF NOT EXISTS server_info (
    id SERIAL PRIMARY KEY,
    server_name VARCHAR(255),
    server_ip VARCHAR(255),
    server_port VARCHAR(10),
    server_type VARCHAR(255),
    server_os_name VARCHAR(255)
);