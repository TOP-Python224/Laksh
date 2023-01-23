drop database if exists academy;

create database if not exists academy;
use academy;

create table if not exists `Curators` (
	`id` mediumint unsigned not null auto_increment,
    `Name` varchar(30) not null,
    `Surname` varchar(30) not null,
    constraint `PK_id` primary key(`id`)
);
alter table `Curators`
	add constraint `CH_Curators_Name` check (`Name` <> ''),
    add constraint `CH_Curators_Surname` check (`Surname` <> '');

create table if not exists `Departments` (
	`id` smallint unsigned not null auto_increment,
    `Building` tinyint not null,
    `Financing` decimal(10,2) not null default 0,
    `Name` varchar(100) not null unique,
    `FacultyId` tinyint unsigned not null,
    constraint `PK_id` primary key(`id`),
    constraint `CH_Departments_Building` check (`Building` between 1 and 5),
    constraint `CH_Departments_Financing` check (`Financing` >= 0),
    constraint `CH_Departments_Name` check (`Name` <> '')
);

create table if not exists `Faculties` (
	`id` tinyint unsigned not null auto_increment,
	`Name` varchar(100) not null unique,
    constraint `PK_id` primary key(`id`),
    constraint `CH_Faculties_Name` check (`Name` <> '')
);

create table if not exists `Groups` (
	`id` mediumint unsigned not null auto_increment,
	`Name` varchar(10) not null unique,
    `Year` tinyint not null,
    `DepartmentId` smallint unsigned not null,
    constraint `PK_id` primary key(`id`),
    constraint `CH_Groups_Name` check (`Name` <> ''),
    constraint `CH_Groups_Year` check (`Year` between 1 and 6)
);

create table if not exists `GroupsCurators` (
	`id` int unsigned not null auto_increment,
    `CuratorId` mediumint unsigned not null,
    `GroupId` mediumint unsigned not null,
    constraint `PK_id` primary key(`id`)
);

create table if not exists `GroupsLectures` (
	`id` int unsigned not null auto_increment,
    `LectureId` int unsigned not null,
    `GroupId` mediumint unsigned not null,
    constraint `PK_id` primary key(`id`)
);

create table if not exists `GroupsStudents` (
	`id` int unsigned not null auto_increment,
    `StudentId` mediumint unsigned not null,
    `GroupId` mediumint unsigned not null,
    constraint `PK_id` primary key(`id`)
);

create table if not exists `Lectures` (
	`id` int unsigned not null auto_increment,
    `Date` date not null,
    `SubjectId` smallint unsigned not null,
    `TeacherId` smallint unsigned not null,
    constraint `PK_id` primary key(`id`)
);

create table if not exists `Students` (
	`id` mediumint unsigned not null auto_increment,
    `Name` varchar(30) not null,
    `Surname` varchar(30) not null,
    `Rating` tinyint not null,
    constraint `PK_id` primary key(`id`),
    constraint `CH_Students_Name` check (`Name` <> ''),
    constraint `CH_Students_Surname` check (`Surname` <> ''),
    constraint `CH_Students_Rating` check (`Rating` between 0 and 5)
);

create table if not exists `Subjects` (
	`id` smallint unsigned not null auto_increment,
	`Name` varchar(100) not null unique,
    constraint `PK_id` primary key(`id`),
    constraint `CH_Subjects_Name` check (`Name` <> '')
);

create table if not exists `Teachers` (
	`id` smallint unsigned not null auto_increment,
    `Name` varchar(30) not null,
    `Surname` varchar(30) not null,
    `Salary` decimal(8,2) not null,
    `IsProfessor` bit(1) not null default 0,
    constraint `PK_id` primary key(`id`),
    constraint `CH_Teachers_Name` check (`Name` <> ''),
    constraint `CH_Teachers_Surname` check (`Surname` <> ''),
    constraint `CH_Teachers_Salary` check (`Salary` > 0)
);

alter table `Departments` 
	add constraint `FK_Departments_FacultyId` 
		foreign key(`FacultyId`) 
        references `Faculties`(`id`);

alter table `Groups` 
	add constraint `FK_Groups_DepartmentId` 
		foreign key(`DepartmentId`) 
        references `Departments`(`id`);

alter table `GroupsCurators` 
	add constraint `FK_GroupsCurators_CuratorId` 
        foreign key(`CuratorId`) 
        references `Curators`(`id`),
	add constraint `FK_GroupsCurators_GroupId` 
        foreign key(`GroupId`) 
        references `Groups`(`id`);

alter table `GroupsLectures` 
	add constraint `FK_GroupsLectures_LectureId` 
        foreign key(`LectureId`) 
        references `Lectures`(`id`),
	add constraint `FK_GroupsLectures_GroupId` 
        foreign key(`GroupId`) 
        references `Groups`(`id`);

alter table `GroupsStudents` 
	add constraint `FK_GroupsStudents_StudentId` 
        foreign key(`StudentId`)
        references `Students`(`id`),
	add constraint `FK_GroupsStudents_GroupId` 
        foreign key(`GroupId`) 
        references `Groups`(`id`);

alter table `Lectures` 
	add constraint `FK_Lectures_SubjectId` 
        foreign key(`SubjectId`) 
        references `Subjects`(`id`),
	add constraint `FK_Lectures_TeacherId` 
        foreign key(`TeacherId`) 
        references `Teachers`(`id`);
