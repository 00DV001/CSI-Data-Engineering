CREATE TABLE Teachers (
    TeacherID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Subject VARCHAR(100),
    Email VARCHAR(100),
    ExperienceYears INT
);

INSERT INTO Teachers (TeacherID, FirstName, LastName, Subject, Email, ExperienceYears) VALUES
(1, 'Anil', 'Sharma', 'Mathematics', 'anil.sharma@school.edu', 10),
(2, 'Meera', 'Nair', 'Physics', 'meera.nair@school.edu', 8),
(3, 'Rajiv', 'Kohli', 'Chemistry', 'rajiv.kohli@school.edu', 12),
(4, 'Sonal', 'Kapoor', 'Biology', 'sonal.kapoor@school.edu', 7),
(5, 'Deepak', 'Verma', 'Computer Science', 'deepak.verma@school.edu', 9),
(6, 'Kavita', 'Deshmukh', 'English', 'kavita.d@school.edu', 11),
(7, 'Amit', 'Joshi', 'History', 'amit.joshi@school.edu', 6);
