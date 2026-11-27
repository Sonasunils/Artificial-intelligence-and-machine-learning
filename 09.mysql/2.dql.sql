#1. Switching to database

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

#3. Inserting student details into the table

INSERT INTO student_details
(student_id, student_name, age, gender, email, phone, course, fees)
VALUES
(1, 'Anu', 21, 'Female', 'anu@gmail.com', 9876543210, 'Python', 15000),
(2, 'Rahul', 23, 'Male', 'rahul@gmail.com', 9876543211, 'Data Science', 25000),
(3, 'Meera', 22, 'Female', 'meera@gmail.com', 9876543212, 'Python', 15000),
(4, 'Arjun', 24, 'Male', 'arjun@gmail.com', 9876543213, 'Java', 12000),
(5, 'Anjali', 20, 'Female', 'anjali@gmail.com', 9876543214, 'Data Science', 25000),
(6, 'Akhil', 25, 'Male', 'akhil@gmail.com', 9876543215, 'Python', 15000),
(7, 'Sneha', 21, 'Female', 'sneha@gmail.com', 9876543216, 'Java', 12000),
(8, 'Vishnu', 23, 'Male', 'vishnu@gmail.com', 9876543217, 'Data Science', 25000),
(9, 'Amal', 22, 'Male', NULL, 9876543218, 'Python', 15000),
(10, 'Diya', 24, 'Female', 'diya@gmail.com', 9876543219, 'Java', 12000);

#4. Displaying all student records

SELECT * FROM student_details;

#5. Selecting particular columns

SELECT student_id, student_name, age
FROM student_details;

#6. Selecting records using WHERE condition

SELECT * FROM student_details
WHERE age > 20;

#7. Selecting records using AND operator

SELECT * FROM student_details
WHERE age > 20 AND fees > 10000;

#8. Selecting records using OR operator

SELECT * FROM student_details
WHERE course = 'Python' OR course = 'Data Science';

#9. Selecting records using NOT operator

SELECT * FROM student_details
WHERE NOT course = 'Python';

#10. Selecting records using BETWEEN operator

SELECT * FROM student_details
WHERE age BETWEEN 20 AND 23;

#11. Selecting records using IN operator

SELECT * FROM student_details
WHERE course IN ('Python', 'Java');

#12. Selecting records using LIKE operator

SELECT * FROM student_details
WHERE student_name LIKE 'A%';

#13. Selecting distinct course names

SELECT DISTINCT course
FROM student_details;

#14. Sorting records in ascending order

SELECT * FROM student_details
ORDER BY fees ASC;

#15. Sorting records in descending order

SELECT * FROM student_details
ORDER BY fees DESC;

#16. Grouping students by course

SELECT course, COUNT(*)
FROM student_details
GROUP BY course;

#17. Grouping students by age

SELECT age, COUNT(*)
FROM student_details
GROUP BY age;

#18. Filtering grouped records using HAVING

SELECT course, COUNT(*)
FROM student_details
GROUP BY course
HAVING COUNT(*) > 2;

#19. Limiting the number of records

SELECT * FROM student_details
LIMIT 5;

#20. Using LIMIT with OFFSET

SELECT * FROM student_details
LIMIT 5 OFFSET 2;

#21. Using WHERE with GROUP BY

SELECT course, COUNT(*)
FROM student_details
WHERE fees > 10000
GROUP BY course;

#22. Using GROUP BY with HAVING and ORDER BY

SELECT course, COUNT(*)
FROM student_details
GROUP BY course
HAVING COUNT(*) > 1
ORDER BY course ASC;

#23. Selecting records using IS NULL

SELECT * FROM student_details
WHERE email IS NULL;

#24. Selecting records using IS NOT NULL

SELECT * FROM student_details
WHERE email IS NOT NULL;