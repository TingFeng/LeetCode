/* 
LeetCode #180 - Database

Write a SQL query to find all numbers that appear at least three times consecutively.

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+

For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.

+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+

Solution:
distinct, where
hint:
can search between tables that are the same...
*/

select distinct l1.Num as ConsecutiveNums
from Logs as l1, Logs as l2, Logs as l3
where l1.Num=l2.Num and l1.Num=l3.Num and l1.ID+1=l2.ID and l2.ID+1=l3.ID
