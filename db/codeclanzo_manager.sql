DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    merchant VARCHAR(255),
    catagory VARCHAR(255),
    amount FLOAT,
    user_id INT NOT NULL REFERENCES users(id)
);