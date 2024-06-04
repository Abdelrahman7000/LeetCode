<h2><a href="https://datalemur.com/questions/sql-bloomberg-stock-min-max-1">FAANG Stock Min-Max</a></h2><h3>Medium</h3><hr>
The Bloomberg terminal is the go-to resource for financial professionals, offering convenient access to a wide array of financial datasets. As a Data Analyst at Bloomberg, you have access to historical data on stock performance.

Currently, you're analyzing the highest and lowest open prices for each FAANG stock by month over the years.

For each FAANG stock, display the ticker symbol, the month and year ('Mon-YYYY') with the corresponding highest and lowest open prices (refer to the Example Output format). Ensure that the results are sorted by ticker symbol.

<p>Table: <code>stock_prices</code></p>
<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| date        | datetime|
| ticker      | varchar |
| open        | decimal |
| high        | decimal |
| low         | decimal |
| close       | decimal |
+-------------+---------+
</pre>
