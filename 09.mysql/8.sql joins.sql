
#1. Create database

CREATE DATABASE join_demo;

#2. Select database

USE join_demo;


#3. Create department table

CREATE TABLE department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50),
    location VARCHAR(50)
);


#4. Create student_details table

CREATE TABLE student_details (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    age INT,
    course VARCHAR(50),
    fees DECIMAL(10,2),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES department(dept_id)
);


#5. Insert records into department

INSERT INTO department VALUES
(1, 'Python', 'Kochi'),
(2, 'Data Science', 'Trivandrum'),
(3, 'Java', 'Kollam'),
(4, 'Web Development', 'Calicut'),
(5, 'AI and ML', 'Thrissur');


#6. Insert records into student_details

INSERT INTO student_details VALUES
(101, 'Anu', 21, 'Python', 15000, 1),
(102, 'Rahul', 23, 'Data Science', 25000, 2),
(103, 'Meera', 22, 'Python', 15000, 1),
(104, 'Arjun', 24, 'Java', 12000, 3),
(105, 'Diya', 20, 'Data Science', 25000, 2),
(106, 'Kiran', 25, 'Web Development', 18000, 4),
(107, 'Sneha', 22, 'Python', 15000, 1),
(108, 'Vishnu', 23, 'Java', 12000, 3);


#7. Display department table

SELECT * FROM department;


#8. Display student_details table

SELECT * FROM student_details;





#1. INNER JOIN

SELECT *
FROM student_details
INNER JOIN department
ON student_details.dept_id = department.dept_id;


#2. INNER JOIN with selected columns

SELECT
student_details.student_id,
student_details.student_name,
department.dept_name
FROM student_details
INNER JOIN department
ON student_details.dept_id = department.dept_id;


#3. INNER JOIN using aliases

SELECT
s.student_name,
d.dept_name,
d.location
FROM student_details AS s
INNER JOIN department AS d
ON s.dept_id = d.dept_id;


#4. INNER JOIN with WHERE

SELECT s.student_name, d.dept_name
FROM student_details s
INNER JOIN department d
ON s.dept_id = d.dept_id
WHERE d.dept_name = 'Python';






#1. RIGHT JOIN

SELECT *
FROM student_details
RIGHT JOIN department
ON student_details.dept_id = department.dept_id;


#2. RIGHT JOIN with selected columns

SELECT
s.student_name,
d.dept_name
FROM student_details s
RIGHT JOIN department d
ON s.dept_id = d.dept_id;




#1. CROSS JOIN

SELECT *
FROM student_details
CROSS JOIN department;


#2. CROSS JOIN with selected columns

SELECT
s.student_name,
d.dept_name
FROM student_details s
CROSS JOIN department d;





#1. SELF JOIN

SELECT
s1.student_name AS Student1,
s2.student_name AS Student2,
s1.dept_id
FROM student_details s1
INNER JOIN student_details s2
ON s1.dept_id = s2.dept_id
WHERE s1.student_id <> s2.student_id;


#2. Find students belonging to the same department

SELECT
s1.student_name,
s2.student_name,
s1.course
FROM student_details s1
JOIN student_details s2
ON s1.dept_id = s2.dept_id
WHERE s1.student_id < s2.student_id;


