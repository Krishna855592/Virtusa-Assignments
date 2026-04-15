CREATE DATABASE Online_Retail_Sales_Analysis_Database;
-- using the database

USE Online_Retail_Sales_Analysis_Database;

-- creating the customer table
create table customers(
	customer_id int primary key,
    name varchar(50),
    city varchar(50)
);

-- creating products table
create table Products(
	product_id int primary key,
    name varchar(50),
    category varchar(50),
    price decimal(10,2)
);

-- creating orders table
create table Orders(
	order_id int primary key,
    customer_id int,
    order_date date,
    foreign key(customer_id) references customers(customer_id)
);

-- creating order items table
create table order_items(
	order_id int,
    product_id int,
    quantity int,
    primary key(order_id,product_id),
    foreign key(order_id) references orders(order_id),
    foreign key(product_id) references products(product_id)
);

-- inserting some data into tables
insert into customers values
(1,'Ravi Kumar','Hyderabad'),
(2,'Sneha Reddy','Bangalore'),
(3,'Amit Sharma','Delhi'),
(4,'Priya Singh','Mumbai'),
(5,'Krishna Rao','Chennai');

insert into products values
(101,'Laptop','Electonics',55000.00),
(102,'Mobile','Electonics',20000.00),
(103,'Headphones','Accessories',2000.00),
(104,'Chair','Furniture',5000.00),
(105,'Table','Furniture',7000.00);

-- one customer can have multiple orders
insert into orders values
(1001,1,'2024-01-10'),
(1002,2,'2024-01-15'),
(1003,1,'2024-02-05'),
(1004,3,'2024-02-20'),
(1005,4,'2024-03-01');

insert into order_items values
(1001, 101, 1),
(1001, 103, 2),
(1002, 102, 1),
(1003, 104, 1),
(1003, 105, 1),
(1004, 101, 1),
(1005, 103, 3);

-- Now Performing the key tasks stated in the assignment

-- 1 find the top selling product  (using inner join concept)
select  
	p.product_id,p.name,sum(oi.quantity) as total_sold
    from  order_items oi join products p
    on oi.product_id=p.product_id
    group by p.product_id,p.name
    order by total_sold desc;
    
-- 2 identify most valuable customers   (Customers who spent the most money are treated as valuable customers)
select
	c.customer_id,c.name,
    sum(oi.quantity*p.price) as total_spent
	from customers c join orders o 
    on c.customer_id=o.customer_id
    join order_items oi 
    on o.order_id=oi.order_id
    join products p
    on oi.product_id=p.product_id
    group by c.customer_id,c.name
    order by total_spent desc;
    
-- 3 Monthly Revenue Calculation   (By separating date by month and year we can calculate montly revenue)
select
	year(o.order_date) as year,
    month(o.order_date) as month,
    sum(oi.quantity*p.price) as monthly_revenue
    from orders o join order_items oi
    on o.order_id=oi.order_id
    join products p
    on oi.product_id=p.product_id
    group by year(o.order_date),month(o.order_date)
    order by year,month;
    
-- 4 category-wise sales analysis    
select 
	p.category,
    sum(oi.quantity*p.price) as total_sales
    from order_items oi join products p
    on oi.product_id=p.product_id
    group by p.category
    order by total_sales desc;
    
    
-- 5 Detect inactive customers   (using the left join concept)
select
	c.customer_id,c.name
    from customers c left join orders o
    on c.customer_id=o.customer_id
    where o.order_id is null;

    
    
    

-- printing all tables
SELECT * FROM Customers;
SELECT * FROM Products;
SELECT * FROM Orders;
SELECT * FROM Order_Items;








































