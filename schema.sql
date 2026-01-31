CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    quantity INTEGER
);