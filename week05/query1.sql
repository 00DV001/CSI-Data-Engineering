CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    Age INT,
    Email NVARCHAR(100)
);

INSERT INTO Students (StudentID, FirstName, LastName, Age, Email)
VALUES 
(1, 'Riya', 'Mehta', 21, 'riya.mehta21@gmail.com'),
(2, 'Aditya', 'Sharma', 22, 'aditya.s@outlook.com'),
(3, 'Sneha', 'Iyer', 20, 'sneha.iyer93@yahoo.com'),
(4, 'Karan', 'Patel', 23, 'karan.patel11@hotmail.com'),
(5, 'Ananya', 'Roy', 19, 'ananya.roy27@gmail.com'),
(6, 'Vikram', 'Singh', 24, 'vikram.singh198@gmail.com'),
(7, 'Priya', 'Chopra', 20, 'priya.chopra99@rediffmail.com'),
(8, 'Neha', 'Kumar', 22, 'neha.kumar@protonmail.com'),
(9, 'Aman', 'Joshi', 21, 'amanj_1999@gmail.com'),
(10, 'Divya', 'Nair', 23, 'divya.nair@live.in');
