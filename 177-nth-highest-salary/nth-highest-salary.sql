CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT MAX(salary) as getNthHighestSalary
      FROM(
        select salary,
        DENSE_RANK() OVER(ORDER BY salary DESC) as salary_rank
        From Employee
      ) as ranking_salary
      WHERE salary_rank = N

  );
END