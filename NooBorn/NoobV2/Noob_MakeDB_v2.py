
"""
NooB_MakeDB.py 
Opens then creates the sqlite3 database file, various tables, and columns.
Saves the changes. 
Quits the database. 

notes : primary key should be first entry in database.  

"""

def main():
    import sqlite3

    database = sqlite3.connect('noob_database2.db')
    cursor = database.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")#turns foreign keys on.

    # if exists(database) == False: create_database()
#updated 3/31/22

    def create_baby_profile():
        cursor.execute("""CREATE TABLE IF NOT EXISTS baby_profile (
                userID text,
                babyID text PRIMARY KEY,
                datetime text,
                utc integer,
                baby_name text,
                birthdate_time text
            );""")

#updated 3/31/22
    def create_user_profile():
        cursor.execute("""CREATE TABLE IF NOT EXISTS user_profile (
                userID text PRIMARY KEY,
                datetime text,
                utc integer,
                username text UNIQUE,
                password text
            );""")

#updated 3/31/22
    def create_relationship():
        cursor.execute("""CREATE TABLE IF NOT EXISTS relationship (
                table_id    INTEGER     PRIMARY KEY ASC AUTOINCREMENT,
                userID      text    NOT NULL, 
                babyID      text    NOT NULL,
                FOREIGN KEY (userID) REFERENCES user_profile (userID),
                FOREIGN KEY (babyID) REFERENCES baby_profile (babyID)
            );""")

    def create_bottle():
        #slight update 4/3/22 - entry button made elsewhere, be wary.
        cursor.execute("""CREATE TABLE IF NOT EXISTS bottle (
                table_id    INTEGER     PRIMARY KEY ASC AUTOINCREMENT,
                datetime text,
                utc integer,  
                amount integer NOT NULL,
                product text,
                product_id integer,
                babyID text NOT NULL, 
                FOREIGN KEY(babyID) REFERENCES baby_profile(babyID)
                ) """) 
##slight update 4/3/22
    def create_diaper():
        cursor.execute("""CREATE TABLE IF NOT EXISTS diaper(
                table_id    INTEGER     PRIMARY KEY ASC AUTOINCREMENT,
                datetime text,
                utc integer,
                onetwo integer NOT NULL,
                babyID text NOT NULL, 
                FOREIGN KEY(babyID) REFERENCES baby_profile(babyID)
                )""")
##slight update 4/3/22
    def create_sleep():
        cursor.execute("""CREATE TABLE IF NOT EXISTS sleep(
                table_id    INTEGER     PRIMARY KEY ASC AUTOINCREMENT,
                datetime text,
                utc integer,
                start_time integer, 
                end_time integer,
                duration integer NOT NULL,
                babyID text NOT NULL, 
                FOREIGN KEY(babyID) REFERENCES baby_profile(babyID)
                )""")

##slight update 4/3/22
    def create_solidfood():
        cursor.execute("""CREATE TABLE IF NOT EXISTS solid_food(
                table_id    INTEGER     PRIMARY KEY ASC AUTOINCREMENT,
                solid_food_num integer, 
                datetime text,
                utc integer,
                food_name text,
                amount integer NOT NULL,
                babyID text NOT NULL, 
                FOREIGN KEY(babyID) REFERENCES baby_profile(babyID)
            )""")
#updated 4/2/22 but... not well.
    def create_milestones():
        cursor.execute("""CREATE TABLE IF NOT EXISTS milestones(
                table_id    INTEGER     PRIMARY KEY ASC AUTOINCREMENT,
                stone_name text, 
                stone_description text,
                stone_acheived integer,
                stone_text_achieve text, 
                datetime text,
                utc integer,
                babyID text NOT NULL, 
                FOREIGN KEY(babyID) REFERENCES baby_profile(babyID)
            )""")

    #allows me to see what tables are in DB:
    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # print("Table List", cursor.fetchall())

    #breaks down a table into it's columns
    def table_info(tablename):
        cursor.execute(f"PRAGMA table_info({tablename});")
        tableInfo = cursor.fetchall()
        for x in tableInfo:
            print(x)

    #Information about the Foreign Key Toggle: 
    # cursor.execute("PRAGMA foreign_key_check;")  
    # print("keyCheck", cursor.fetchall())
    # cursor.execute("PRAGMA foreign_keys= True;")  
    # print("foreignkeys : ", cursor.fetchall())
    # cursor.execute("PRAGMA foreign_keys;")  
    # print("same", cursor.fetchall())
    # print(cursor.fetchall())

    def create_all_tables():
        create_user_profile()
        create_baby_profile()
        create_relationship()
        create_bottle()
        create_diaper()
        create_milestones()
        create_sleep()
        create_solidfood()
        print("database is set and and good to go!")

    #Functions that run : 
    create_all_tables()
    # table_info('bottle')


    database.commit()
    database.close()


if __name__ == '__main__':
    main()