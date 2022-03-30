
"""
NooB_MakeDB.py 
Opens / creates the sqlite3 database file, various tables, and columns.
Saves the changes. 
Quits the database. 
"""

def main():
    import sqlite3, datetime, time, uuid
    from os.path import exists
    
    database = sqlite3.connect('noob_database.db')
    cursor = database.cursor()


    # database = "noob_database.db"
    # if exists(database) == False: create_database()
    
    def create_database():
    
        cursor.execute("""CREATE TABLE IF NOT EXISTS bottle (
                bottle_num integer UNIQUE, 
                datetime text,
                utc integer,  
                amount integer NOT NULL,
                baby_id integer, 
                product text,
                product_id integer
                ) """) 

        cursor.execute("""CREATE TABLE IF NOT EXISTS diaper(
                    table_id text,
                    diaper_num integer, 
                    datetime text,
                    utc integer,
                    onetwo integer NOT NULL,
                    baby_id integer 
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
                    baby_id integer,
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
                    baby_id integer
            )""")




        cursor.execute("""CREATE TABLE IF NOT EXISTS baby_profile (
                    unique_user_str text,
                    baby_id text PRIMARY KEY,
                    table_id text,
                    profile_num integer, 
                    datetime text,
                    utc integer,
                    baby_name text,
                    birthdate_time text
                    
            )""")


        cursor.execute("""CREATE TABLE IF NOT EXISTS user_profile (
                    table_id text,
                    unique_user_str text PRIMARY KEY,
                    datetime text,
                    utc integer,
                    username text
            )""")

        #this saves the database. 
        database.commit()

        # this closes the database.
        database.close()

    create_database()

if __name__ == '__main__':
    main()