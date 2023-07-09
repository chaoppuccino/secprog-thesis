-- Create tables 

CREATE TABLE IF NOT EXISTS employees 
                (e_id TEXT PRIMARY KEY UNIQUE NOT NULL,
                name TEXT NOT NULL,
                hourly_wage INT NOT NULL);

CREATE TABLE IF NOT EXISTS messages 
                (content TEXT NOT NULL,
                 id INTEGER PRIMARY KEY AUTOINCREMENT);


-- Clear all table rows

DELETE FROM employees;
DELETE FROM messages;


-- Add sample rows

INSERT INTO employees (e_id, name, hourly_wage) VALUES
    ("kime62", "Kim Mendez", 45),
    ("isjo67", "Isabel Jones", 37),
    ("medo24", "Melvin Doe", 29),
    ("lech83", "Lewis Chambers", 33),
    ("sohi05", "Sofia Hines", 40);

INSERT INTO messages (content) VALUES
    ("Hello world!");