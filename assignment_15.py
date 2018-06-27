import MySQLdb
db=MySQLdb.connect("localhost","root","2216","DB1")
cursor=db.cursor()


print("Q1. CREATE the following tables\n")

  
sql="""CREATE TABLE BOOKS 
BOOK_ID INT NOT NULL,
TITLE_ID INT,
LOCATION CHAR(15),
GENRE CHAR(15)
"""

sql2="""CREATE TABLE TITLES 
TITLE_ID INT NOT NULL,
TITLE CHAR(30),
ISBN INT, 
PUBLISHER_ID INT,
PUBLICATION_YEAR INT 
"""

sql3="""CREATE TABLE PUBLISHERS
PUBLISHER_ID INT NOT NULL,
NAME CHAR(30),
STREET_ADDRESS CHAR(30),
SUITE_NUMBER INT,
ZIP_CODE INT
"""

sql4="""CREATE TABLE ZIP_CODES
ZIP_CODE_ID INT NOT NULL,
CITY CHAR(20),
STATE(20),
ZIP_CODE INT
"""

sql5="""CREATE TABLE AUTHORS TITLES
AUTHOR_TITLE_ID INT NOT NULL,
AUTHOR_ID INT,
TITLE_ID INT
"""
sql6="""CREATE TABLE AUTHORS
AUTHOR_ID INT NOT NULL,
FIRST_NAME CHAR(10),
MIDDLE_NAME CHAR(10),
LAST_NAME CHAR(10)
"""

cursor.execute(sql)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql4)
cursor.execute(sql5)
cursor.execute(sql6)









print("\n\nQ2. INSERT values in the above tables\n")


insert1 = """INSERT INTO BOOKS(BOOK_ID,TITLE_ID,LOCATION,GENRE ) 
        VALUES(122, 22, "KALKI","Literature")"""
try:
    cursor.execute(insert1)
    db.commit()
except:
    db.rollback()

insert2 = """INSERT INTO TITLES( TITLE_ID,TITLE,ISBN,PUBLISHER_ID,PUBLICATION_YEAR ) 
        VALUES(122,"KALKI",1223103346,208,2019)"""
try:
    cursor.execute(insert2)
    db.commit()
except:
    db.rollback()

insert3 = """INSERT INTO PUBLISHERS(PUBLISHER_ID,NAME,STREET_ADDRESS,STATE_NUMBER,ZIP_CODE_ID ) 
        VALUES(208,"BIGGO","WALL STREET",808080,1)"""
try:
    cursor.execute(insert3)
    db.commit()
except:
    db.rollback()

insert4 = """INSERT INTO ZIP_CODES(ZIP_CODE_ID,CITY,STATE,ZIP_CODE) 
        VALUES(1,"DEHRADUN","UK",248001)"""
try:
    cursor.execute(insert4)
    db.commit()
except:
    db.rollback()

insert5 = """INSERT INTO AUTHORS_TITLES(AUTHOR_TITLE_ID,AUTHOR_ID,TITLE_ID ) 
        VALUES(100,101,285)"""
try:
    cursor.execute(insert5)
    db.commit()
except:
    db.rollback()

insert6 = """INSERT INTO AUTHORS(AUTHOR_ID, FIRST_NAME, MIDDLE_NAME,LAST_NAME ) 
        VALUES(101,"ASHUTOSH","-","RAWAT")"""
try:
    cursor.execute(insert6)
    db.commit()
except:
    db.rollback()







print("\n\nQ3. UPDATE in any one of the above tables.\n)

upd ="""UPDATE BOOKS SET GENRE="Sci-Fi Thriller" 
      WHERE LOCATION='DEHRADUN'"""
try:
    cursor.execute(upd)
    db.commit()
except:
    db.rollback()
db.close()