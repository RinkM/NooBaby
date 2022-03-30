"""
THings learned : the fetchall 'resets' the selection and it must be selected again.
the results are a tuple inside a list.   I can use the tuple to find 

a search querey would be like : find the user ID#.  select the baby that belongs to this number. show their milk status.  
can I combine selections?  Both userprofile and baby one?



how to pull data?    
how to graph data?
how to structure data

Main owner = username
username owns baby 
baby owns the data.

table shows the 

"""


def main():
    
    import tkinter as tk, customtkinter as ctk
    import random #For the bottle notice. 
    import sqlite3, datetime, time, uuid
    from os.path import exists
    import tkcalendar as tkcal


    database = sqlite3.connect('noob_database.db')
    cursor = database.cursor()

    # database = "noob_database.db"
    # if exists(database) == False: create_database()
    cursor.execute("SELECT unique_user_str FROM user_profile")
    user= cursor.fetchall()

    
    cursor.execute("SELECT baby_name FROM baby_profile WHERE unique_user_str = unique_user_str FROM user_profile WHERE username = 'mike' ")
    username= cursor.fetchall()
    
    cursor.execute("SELECT baby_name FROM baby_profile")
    baby = cursor.fetchall()
    
    
    #THIS RETURNS THE USERNAME OF THE BABY!!!!!
    # print(baby[0][6])
    # print("all baby info : ", baby)

    # #this is the user's UUID number.   
    # print("userID", user)
    print("username", username)
    # namee='jamie'

    # cursor.execute(f"SELECT * FROM user_profile WHERE username = '{namee}' ")
    # jamie= cursor.fetchall()
    # print(jamie)



    
    

# # baby_profile



if __name__ == '__main__':
    main()

