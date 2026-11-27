#1. Switching to a database

USE student;

#2. Creating a student table

CREATE TABLE student_details (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    email VARCHAR(100),
    phone BIGINT,
    course VARCHAR(50),
    fees DECIMAL(10,2)
);

#3. Displaying all tables

SHOW TABLES;

#4. Verifying the table structure

DESC student_details;

#5. Adding a new column

ALTER TABLE student_details
ADD address VARCHAR(100);

#6. Adding multiple columns

ALTER TABLE student_details
ADD dob DATE,
ADD admission_date DATE;

#7. Dropping a particular column

ALTER TABLE student_details
DROP COLUMN gender;

#8. Modifying a column datatype or size

ALTER TABLE student_details
MODIFY COLUMN student_name VARCHAR(100);

#9. Renaming a particular column

ALTER TABLE student_details
RENAME COLUMN phone TO mobile_number;

#10. Renaming a table

RENAME TABLE student_details TO student_info;

#11. Deleting all records from a table (TRUNCATE)

TRUNCATE TABLE student_info;



#12. Deleting an entire table

DROP TABLE student_info;

#13. Deleting a table if it exists

DROP TABLE IF EXISTS student_info;

#14. Checking all tables

SHOW TABLES;