select count(*) from sales_data;
select* from sales_data;

#1 TO Know total orders and total quanity sold---:
select count(order_id) AS total_orders,
sum(quantity) AS total_quantity_sold
from sales_data;

#2 City with least quantity and least orders-----
select city,count(order_id) as total_orders,sum(Quantity) as total_qty
from sales_data
Group by city
order by total_orders asc
limit 1;

#3 Top 5 products by how much of Quantity sold-----
select Product_Name ,sum(Quantity) as total_sold_quantity
from sales_data
group by Product_Name
order by total_sold_quantity desc
limit 5 ;

#4 Total sales by months(jan-dec) in an year----

select month(Order_Date) as month_number,
monthname(order_date) as month_name,
sum(Quantity) as total_qty_sold,
sum(sales) as total_sales_amount,
count(order_id) as total_orders_recieved
from sales_data
group by month(order_date),monthname(order_date)
order by month_number;

# find top 10 cities who generate maximum revenue for superstore-----
select city,
round(sum(sales),2) as total_revenue,
sum(quantity) as total_qty_sold,
count(distinct Order_ID) as total_orders
from sales_data
group by city
order by total_revenue desc
limit 10;

#6Category wise revenue and profit from products-----
#which category (products) make more profit for supermart-----

select category,
round(sum(sales),2) as total_revenue,
round(sum(profit),2) as total_profit,
round(sum(profit)*100/sum(sales),2) as profit_margin,
count(distinct order_id) as total_orders
from sales_data
group by Category
order by total_profit desc;

#7 year by year company growth-----
select  
year(order_date) as sales_year,
round(sum(sales),2) as total_revenue,
round(sum(profit),2) as total_profit,
count(distinct order_id) as total_orders
from sales_data
group by year(Order_Date)
order by sales_year;

#8 which month got most profitable and generate more revenue for company----
#Monthly seasonlity analysis------

select 
monthname(order_date) as month_name,
month(order_date) as month_number,
round(sum(sales),2) as montly_revenue,
round(sum(profit),2) as montly_profit,
count(distinct order_id) as total_orders,
round(sum(profit) *100/sum(sales),2) as profit_margin
from sales_data
group by month_name,month_number
order by month_number;

# loss making product in company by category----

select Product_Name,
category,
round(sum(sales),2) as total_revenue,
round(sum(profit),2) as total_profit,
count(distinct order_id) as times_sold
from sales_data
group by product_name,Category
order by total_profit asc
limit 12;














































