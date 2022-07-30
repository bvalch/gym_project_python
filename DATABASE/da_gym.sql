DROP TABLE gymsession;
DROP TABLE members;
DROP TABLE gymclasses;


CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    sex VARCHAR(255),
    
    membership_type BOOLEAN
);

CREATE TABLE gymclasses(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price INT,
    capacity INT,
    runtime INT
);



CREATE TABLE gymsessions(
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id), 
    gymclass_id INT REFERENCES gymclasses(id)
);

