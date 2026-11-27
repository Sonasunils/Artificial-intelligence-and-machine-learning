#1. AND Operator

SELECT * FROM student_details
WHERE age > 20 AND fees > 15000;

#2. OR Operator

SELECT * FROM student_details
WHERE course = 'Python' OR course = 'Java';

#3. NOT Operator

SELECT * FROM student_details
WHERE NOT course = 'Python';

#4. IN Operator

SELECT * FROM student_details
WHERE course IN ('Python', 'Java');

#5. NOT IN Operator

SELECT * FROM student_details
WHERE course NOT IN ('Python', 'Java');

#6. LIKE Operator – Starts with A

SELECT * FROM student_details
WHERE student_name LIKE 'A%';

#7. LIKE Operator – Ends with a

SELECT * FROM student_details
WHERE student_name LIKE '%a';

#8. LIKE Operator – Contains the letter a

SELECT * FROM student_details
WHERE student_name LIKE '%a%';

#9. LIKE Operator – Second character is n

SELECT * FROM student_details
WHERE student_name LIKE '_n%';

#10. BETWEEN Operator

SELECT * FROM student_details
WHERE age BETWEEN 20 AND 25;

#11. NOT BETWEEN Operator

SELECT * FROM student_details
WHERE age NOT BETWEEN 20 AND 25;

#12. AND with BETWEEN Operator

SELECT * FROM student_details
WHERE age BETWEEN 20 AND 25
AND fees > 10000;

#13. OR with IN Operator

SELECT * FROM student_details
WHERE course IN ('Python', 'Java')
OR age = 24;

#14. NOT with IN Operator

SELECT * FROM student_details
WHERE course NOT IN ('Python', 'Java');

#15. AND with LIKE Operator

SELECT * FROM student_details
WHERE student_name LIKE 'A%'
AND age > 20;

#16. OR with LIKE Operator

SELECT * FROM student_details
WHERE student_name LIKE 'A%'
OR student_name LIKE 'M%';