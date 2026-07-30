# Write your MySQL query statement below
SELECT E.employee_id,E.name, COUNT(Em.reports_to) AS reports_count , ROUND(AVG(Em.age)) AS average_age
FROM Employees E
JOIN Employees Em
ON E.employee_id = Em.reports_to
GROUP BY E.employee_id
ORDER BY E.Employee_id;