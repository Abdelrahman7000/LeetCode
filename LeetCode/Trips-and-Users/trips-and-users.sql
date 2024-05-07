with banned as(
    select users_id
    from Users u
    where u.banned= 'Yes'
),
total as (
    select request_at,count(id)::decimal count
    from Trips t
    where t.client_id not in (select * from banned)
        and t.driver_id not in(select * from banned)
        and (request_at >='2013-10-01' and request_at <= '2013-10-03')
    group by 1
),
cancel as (
    select t.request_at,
            count(t.id)::decimal counter
    from Trips t
    where t.client_id not in (select * from banned)
        and t.driver_id not in(select * from banned)
        and (t.status = 'cancelled_by_driver' or
             t.status= 'cancelled_by_client') 
        and (t.request_at >='2013-10-01' and t.request_at <= '2013-10-03')
    group by 1    
)

  
select t.request_at "Day", 
    case when round(c.counter/t.count,2) is null then 0
        else  round(c.counter/t.count,2)
        end as "Cancellation Rate"
from total t
left join cancel c
on t.request_at=c.request_at
order by 1
