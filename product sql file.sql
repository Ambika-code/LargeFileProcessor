show databases;
create database productsdata;
use product10;
create table products(name varchar(20),sku varchar(100),description varchar(100));
select name,count(name) from products group by name;