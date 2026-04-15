# Online-Retail-Sales-Analysis-Database-virtusa-Assignment

## 1. Problem Statement
Retail businesses generate huge sales data but lack structured insights. Design a database and write SQL queries to analyze sales performance.

## 2. Objectives
- Create a relational database for an online store  
- Store customer, product, and order data  
- Extract meaningful insights using SQL queries  

## 3. Database Tables
### 3.1 Customers
- customer_id (Primary Key)  
- name  
- city
### 3.2 Products
- product_id (Primary Key)  
- name  
- category  
- price  
### 3.3 Orders
- order_id (Primary Key)  
- customer_id (Foreign Key)  
- order_date  
### 3.4 Order_Items
- order_id (Foreign Key)  
- product_id (Foreign Key)  
- quantity

## 4. Key Tasks Performed
### 4.1 Top-Selling Products
Calculated which products have the highest total quantity sold.
### 4.2 Most Valuable Customers
Identified customers who have spent the most based on total purchase value.
### 4.3 Monthly Revenue Calculation
Computed revenue generated per month using order date and product prices.
### 4.4 Category-wise Sales Analysis
Analyzed total sales for each product category to understand performance.
### 4.5 Detect Inactive Customers
Found customers who have not placed any orders.

## 5. Tools and Concepts Used

- sql (mysql or similar relational database)  
- Joins (inner join, left join)  
- Aggregate Functions (sum)  
- group by and order by  
- Date Functions (year, month)  
- Primary Key and Foreign Key relationships

## 6. Screenshots
### ER Diagram
![ER Diagram](ER%20diagram%20Online%20Retail%20Sales%20Analysis.png)
### Relationship Schema
![Relationship Schema](relationalship%20schema%20Online%20Retail%20Sales%20Analysis.png)



