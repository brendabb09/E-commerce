
create database escola_db;
 use escola_db;

create table aluno(
id_aluno int auto_increment not null primary key,
nome_aluno varchar (20) not null,
idade_aluno varchar (20) not null);

insert into aluno (nome_aluno,idade_aluno) values ('Brenda barroso',20);


create table professor(
id_professor int auto_increment not null primary key,
nome_professor varchar (20) not null,
materia_professor varchar (30) not null);


insert into professor (nome_professor,materia_professor) values ('helio','programacao de sistemas');

create table curso(
id_curso int auto_increment not null primary key,
nome_curso varchar (30) not null,
carga_horaria int not null);

insert into curso (nome_curso,carga_horaria) values ('programacao de sistemas',200);

create table matricula(
id_matricula int auto_increment not null primary key,
id_alunofk int not null,
id_professorfk int not null,
id_cursofk  int not null,
foreign key(id_alunofk) references aluno(id_aluno),
foreign key(id_professorfk) references professor(id_professor),
foreign key(id_cursofk) references curso(id_curso));



