#1. WHERE Clause

SELECT * FROM student_details
WHERE age > 20;

#2. GROUP BY Clause

SELECT course, COUNT(*)
FROM student_details
GROUP BY course;

#3. HAVING Clause

SELECT course, COUNT(*)
FROM student_details
GROUP BY course
HAVING COUNT(*) > 2;

#4. LIMIT Clause

SELECT * FROM student_details
LIMIT 5;

#5. DISTINCT Clause

SELECT DISTINCT course
FROM student_details;

#6. ALIAS – Column Alias

SELECT student_name AS name, fees AS course_fees
FROM student_details;

#7. ALIAS – Table Alias

SELECT *
FROM student_details AS s;

#8. ORDER BY – Ascending Order

SELECT * FROM student_details
ORDER BY fees ASC;

#9. ORDER BY – Descending Order

SELECT * FROM student_details
ORDER BY fees DESC;

#10. WHERE with ORDER BY

SELECT * FROM student_details
WHERE age > 20
ORDER BY student_name ASC;

#11. WHERE with GROUP BY

SELECT course, COUNT(*)
FROM student_details
WHERE fees > 10000
GROUP BY course;

#12. GROUP BY with HAVING

SELECT course, COUNT(*)
FROM student_details
GROUP BY course
HAVING COUNT(*) > 1;

#13. GROUP BY with ORDER BY

SELECT course, COUNT(*)
FROM student_details
GROUP BY course
ORDER BY COUNT(*) DESC;

#14. GROUP BY with HAVING and ORDER BY

SELECT course, COUNT(*)
FROM student_details
GROUP BY course
HAVING COUNT(*) > 1
ORDER BY course ASC;

#15. WHERE with LIMIT

SELECT * FROM student_details
WHERE age > 20
LIMIT 5;

#16. DISTINCT with ORDER BY

SELECT DISTINCT course
FROM student_details
ORDER BY course ASC;

#17. WHERE with BETWEEN

SELECT * FROM student_details
WHERE age BETWEEN 20 AND 25;

#18. WHERE with LIKE

SELECT * FROM student_details
WHERE student_name LIKE 'A%';

#19. WHERE with IN

SELECT * FROM student_details
WHERE course IN ('Python', 'Java');

#20. WHERE with IS NULL

SELECT * FROM student_details
WHERE email IS NULL;