#1. COUNT() – Counts the total number of students

SELECT COUNT(*)
FROM student_details;

#2. COUNT() – Counts non-NULL email values

SELECT COUNT(email)
FROM student_details;

#3. SUM() – Calculates the total course fees

SELECT SUM(fees)
FROM student_details;

#4. AVG() – Calculates the average course fees

SELECT AVG(fees)
FROM student_details;

#5. MIN() – Finds the minimum course fees

SELECT MIN(fees)
FROM student_details;

#6. MAX() – Finds the maximum course fees

SELECT MAX(fees)
FROM student_details;

#7. COUNT() with GROUP BY

SELECT course, COUNT(*)
FROM student_details
GROUP BY course;

#8. SUM() with GROUP BY

SELECT course, SUM(fees)
FROM student_details
GROUP BY course;

#9. AVG() with GROUP BY

SELECT course, AVG(fees)
FROM student_details
GROUP BY course;

#10. MIN() with GROUP BY

SELECT course, MIN(fees)
FROM student_details
GROUP BY course;

#11. MAX() with GROUP BY

SELECT course, MAX(fees)
FROM student_details
GROUP BY course;

#12. Aggregate functions with HAVING

SELECT course, COUNT()
FROM student_details
GROUP BY course
HAVING COUNT() > 2;

#13. Multiple aggregate functions in one query

SELECT
COUNT(*) AS total_students,
SUM(fees) AS total_fees,
AVG(fees) AS average_fees,
MIN(fees) AS minimum_fees,
MAX(fees) AS maximum_fees
FROM student_details;

#14. Aggregate functions with WHERE

SELECT AVG(fees)
FROM student_details
WHERE course = 'Python';