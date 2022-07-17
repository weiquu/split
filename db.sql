drop table if exists Users cascade;

create table Users (
	uid 	integer primary key,
    name    varchar(50) NOT NULL
);