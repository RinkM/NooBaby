


"""
Program Goals - 
It will : NooBorn will allow a user to track and view the nutrition, sleep, and waste of infants.  
Major Goals : 
allow user to input food, sleep and diaper changes as they happen. 
Display this information in a way similar to Fitbit or Apple health. 
    Track personalized averages over time, create visual displays, showing what is normal and abnormal.
    compare with data about average children.   Basically freak out new parents with "WHY IS MY BABY EATING TOO MUCH?!?!  (OR NOT ENOUGH!?!?!)
    allow user to view and edit previous data entries to clean up their mistakes.  Can delete their own sql entries.



SO MUCH TO DO....
4/14/22
FIXED SO MANY ISSUES.   BUT IT WORKS AGAIN!   Now I can break it again if I want!
4/9/22
REASSESS - 
Should I split NOOB WINDOW - One for TKINTER buttons and commands.
One for all the SQL commands?
Passes the dicationary into the button commands?
Maybe.....

What is broken / incomplete : 
liquid slider not printing results
solid food going to the wrong place.   What if I make a simple thing?    Food name, amount. 
rethink sleep sliders.   short or full sleep. 
ENTER BOTTLE BUTTON TESTS.  1 button collects the data and sends it over to summary table.
Requires you to set the date / time buttons and they must be real things...

Create Profile Menu - Create Error messages for user. 
did you enter a date? Did you enter username? Is it acceptable?  What problems are there? Messages to guide the user.
username screen - checking the username. Is it valid?   forgot your username button?   Yeah... no.

Inner profile menu - ability to select two babys. 
Can I make a picture a button?   Like the baby profile?    Put that somewhere on the screen?   

When in Diaper menu - selecting the yellow or brown doesn't redraw the summary frame.


"""



def main():


    import NooB_Profile as prof
    import NooB_MakeDB as db

    import tkinter as tk, customtkinter as ctk
    import sqlite3, datetime, time, uuid
    from os.path import exists


    database = sqlite3.connect('noob_database2.db')
    cursor = database.cursor()


    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    
    root = ctk.CTk() 
    # root.geometry("1024x576")
    root.resizable(width=False, height=False)
    root.title("NooBorn")



    db.main()
    prof.profile_main(root)
    root.mainloop()


























if __name__ == '__main__':
    main()
