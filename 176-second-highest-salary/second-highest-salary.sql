# Write your MySQL query statement below
SELECT max(salary) AS SecondHighestSalary
FROM (
    SELECT salary, 
           ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
    FROM (SELECT DISTINCT salary FROM Employee) AS unique_salaries
) AS ranked
WHERE row_num = 2