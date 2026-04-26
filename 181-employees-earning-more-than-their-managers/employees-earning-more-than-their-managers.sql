# Write your MySQL query statement below
WITH non_managers as(
    SELECT * from Employee
    WHERE managerId is NOT NULL
),
managers as(
    SELECT * from Employee
    -- WHERE managerId is NULL
)


SELECT nm.name as  `Employee`
FROM non_managers nm
LEFT JOIN managers em on nm.managerId = em.id
WHERE nm.salary > em.salary