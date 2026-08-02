-- CREATE DATABASE retail_sales_analysis;
USE retail_sales_analysis;

CREATE TABLE orders (
    order_id VARCHAR(20),
    order_date DATE,
    ship_date DATE,
    ship_mode VARCHAR(50),
    customer_name VARCHAR(100),
    segment VARCHAR(50),
    state VARCHAR(100),
    country VARCHAR(100),
    market VARCHAR(50),
    region VARCHAR(50),
    product_id VARCHAR(20),
    category VARCHAR(50),
    sub_category VARCHAR(50),
    product_name VARCHAR(255),
    sales DECIMAL(10,2),
    quantity INT,
    discount DECIMAL(4,2),
    profit DECIMAL(10,2),
    shipping_cost DECIMAL(10,2),
    order_priority VARCHAR(20),
    year INT
);

-- KPI Queries
-- Total Revenue
SELECT SUM(sales) AS Total_Revenue
FROM orders;

-- Total Profit
SELECT SUM(profit) AS Total_Profit
FROM orders;

-- Total Orders
SELECT COUNT(order_id) AS Total_Orders
FROM orders;

-- Total Customers
SELECT COUNT(DISTINCT customer_name) AS Total_Customers
FROM orders;

-- Average Order Value
SELECT SUM(sales) / COUNT(order_id) AS Average_order_value
FROM orders;

-- Regional Analysis

-- Revenue by Region
SELECT region, SUM(sales) AS Revenue
FROM orders
GROUP BY region
ORDER BY Revenue DESC;

-- Profit by Region
SELECT region, SUM(profit) AS Profit
FROM orders
GROUP BY region
ORDER BY Profit DESC;

-- Orders by Region
SELECT region, COUNT(DISTINCT order_id) AS Orders
FROM orders
GROUP BY region
ORDER BY Orders DESC;

-- Profit Margin by Region
SELECT region, SUM(profit)/SUM(sales) AS Profit_Margin
FROM orders
GROUP BY region
ORDER BY Profit_Margin DESC;

-- Category Analysis
-- Revenue by Category
SELECT category, SUM(sales) AS Revenue
FROM orders
GROUP BY category
ORDER BY Revenue DESC;

-- Profit by Category
SELECT category, SUM(Profit) AS Profit
FROM orders
GROUP BY category
ORDER BY Profit DESC;

-- Revenue by Sub-Category
SELECT sub_category, SUM(sales) AS Revenue
FROM orders
GROUP BY sub_category
ORDER BY Revenue DESC;

-- Profit by Sub-Category
SELECT sub_category, SUM(profit) AS Profit
FROM orders
GROUP BY sub_category
ORDER BY Profit DESC;

-- Customer Analysis
-- Revenue by Segment
SELECT segment, SUM(sales) AS Revenue
FROM orders
GROUP BY segment
ORDER BY Revenue DESC;

-- Profit by Segment
SELECT segment, SUM(profit) AS profit
FROM orders
GROUP BY segment
ORDER BY profit DESC;

-- Top Customers by Revenue
SELECT customer_name, SUM(sales) AS revenue
FROM orders
GROUP BY customer_name
ORDER BY revenue DESC
LIMIT 10;

-- Time Analysis

-- Monthly Revenue
SELECT DATE_FORMAT(order_date, '%Y-%m') AS month, SUM(sales) AS Revenue
FROM orders
GROUP BY month
ORDER BY month;

-- Monthly Profit
SELECT DATE_FORMAT(order_date, '%Y-%m') AS month, SUM(profit) AS profit
FROM orders
GROUP BY month
ORDER BY month;

-- Yearly Revenue
SELECT year, SUM(sales) AS revenue
FROM orders
GROUP BY year
ORDER BY year;

-- Quarterly Revenue
SELECT year, QUARTER(order_date) AS quarter, SUM(sales) AS revenue
FROM orders
GROUP BY year, quarter
ORDER BY year, quarter;

-- Advanced SQL
-- CASE — categorize orders into profit tiers
SELECT order_id, profit,
	CASE
		WHEN profit < 0 THEN 'Loss'
        WHEN profit BETWEEN 0 AND 50 THEN 'Low Profit'
        ELSE 'High Profit'
	END AS 'Profit_Tier'
FROM orders;

-- CTE
-- Ranking Months by revenue
WITH monthly_revenue AS (
	SELECT DATE_FORMAT(order_date, '%Y-%m') AS month, SUM(sales) AS revenue
    FROM orders
    GROUP BY month
)
SELECT month, revenue,
	RANK() OVER (ORDER BY revenue DESC) AS Revenue_rank
FROM monthly_revenue
ORDER BY Revenue_rank;

-- ROW_NUMBER() vs RANK() vs DENSE_RANK()
-- rank sub-categories by profit within each category.
SELECT category, sub_category, profit,
       ROW_NUMBER() OVER (PARTITION BY category ORDER BY profit DESC) AS row_num,
       RANK()       OVER (PARTITION BY category ORDER BY profit DESC) AS rank_,
       DENSE_RANK() OVER (PARTITION BY category ORDER BY profit DESC) AS dense_rank_
FROM (
    SELECT category, sub_category, SUM(profit) AS profit
    FROM orders
    GROUP BY category, sub_category
) t;

-- LAG() / LEAD() — compare each month to the previous/next one

WITH monthly_revenue AS (
    SELECT DATE_FORMAT(order_date, '%Y-%m') AS month, SUM(sales) AS revenue
    FROM orders
    GROUP BY month
)
SELECT month, revenue,
       LAG(revenue) OVER (ORDER BY month) AS prev_month_revenue,
       revenue - LAG(revenue) OVER (ORDER BY month) AS revenue_change,
       LEAD(revenue) OVER (ORDER BY month) AS next_month_revenue
FROM monthly_revenue
ORDER BY month;

-- Running Total — cumulative revenue over time

WITH monthly_revenue AS (
    SELECT DATE_FORMAT(order_date, '%Y-%m') AS month, SUM(sales) AS revenue
    FROM orders
    GROUP BY month
)
SELECT month, revenue,
       SUM(revenue) OVER (ORDER BY month) AS running_total
FROM monthly_revenue
ORDER BY month;


	

        


