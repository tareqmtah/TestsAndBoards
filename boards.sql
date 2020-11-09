CREATE TABLE `boards` (BoardName varchar(255),Memory integer,OS varchar(255),OSVerMajor integer,OSVerMinor integer,Hwtype varchar(255),PeriphA integer,PeriphB integer,InUse integer);
INSERT INTO `boards` VALUES('Toto',512,'Linux',4,1,'x4000',1,1,0);
INSERT INTO `boards` VALUES('GoodLuck',512,'Linux',4,0,'x4000',1,1,1);
INSERT INTO `boards` VALUES('Badger',512,'Linux',4,1,'x4000',1,1,1);
INSERT INTO `boards` VALUES('Weasel',32768,'Linux',3,18,'P/R-4',1,1,0);
INSERT INTO `boards` VALUES('SmallButGood',512,'Linux',3,17,'P/R-4',1,1,0);
INSERT INTO `boards` VALUES('Fred',1024,'Android',5,0,'x4000',1,1,0);
INSERT INTO `boards` VALUES('Ash',256,'Windows',10,0,'STD/01:2',0,0,0);
INSERT INTO `boards` VALUES('Cam1',512,'Linux',3,18,'x4001',0,0,0);
