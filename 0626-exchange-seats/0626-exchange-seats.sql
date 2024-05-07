# Write your MySQL query statement below
select id,
    case 
        when id %2=1 then lead(student,1,student) over(order by id)
        else lag(student) over(order by id)
    end as student
from Seat;