CREATE TABLE weather (
    city VARCHAR(50),
    temperature FLOAT,
    humidity INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);