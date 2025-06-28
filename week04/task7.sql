/* task7, https://www.hackerrank.com/challenges/the-report/problem?isFullScreen=true */
select if(grade<8,NULL,students.Name), grades.grade, students.Marks 
from students join grades 
on students.marks
between grades.min_mark and grades.max_mark 
order by grades.grade desc, students.name asc;