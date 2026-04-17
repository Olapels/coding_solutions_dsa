# Write your MySQL query statement below
SELECT e.name as name, b.bonus as bonus
from Employee e LEFT JOIN Bonus b USING(empId)
WHERE b.bonus IS NULL or b.bonus < 1000 
