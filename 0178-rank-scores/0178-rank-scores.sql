# Write your MySQL query statement below
select score,
        DENSE_RANK() over(order by score desc) "rank" 
from Scores