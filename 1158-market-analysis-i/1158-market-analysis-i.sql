# Write your MySQL query statement below
with t as(
    select buyer_id,count(order_id) c
    from Orders o
    where year(o.order_date) in  (
                select year(Orders.order_date)
                from Orders
                where year(Orders.order_date)=2019
            )
    group by 1
)

select us.user_id buyer_id,us.join_date join_date, COALESCE(t.c, 0 ) orders_in_2019
from Users us
left join t on us.user_id=t.buyer_id

