
# mysql -u fahad2023_fahad -h fahad2023.helioho.st -p
# machinelearning!@12

CREATE TABLE helper(
id INT AUTO_INCREMENT PRIMARY KEY,
trainee_id BIGINT NOT NULL,
trainee_status CHAR(10) DEFAULT 'available',
date_created TIMESTAMP DEFAULT NOW(),
    
FOREIGN KEY (trainee_id) REFERENCES trainee(id)
);

CREATE TABLE help_request(
id INT AUTO_INCREMENT PRIMARY KEY,
trainee_id BIGINT NOT NULL,
help_type CHAR(15) NOT NULL,
topic VARCHAR(255) NOT NULL,
help_description TEXT NOT NULL,
helping_status CHAR(15) DEFAULT 'pending',
helper_id INT NOT NULL,
feedback TEXT,
stars INT NOT NULL,
helped_date VARCHAR(255),

date_created TIMESTAMP DEFAULT NOW(),
    
FOREIGN KEY (trainee_id) REFERENCES trainee(id),
FOREIGN KEY (helper_id) REFERENCES helper(id)
);

CREATE TABLE trainee_work(
id INT AUTO_INCREMENT PRIMARY KEY,
trainee_id BIGINT NOT NULL,
work_type CHAR(15) NOT NULL,
materials VARCHAR(255) NOT NULL,
team_work CHAR(10) NOT NULL,
date_created TIMESTAMP DEFAULT NOW(),
    
FOREIGN KEY (trainee_id) REFERENCES trainee(id)
);

ALTER TABLE trainee_work ADD COLUMN work_id TEXT AFTER team_work;

-- INSERT INTO helper(trainee_id)
-- VALUES
-- (30),
-- (49),
-- (80),
-- (40),
-- (97);