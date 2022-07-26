drop table if exists Users cascade;
/* contains all registered users */
create table Users (
	uid 	    integer primary key, /* see if this should be a string or bigint */
    username    varchar(50) NOT NULL
);
insert into Users values (1, 'test1'), (2, 'test2'), (262112498, 'weiquu'), (465678629, 'tanyaragu');

drop table if exists Unregistered cascade;
/* all users invited to a group but have not yet started the bot */
/* TODO: see if this is needed */
create table Unregistered (
    username    varchar(50) primary key
);

drop table if exists Groups cascade;
/* a group is a bunch of people who want to split their costs */
create table Groups (
    gid         serial primary key,
    groupname   varchar(50) NOT NULL, /* unique? */
    creator     integer references Users(uid) NOT NULL /* on delete cascade? */
);

drop table if exists Access cascade;
/* records which user has access to which group */
/* TODO: add in differing levels of permissions */
create table Access (
    uid         integer references Users(uid) NOT NULL, /* on delete cascade? */
    gid         integer references Groups(gid) NOT NULL, /* on delete cascade? */
    primary key (uid, gid)
);

drop table if exists Currencies cascade;
/* which currencies an expense can be recorded in */
create table Currencies (
    currency    varchar(50) primary key
);
insert into Currencies values ('SGD'), ('Euro');

drop table if exists Expenses cascade;
/* records all expenses */
create table Expenses (
    eid         serial primary key,
    gid         integer references Groups(gid) NOT NULL, /* on delete cascade? */
    uid         integer references Users(uid) NOT NULL, /* on delete cascade? represents who paid */
    cost        decimal(12, 2) NOT NULL,
    currency    varchar(50) NOT NULL references Currencies(currency), /* on delete cascade? */
    expDesc     varchar(50) NOT NULL,
    hasSplit    boolean NOT NULL DEFAULT false,
    datecreated timestamptz DEFAULT NOW()
);

drop table if exists Splits cascade;
/* contains who should be splitting payment for an expense */
create table Splits (
    eid         integer references Expenses(eid) NOT NULL,
    uid         integer references Users(uid) NOT NULL,
    primary key (eid, uid)
);