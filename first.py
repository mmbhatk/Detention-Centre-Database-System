import sqlite3
con = sqlite3.connect("FrostgateDetentionCenter.db")

crsr = con.cursor()

com = """CREATE TABLE Officer (    
fname VARCHAR(20),  
lname VARCHAR(30),
OID CHAR(10) PRIMARY KEY,
title VARCHAR(10),
phone INTEGER,
salary FLOAT,
uname CHAR(10),
password CHAR(10));"""
crsr.execute(com)

com = """INSERT INTO Officer VALUES ('HOLLIS','DOYLE','1234567890','ASSISTANT',444555, 30000,'abcdefghij','0000000000')"""
crsr.execute(com)

com = """INSERT INTO Officer VALUES ('BENNETT','COLE','1111111111','ASSOCIATE',444333, 40000,'1234WERSQW','9999999999')"""
crsr.execute(com)

com = """INSERT INTO Officer VALUES ('JAMES','POIROT','2222233333','CHIEF',456473, 50000,'GHTWY99999','8888888888')"""
crsr.execute(com)


#com = """SELECT * FROM Officer"""
#crsr.execute(com)
#ans = crsr.fetchall()
#for i in ans:
#    print(i)


com = """CREATE TABLE Warden (    
name VARCHAR(20),    
WID CHAR(10) PRIMARY KEY,
salary FLOAT,
OID CHAR(10) REFERENCES Officer(OID));"""
crsr.execute(com)

com = """INSERT INTO Warden VALUES ('JOHN SMITH','4444444444',5500,'2222222222')"""
crsr.execute(com)

com = """INSERT INTO Warden VALUES ('JANE DIAS','5673982349',7500,'1234567890')"""
crsr.execute(com)

com = """INSERT INTO Warden VALUES ('PABLO NAZLO','9834782310',9500,'1111111111')"""
crsr.execute(com)

com = """INSERT INTO Warden VALUES ('JOHN SMITH','4444489023',3500,'2222233333')"""
crsr.execute(com)

#com = """SELECT * FROM Warden"""
#crsr.execute(com)
#ans = crsr.fetchall()
#for i in ans:
#    print(i)

com = """CREATE TABLE Section (
name VARCHAR(20),
SID CHAR(10) PRIMARY KEY,
WID CHAR(10) REFERENCES Warden(WID));"""
crsr.execute(com)

com = """INSERT INTO Section VALUES ('A','A_Section_','4444444444')"""
crsr.execute(com)

com = """INSERT INTO Section VALUES ('B','B_Section_','5673982349')"""
crsr.execute(com)

com = """INSERT INTO Section VALUES ('C','C_Section_','9834782310')"""
crsr.execute(com)

com = """INSERT INTO Section VALUES ('D','D_Section_','4444489023')"""
crsr.execute(com)

#com = """SELECT * FROM Section"""
#crsr.execute(com)
#ans = crsr.fetchall()
#for i in ans:
#    print(i)

#com = """DROP TABLE Section_BACKUP"""
#crsr.execute(com)

#com = """DROP TABLE CELL"""
#crsr.execute(com)

com = """CREATE TABLE CELL (    
cell_id VARCHAR(10) PRIMARY KEY,    
cellLoc VARCHAR(20),
noPrisoners INTEGER,
SID CHAR(10) REFERENCES Section(SID)
);"""
crsr.execute(com)


com = """INSERT INTO CELL VALUES ('QQ','NORTH',1,'4444444444');"""
crsr.execute(com)

com = """INSERT INTO CELL VALUES ('AA','NORTH',1,'4444444444');"""
crsr.execute(com)

com = """INSERT INTO CELL VALUES ('BB','EAST',1,'5673982349');"""
crsr.execute(com)

com = """INSERT INTO CELL VALUES ('CC','EAST',1,'5673982349');"""
crsr.execute(com)

com = """INSERT INTO CELL VALUES ('MM','WEST',1,'9834782310');"""
crsr.execute(com)

com = """INSERT INTO CELL VALUES ('HH','WEST',1,'9834782310');"""
crsr.execute(com)

com = """INSERT INTO CELL VALUES ('II','SOUTH',1,'4444489023');"""
crsr.execute(com)

com = """INSERT INTO CELL VALUES ('JJ','SOUTH',1,'4444489023');"""
crsr.execute(com)

#com = """SELECT * FROM CELL"""
#crsr.execute(com)
#ans = crsr.fetchall()
#for i in ans:
#    print(i)

com = """CREATE TABLE CASES (    
case_id VARCHAR(10) PRIMARY KEY,    
caseName VARCHAR(20),
caseType VARCHAR(20),
year INTEGER
);"""
crsr.execute(com)

com = """INSERT INTO CASES VALUES ('0','A vs B', 'INSURANCE FRAUD', 2010)"""
crsr.execute(com)

com = """INSERT INTO CASES VALUES ('1','C vs D', 'MURDER', 2009)"""
crsr.execute(com)

com = """INSERT INTO CASES VALUES ('2','E vs F', 'THEFT', 2017)"""
crsr.execute(com)

com = """INSERT INTO CASES VALUES ('3','G vs H', 'ARSON', 2014)"""
crsr.execute(com)

com = """INSERT INTO CASES VALUES ('4','J vs I', 'RAPE', 2016)"""
crsr.execute(com)

#com = """SELECT * FROM CASES"""
#crsr.execute(com)
#ans = crsr.fetchall()
#for i in ans:
#    print(i)

#com = """DROP TABLE PRISONER"""
#crsr.execute(com)

com = """CREATE TABLE PRISONER (    
PID VARCHAR(10) PRIMARY KEY,
fname VARCHAR(20),
lname VARCHAR(30),
addr VARCHAR(30),
category VARCHAR(20),
date_of_in DATE,
date_of_out DATE,
gender VARCHAR,
salary FLOAT,
cell_id CHAR(10) REFERENCES CELL(cell_id),
SID CHAR(10) REFERENCES Section(SID),
case_id CHAR(10) REFERENCES CASES(case_id)
);"""
crsr.execute(com)

com = """INSERT INTO PRISONER VALUES ('P0','VARSHA','M','221, CLOVERFIELD LANE','FIRST DEGREE','2000-01-23','2017-01-23','FEMALE',6000,'QQ','A_Section_','1');"""
crsr.execute(com)

com = """INSERT INTO PRISONER VALUES ('P1','PRATIKSHA','P','TIMES SQUARE, NY','SECOND DEGREE','1998-03-20','2017-03-23','FEMALE',9000,'JJ','B_Section_','0');"""
crsr.execute(com)

com = """INSERT INTO PRISONER VALUES ('P2','HARMFUL','HARRY','34, AVENUE BOULEVARD','THIRD DEGREE','2001-02-30','2015-03-17','MALE',4000,'AA','A_Section_','2');"""
crsr.execute(com)

com = """INSERT INTO PRISONER VALUES ('P3','HARMLESS','INTRUDER','89, LINKIN STREET','FIRST DEGREE','2002-07-30','2018-10-31','FEMALE',8000,'BB','C_Section_','3');"""
crsr.execute(com)

com = """INSERT INTO PRISONER VALUES ('P4','BELLA','SWAN','100, FORKS, SEATTLE','FIRST DEGREE','1997-04-19','2018-10-11','FEMALE',3000,'II','B_Section_','4');"""
crsr.execute(com)

com = """INSERT INTO PRISONER VALUES ('P5','JENKIN','JACOB','20, POWERHOUSE LANE','SECOND DEGREE','1980-05-19','2014-11-09','MALE',6000,'CC','C_Section_','0');"""
crsr.execute(com)

com = """INSERT INTO PRISONER VALUES ('P6','URSULA','BUFFAY','17, MANSFIELD PARK','THIRD DEGREE','1988-09-29','2012-11-10','FEMALE',2000,'MM','D_Section_','2');"""
crsr.execute(com)

com = """INSERT INTO PRISONER VALUES ('P7','RACHEL','GREENE','10, FRONTING LANE','SECOND DEGREE','1978-12-31','2014-12-31','NONE',2000,'HH','D_Section_','3');"""
crsr.execute(com)

#com = """SELECT * FROM PRISONER"""
#crsr.execute(com)
#ans = crsr.fetchall()
#for i in ans:
#    print(i)


#com = """DROP TABLE VISITOR"""
#crsr.execute(com)

com = """CREATE TABLE VISITOR (    
VID VARCHAR(10) PRIMARY KEY,    
name VARCHAR(20),
PID CHAR(10) REFERENCES PRISONER(PID)
);"""
crsr.execute(com)

com = """INSERT INTO VISITOR VALUES ('78','SHERLOCK HOLMES', 'P1')"""
crsr.execute(com)

com = """INSERT INTO VISITOR VALUES ('99','ROSS GELLER', 'P7')"""
crsr.execute(com)

com = """INSERT INTO VISITOR VALUES ('19','REBECCA MATTHEW', 'P4')"""
crsr.execute(com)

com = """INSERT INTO VISITOR VALUES ('88','TINA MATHUR', 'P2')"""
crsr.execute(com)

#com = """SELECT * FROM VISITOR"""
#crsr.execute(com)
#ans = crsr.fetchall()
#for i in ans:
#   print(i)

con.commit()
con.close()