DROP TABLE dagym;
DROP TABLE members;
DROP TABLE gymclasses;


CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    sex VARCHAR(255),
    wallet INT,
    membership_type BOOLEAN
);

CREATE TABLE gymclasses(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price INT,
    capacity INT,
    runtime INT
);



CREATE TABLE dagym(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    till INT,
    member_id INT REFERENCES members(id), 
    gym_class_id INT REFERENCES gymclasses(id)
);

