INSERT INTO `Curators` (`Name`,`Surname`)
VALUES
  ("Maile","Benjamin"),
  ("Denton","John"),
  ("Ray","Yoko"),
  ("Wesley","Jonas"),
  ("Eleanor","Brianna"),
  ("Xanthus","Kelsie"),
  ("Dante","Zahir"),
  ("Lyle","Nash"),
  ("Erasmus","Reuben"),
  ("Whitney","Howard"),
  ("Laith","Wyoming"),
  ("Karen","George"),
  ("Iris","Porter");

INSERT INTO `Faculties`(`Name`)
VALUES
  ('History'),
  ('Faculty of Arts'),
  ('Faculty of Classics'),
  ('Faculty of Commerce'),
  ('Faculty of Economics'),
  ('Faculty of Education'),
  ('Faculty of Engineering'), 
  ('Faculty of Graduate Studies'),
  ('Faculty of Humanities'),
  ('Faculty of Political Science'),
  ('Faculty of Natural Sciences'),
  ('Faculty of Information Technology');

INSERT INTO `Students` (`Name`,`Surname`,`Rating`)
VALUES
  ("Kieran","Yoko",1),
  ("Calista","Ava",3),
  ("Laith","Wyoming",4),
  ("Karen","George",3),
  ("Jordan","Lucas",0),
  ("Neville","Garrett",3),
  ("Scarlett","Ezra",2),
  ("Uriah","Shay",1),
  ("Keiko","Keaton",4),
  ("Aspen","Allistair",4),
  ("Jack","Perry",2),
  ("Alden","Fuller",4),
  ("Aileen","Nayda",0),
  ("Madison","Bethany",1),
  ("Daphne","Camilla",3),
  ("Rhea","Ifeoma",1),
  ("Andrew","Amir",2),
  ("Roth","Curran",0),
  ("Nasim","Hyacinth",4),
  ("Iris","Porter",1);
  
           
INSERT INTO `Subjects`(`Name`)
VALUES
  ("Accounting & Finance"),
  ("Art & Design"),
  ("Architecture"),
  ("Mechanical, Aeronautical & Manufacturing Engineering"),
  ("Law"),
  ("Economics & Econometrics"),
  ("Business & Management Studies"),
  ("Computer Science & Information Systems"),
  ("Engineering & Technology"),
  ("Geography"),
  ("Marketing"),
  ("Medicine");

INSERT INTO `Teachers` (`Name`,`Surname`,`Salary`,`IsProfessor`)
VALUES
  ("Daphne","Camilla",72170,1),
  ("Rhea","Ifeoma",101459,0),
  ("Andrew","Amir",140046,0),
  ("Roth","Curran",144109,0),
  ("Nasim","Hyacinth",88804,1),
  ("Adrienne","Bruce",70337,0),
  ("Quin","Price",90889,1),
  ("Kyle","Gillian",73858,0),
  ("Tarik","Uriel",108274,1),
  ("Quintessa","Curran",140193,0),
  ("Ocean","Josiah",128546,1),
  ("Neil","Burton",137915,0),
  ("Reed","Jasper",131416,0),
  ("Desiree","Farrah",129999,0),
  ("Damon","Vivian",113730,1),
  ("Ayanna","Rooney",64277,0),
  ("Hoyt","Bruno",77606,1),
  ("Whilemina","Amelia",128811,1),
  ("Samantha","Indigo",119626,0),
  ("Jesse","Tyler",130383,0),
  ("Walker","Sylvia",146831,0),
  ("Adrian","Dane",88686,0),
  ("Gemma","Emi",65810,0),
  ("Madonna","Ignacia",70529,1);

 INSERT INTO `Lectures` (`Date`,`SubjectId`,`TeacherId`)
VALUES
  ("21-12-30",10,19),
  ("22-03-18",9,18),
  ("23-01-20",12,22),
  ("23-03-18",1,23),
  ("22-01-08",2,20),
  ("23-08-24",6,16),
  ("22-08-23",8,7),
  ("23-05-03",8,3),
  ("23-09-28",5,13),
  ("22-12-05",3,17),
  ("23-07-04",12,15),
  ("23-07-04",4,12),
  ("23-03-14",7,11),
  ("22-11-15",6,10),
  ("21-11-21",2,9),
  ("23-01-01",1,8),
  ("21-11-24",6,5),
  ("21-12-12",7,7),
  ("23-01-10",9,3),
  ("22-09-08",10,11);


INSERT INTO `Departments` (`Building`,`Financing`,`Name`,`FacultyId`)
VALUES
  (3,859821,"Massa Quisque Ltd",2),
  (4,854702,"Nunc Quisque Ornare Consulting",1),
  (4,837514,"Cras Corporation",1),
  (2,969338,"Dolor Corp.",10),
  (3,765863,"Aliquam Tincidunt Nunc LLP",10),
  (5,658429,"Nulla Aliquet Institute",1),
  (5,887093,"In Ornare Sagittis Corporation",4),
  (3,758575,"Auctor LLC",4),
  (4,953176,"Magna Ut Limited",2),
  (1,619803,"In Molestie Tortor Inc",4);


INSERT INTO `Groups` (`Name`,`Year`,`DepartmentId`)
VALUES
  ("Python115",1,4),
  ("C++11",2,9),
  ("C#02",5,4),
  ("JS55",1,6),
  ("Java14",5,3),
  ("Java48",4,7),
  ("Html55",5,5),
  ("C#987",2,8),
  ("C++756",3,3),
  ("PHP363",1,5),
  ("PHP014",4,7),
  ("GO14",5,5),
  ("Kotlin47",2,8),
  ("Java28",3,5),
  ("Kotlin89",1,5),
  ("Python147",3,3),
  ("C#654",2,2),
  ("1c915",1,3),
  ("1c177",2,1),
  ("Pascal15",3,2),
  ("JS44",4,9),
  ("Html069",1,7),
  ("C++5",6,8),
  ("Pascal16",5,1),
  ("JS68",5,10),
  ("Go9",5,10),
  ("Python08",3,4),
  ("JS33",6,5),
  ("Mysql102",2,8),
  ("Html13",5,2);



INSERT INTO `GroupsLectures` (`LectureId`,`GroupId`)
VALUES
  (13,21),
  (16,17),
  (10,29),
  (10,26),
  (5,11),
  (11,16),
  (7,7),
  (15,25),
  (4,28),
  (8,19),
  (18,9),
  (11,10),
  (1,19),
  (5,12),
  (4,18),
  (6,16),
  (6,17),
  (8,20),
  (12,5),
  (19,28);

INSERT INTO `GroupsStudents` (`StudentId`,`GroupId`)
VALUES
  (3,17),
  (16,16),
  (5,28),
  (4,20),
  (7,5),
  (10,11),
  (3,6),
  (18,25),
  (5,18),
  (17,12),
  (7,1),
  (14,17),
  (15,7),
  (19,14),
  (3,21),
  (10,15),
  (17,5),
  (6,10),
  (18,27),
  (16,6);
  
INSERT INTO `GroupsCurators` (`CuratorId`,`GroupId`)
VALUES
  (9,8),
  (1,6),
  (6,19),
  (5,5),
  (7,22),
  (4,17),
  (2,26),
  (3,10),
  (11,23),
  (8,16),
  (10,4),
  (10,11);

