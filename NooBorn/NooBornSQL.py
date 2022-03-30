# GREATE EXAMPle of creating tables using functions : 
# https://www.sqlitetutorial.net/sqlite-python/create-tables/


#  The date() function returns the date as text in this format: YYYY-MM-DD.

# The time() function returns the time as text in this format: HH:MM:SS.

# The datetime() function returns the date and time as text in their same formats: YYYY-MM-DD HH:MM:SS. 


# import nooborntest
from dataclasses import dataclass
import sqlite3
import datetime
import time

#connection object to be the database
# def make_database():
database = sqlite3.connect('noob_database.db')
# return database

# database = nooborntest.db

cursor = database.cursor()

#creates a table with 3 columns and what the expected data should be.  
#  I had the comma in wrong place created table with 4th column.  an integer? maybe?  

# def create_tables():

# def create_bottle():
cursor.execute("""CREATE TABLE IF NOT EXISTS bottle3 (
        bottle_num integer UNIQUE, 
        datetime text,
        utc integer,  
        amount integer NOT NULL,
        baby_id integer, 
        product text,
        product_id integer
        ) """) 

#testing version
cursor.execute("SELECT * FROM bottle3;")
cursor.description
print("before data", cursor.description)


cursor.execute("""CREATE TABLE IF NOT EXISTS diaper(
            table_id text,
            diaper_num integer, 
            datetime text,
            utc integer,
            onetwo integer NOT NULL,
            baby_id integer FOREIGN KEY
            )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS sleep(
            table_id text,
            bottle_num integer, 
            datetime text,
            utc integer,
            start_time integer, 
            end_time integer,
            duration integer NOT NULL,
            baby_id integer
            )""")


cursor.execute("""CREATE TABLE IF NOT EXISTS solid_food(
            table_id text,
            solid_food_num integer, 
            datetime text,
            utc integer,
            baby_id integer FOREIGN  KEY,
            food_name text,
            amount integer NOT NULL




    )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS milestones(
            table_id text,
            stone_num integer,
            stone_name text, 
            stone_description text,
            stone_acheived integer,
            stone_text_achieve text, 
            datetime text,
            utc integer,
            baby_id integer FOREIGN  KEY


    )""")


cursor.execute("""CREATE TABLE IF NOT EXISTS baby_profile (
            table_id text,
            profile_num integer, 
            datetime text,
            utc integer,
            baby_id integer PRIMARY KEY,
            baby_name text,
            birthdate_utc integer,
            birthdate_time text NOT NULL,
            sex integer,
            unique_user_str text,
            unique_user blob


    )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS user_profile (
            table_id text,
            unique_user_str text PRIMARY KEY,
            unique_user blob,
            user_num integer, 
            datetime text,
            utc integer,
            baby_id integer,
            username text,
            password text


    )""")








#columns in baby bottle : overkill. 
# bottle_num integer, datetime text, utc integer, amount integer NOT NULL,baby_id integer FOREIGN  KEY, roduct text,product_id integer) """)

# 2022-03-17 01:49:49
# 2022-03-18 05:56:29
# 2022-03-15 22:24:49
# 2022-03-14 18:51:29

# 1647604589
# 1647404689
# 1647305489
# 1647503389


# cursor.execute("""INSERT INTO bottle3 (
#         bottle_num, datetime, utc, amount, baby_id, product, product_id)
#         VALUES (3, '2021-05-17 01:49:49', 1647504589, 180, 803, 'Powder Milk', 100)""")


# cursor.executemany(
#   "INSERT INTO bottle3 (bottle_num, datetime, utc, amount, baby_id, product, product_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
# [
#     (1, '2022-03-17 01:49:49', 1647604589, 180, 803, 'Powder Milk', 100),
#     (2, '2022-03-18 05:56:29', 1647404689, 180, 803, "Powder Milk", 100),
#     (5, '2022-03-15 22:24:49', 1647305489, 160, 803, "Liquid Milk", 101),
#     (4, '2022-03-14 18:51:29', 1647503389, 100, 803, "Liquid Milk", 101),
#   ]
 
# )


# [(3, '2021-05-17 01:49:49', 1647504589, 180, 803, 'Powder Milk', 100), 
# (1, '2022-03-17 01:49:49', 1647604589, 180, 803, 'Powder Milk', 100), 
# (2, '2022-03-18 05:56:29', 1647404689, 180, 803, 'Powder Milk', 100),
#  (5, '2022-03-15 22:24:49', 1647305489, 160, 803, 'Liquid Milk', 101), 
#  (4, '2022-03-14 18:51:29', 1647503389, 100, 803, 'Liquid Milk', 101)]


# database = ""
# make_database()


cursor = database.cursor()
# cursor = database.cursor()
# create_tables()



#this saves the database. 
database.commit()
# #testing version

# cursor.execute("SELECT * FROM bottle3;")
# cursor.description
# # print("cursor description: ", cursor.description)
# print("cursor fetchall: ",cursor.fetchall())


# this closes the database.
database.close()



# [(3, '2021-05-17 01:49:49', 1647504589, 180, 803, 'Powder Milk', 100), 
# (1, '2022-03-17 01:49:49', 1647604589, 180, 803, 'Powder Milk', 100), 
# (2, '2022-03-18 05:56:29', 1647404689, 180, 803, 'Powder Milk', 100), 
# (5, '2022-03-15 22:24:49', 1647305489, 160, 803, 'Liquid Milk', 101), 
# (4, '2022-03-14 18:51:29', 1647503389, 100, 803, 'Liquid Milk', 101), 
# (26, '2022-03-16 23:42:52.655556', 1647495772.655557, 180, 803, 'Powder Milk', 100), 
# (30, '2022-03-16 23:47:34.372720', 1647496054.3727205, 180, 803, 'Powder Milk', 100), 
# (33, '2022-03-16 23:47:52.805686', 1647496072.8056865, 180, 803, 'Powder Milk', 100)]

# []
# bottlenum = 0
# def bottle_insert():
#     bottlenum += 1
#     cursor.execute("""INSERT INTO bottle (
#         bottle_num integer, 
#         datetime text,
#         date text,  
#         time text, 
#         utc integer,  
#         amount integer NOT NULL,
#         baby_id integer FOREIGN  KEY, 
#         product text,
#         product_id integer
#         ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);""")


# cursor.execute("""CREATE TABLE IF NOT EXISTS bottle (
#         bottle_num integer, 
#         datetime text,
#         date text,  
#         time text, 
#         utc integer,  
#         amount integer NOT NULL,
#         baby_id integer FOREIGN  KEY, 
#         product text,
#         product_id integer
#         ) """) 

# # INSERT INTO bottle (column1, column2, column3,...columnN)
# # VALUES (value1, value2, value3,...valueN);



 

# #what did i learn? - time.time prints the UNIX number.   1647361480.9484274    the number of seconds. I can use this. 
# # how to convert it?





# # import time


# print(time.gmtime(1647404389.2520874))  #use this to get the long key value pairs for the date.
# print()
# print (time.asctime(time.localtime(2647404589))) #use this to get a date string.



# print(time.localtime(1647361480))   #converts a unix code to d/t structure..
# # print(time.time())
# # time.sleep(1)
# # print(time.time())
# # time.sleep(2)
# # print(time.time())
# # print(time.gmtime())

# gmtime= time.gmtime()
# print(time.mktime(gmtime))   #converts time string into unix code. 
# # print(time.mktime())

# print(time.localtime()[0:4])   #can use the [] to select data from the struct_time format. 

# # 1647361480.9484274
# # time.struct_time(tm_year=2022, tm_mon=3, tm_mday=15, tm_hour=16, tm_min=24, tm_sec=40, tm_wday=1, tm_yday=74, tm_isdst=0)
