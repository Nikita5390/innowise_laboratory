
--task1 Create tables
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    birth_year INT NOT NULL
);

CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
	student_id integer REFERENCES students (id),
    subject VARCHAR(255),
    grade INT CHECK (grade >= 1 AND grade <= 100)
);


--task2 Insert data
INSERT INTO students (full_name, birth_year)
VALUES
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006)

INSERT INTO grades (student_id, subject, grade)
VALUES
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),
(2, 'Math', 75),
(2, 'History', 83),
(2, 'English', 79),
(3, 'Science', 95),
(3, 'Math', 91),
(3, 'Art', 99),
(4, 'Math', 84),
(4, 'Science', 88),
(4, 'Physical Education', 93),
(5, 'English', 90),
(5, 'History', 85),
(5, 'Math', 88),
(6, 'Science', 72),
(6, 'Math', 78),
(6, 'English', 81),
(7, 'Art', 94),
(7, 'Science', 87),
(7, 'Math', 90),
(8, 'History', 77),
(8, 'Math', 83),
(8, 'Science', 80),
(9, 'English', 96),
(9, 'Math', 89),
(9, 'Art', 92)


--task3 Find all grades for specific student Alice Johnson
SELECT students.full_name, grades.grade
FROM grades
JOIN students ON students.id = grades.student_id
WHERE students.full_name = 'Alice Johnson'


--task4 Calculate the average grade per student
SELECT students.full_name, AVG(grades.grade)
FROM grades
JOIN students ON students.id = grades.student_id
GROUP BY students.full_name;


--task5 List all student born after 2004
SELECT full_name FROM students
WHERE birth_year > 2004;


--task6 Create a query that list all subjects and their avg grades
SELECT subject, AVG(grade) FROM grades
GROUP BY subject;


--task7 Find the top 3 students with the highest avg grades
SELECT students.full_name, AVG(grades.grade)
FROM grades
JOIN students ON students.id = grades.student_id
GROUP BY students.full_name
ORDER BY AVG(grades.grade) DESC LIMIT 3;


--task8 Show all students, who have scored bellow 80 and any subject
SELECT students.full_name, grades.subject, grades.grade
FROM grades
JOIN students ON students.id = grades.student_id
WHERE grades.grade < 80;