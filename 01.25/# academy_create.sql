drop database if exists academy;

create database academy;
use academy;


create table `faculties` (
	`id` tinyint unsigned not null auto_increment,
    `financing`  decimal(10,2) not null default 0,
	`name` varchar(100) not null unique,
    constraint `PK_id` primary key (`id`),
    constraint `CH_faculties_name` check (`name` <> '')
);


create table `departments` (
	`id` smallint unsigned not null auto_increment,
    `building` tinyint not null,
    `financing` decimal(10,2) not null default 0,
    `name` varchar(100) not null unique,
    `faculty_id` tinyint unsigned not null,
    constraint `PK_id` primary key (`id`),
    constraint `CH_departments_building` check (`building` between 1 and 5),
    constraint `CH_departments_financing` check (`financing` >= 0),
    constraint `CH_departments_name` check (`name` <> '')
);


create table `groups` (
	`id` mediumint unsigned not null auto_increment,
	`name` varchar(10) not null unique,
    `year` tinyint not null,
    `department_id` smallint unsigned not null,
    constraint `PK_id` primary key (`id`),
    constraint `CH_groups_name` check (`name` <> ''),
    constraint `CH_groups_year` check (`year` between 1 and 6)
);


create table `curators` (
	`id` mediumint unsigned not null auto_increment,
    `name` varchar(30) not null,
    `surname` varchar(30) not null,
    constraint `PK_id` primary key (`id`),
    constraint `CH_curators_name` check (`name` <> ''),
    constraint `CH_curators_surname` check (`surname` <> '')
);


create table `groups_curators` (
	`id` int unsigned not null auto_increment,
    `curator_id` mediumint unsigned not null,
    `group_id` mediumint unsigned not null,
    constraint `PK_id` primary key (`id`)
);


create table `teachers` (
	`id` smallint unsigned not null auto_increment,
    `name` varchar(30) not null,
    `surname` varchar(30) not null,
    `salary` decimal(8,2) not null,
    `is_professor` bit(1) not null default 0,
    constraint `PK_id` primary key (`id`),
    constraint `CH_teachers_name` check (`name` <> ''),
    constraint `CH_teachers_surname` check (`surname` <> ''),
    constraint `CH_teachers_salary` check (`salary` > 0)
);


create table `subjects` (
	`id` smallint unsigned not null auto_increment,
	`name` varchar(100) not null unique,
    constraint `PK_id` primary key (`id`),
    constraint `CH_subjects_name` check (`name` <> '')
);


create table `lectures` (
	`id` int unsigned not null auto_increment,
    `date` date not null,
    `subject_id` smallint unsigned not null,
    `teacher_id` smallint unsigned not null,
    constraint `PK_id` primary key (`id`)
);


create table `groups_lectures` (
	`id` int unsigned not null auto_increment,
    `lecture_id` int unsigned not null,
    `group_id` mediumint unsigned not null,
    constraint `PK_id` primary key (`id`)
);


create table `students` (
	`id` mediumint unsigned not null auto_increment,
    `name` varchar(30) not null,
    `surname` varchar(30) not null,
    `rating` tinyint not null,
    constraint `PK_id` primary key (`id`),
    constraint `CH_students_name` check (`name` <> ''),
    constraint `CH_students_surname` check (`surname` <> ''),
    constraint `CH_students_rating` check (`rating` between 0 and 5)
);


create table `groups_students` (
	`id` int unsigned not null auto_increment,
    `student_id` mediumint unsigned not null,
    `group_id` mediumint unsigned not null,
    constraint `PK_id` primary key (`id`)
);


alter table `departments` 
	add constraint `FK_departments_faculty_id` 
		foreign key (`faculty_id`) 
        references `faculties` (`id`);

alter table `groups` 
	add constraint `FK_groups_department_id` 
		foreign key (`department_id`) 
        references `departments` (`id`);

alter table `lectures` 
	add constraint `FK_lectures_subject_id` 
        foreign key (`subject_id`) 
        references `subjects` (`id`),
	add constraint `FK_lectures_teacher_id` 
        foreign key (`teacher_id`) 
        references `teachers` (`id`);

alter table `groups_curators` 
	add constraint `FK_groups_curators_curator_id` 
        foreign key (`curator_id`) 
        references `curators` (`id`),
	add constraint `FK_groups_curators_group_id` 
        foreign key (`group_id`) 
        references `groups` (`id`);

alter table `groups_lectures` 
	add constraint `FK_groups_lectures_lecture_id` 
        foreign key (`lecture_id`) 
        references `lectures` (`id`),
	add constraint `FK_groups_lectures_group_id` 
        foreign key (`group_id`) 
        references `groups` (`id`);

alter table `groups_students` 
	add constraint `FK_groups_students_student_id` 
        foreign key (`student_id`)
        references `students` (`id`),
	add constraint `FK_groups_students_group_id` 
        foreign key (`group_id`) 
        references `groups` (`id`);
