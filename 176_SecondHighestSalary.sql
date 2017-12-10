/*
LeetCode Problem #176 - Database

Write a SQL query to get the second highest salary from the Employee table.

Employee
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

For example, given the above Employee table, the query should return 200 as the second highest salary. 
If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+


Solution:
Distinct
Limit
Offset
subquery or ifnull

*/


Select 
  (
    select salary from Employee
    order by salary DESC
    limit 1 offset 1
  ) as SecondHighestSalary
  
  
  /* or the ifnull solution
  
  select
    ifnull(
      (
      select salary from Employee
      order by salary DESC
      limit 1 offset 1
      ), Null
      ) as SecondHighestSalary
