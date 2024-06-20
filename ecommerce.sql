create database ecommerce_db;

use ecommerce_db;


create table produtos(
id int auto_increment primary key,
nome varchar (255) not null,
preco decimal (10,2) not null,
descricao text,
estoque int

);



create table usuario(
id int auto_increment primary key,
nome varchar (255) not null,
telefone decimal (12,2) not null

);

use ecommerce_db;
select*from produtos;

