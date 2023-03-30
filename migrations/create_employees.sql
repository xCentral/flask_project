DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS credentials;

CREATE TABLE IF NOT EXISTS accounts(
    id serial PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    ip_address VARCHAR(255,
    created_at TIMESTAMP);

CREATE TABLE IF NOT EXISTS credentials(
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    current_employer VARCHAR(255) NOT NULL,
    city_of_residence VARCHAR(255) NOT NULL,
    invested_amount NUMERIC(10,2) NOT NULL,
    FOREIGN KEY (account_id) REFERENCES accounts(id)
    );

/* copy restaurants (name, address, city, category, rating, url) FROM 'yelp_lunch_nyc.csv' DELIMITER ',' CSV HEADER; */
