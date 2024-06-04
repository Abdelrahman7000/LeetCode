with cte as (
  SELECT ticker,max(open) highest_open
  from stock_prices
  GROUP BY 1
),

cte2 as (
  SELECT ticker, min(open) lowest_open
  from stock_prices
  GROUP BY 1
),
cte3 as (
  select cte.ticker,cte.highest_open,s.date highest_mth
  FROM cte 
  join stock_prices s
  on cte.highest_open=s .open
),

cte4 as (
  select cte2.ticker,cte2.lowest_open,s.date lowest_mth
  FROM cte2 
  join stock_prices s
  on cte2.lowest_open=s.open
)

SELECT cte3.ticker,
        replace(to_char(cte3.highest_mth,'Mon-YYYY'),' ','') highest_mth,
        cte3.highest_open,
        replace(to_char(cte4.lowest_mth,'Mon-YYYY'),' ','') lowest_mth,
        cte4.lowest_open
from cte3
join cte4
using (ticker)
ORDER BY 1
