#1. Switching to database

USE student;

#2. Displaying all student records

SELECT * FROM student_details;

#3. Inserting a single record into the table

INSERT INTO student_details
(student_id, student_name, age, gender, email, phone, course, fees)
VALUES
(11, 'Kiran', 22, 'Male', 'kiran@gmail.com', 9876543220, 'Python', 15000);

#4. Inserting multiple records into the table

INSERT INTO student_details
(student_id, student_name, age, gender, email, phone, course, fees)
VALUES
(12, 'Neha', 21, 'Female', 'neha@gmail.com', 9876543221, 'Java', 12000),
(13, 'Manu', 23, 'Male', 'manu@gmail.com', 9876543222, 'Python', 15000),
(14, 'Kavya', 24, 'Female', 'kavya@gmail.com', 9876543223, 'Data Science', 25000);

#5. Inserting values into particular columns

INSERT INTO student_details
(student_id, student_name, age)
VALUES
(15, 'Akhila', 22);

#6. Updating a particular record

UPDATE student_details
SET age = 25
WHERE student_id = 1;

#7. Updating multiple columns in a record

UPDATE student_details
SET age = 26, course = 'Java', fees = 12000
WHERE student_id = 2;

#8. Updating records using a condition

UPDATE student_details
SET fees = 18000
WHERE course = 'Python';

#9. Updating all records in a particular column

UPDATE student_details
SET gender = 'Female'
WHERE student_id = 15;

#10. Deleting a particular record

DELETE FROM student_details
WHERE student_id = 11;

#11. Deleting records using a condition

DELETE FROM student_details
WHERE course = 'Java';

#12. Deleting multiple records using a condition

DELETE FROM student_details
WHERE age > 23;

#13. Displaying the updated table

SELECT * FROM student_details;