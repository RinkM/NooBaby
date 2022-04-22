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


    database = sqlite3.connect('noob_database2.db')
    
    cursor = database.cursor()
    

    #Find and Print Column names in a table. 
    cursor.execute("PRAGMA TABLE_INFO(user_profile)")
    print("table info : ", cursor.fetchall())

    # database = "noob_database.db"
    # if exists(database) == False: create_database()
    # cursor.execute("SELECT unique_user_str FROM user_profile")
    # user= cursor.fetchall()
    # print(user)

    
    #Find and Print All Table Names in a DB:
    # cursor.execute ("SELECT sql FROM sqlite_masterWHERE tbl_name = 'table_name' AND type = 'table'")
    table_query = ("SELECT name FROM sqlite_master WHERE type='table';")
    cursor.execute(table_query)
    tables= cursor.fetchall()
    print ("tablelist:", tables)


    # cursor.execute("SELECT baby_name FROM baby_profile WHERE unique_user_str = unique_user_str FROM user_profile WHERE username = 'mike' ")
    # username= cursor.fetchall()
    
    # cursor.execute("SELECT baby_name FROM baby_profile")
    # baby = cursor.fetchall()

    def tablecontents(table):
        cursor.execute(f"SELECT * FROM {table};")
        all_data = cursor.fetchall()
        print(f"{table} Table Data: ")
        for x in all_data:
            print(x)
        return
    tablecontents('user_profile')

    # cursor.execute("SELECT * FROM bottle;")
    # all_data = cursor.fetchall()
    # print("Bottle Table: ")
    # for x in all_data:
    #     print(x)
            


    # cursor.execute("SELECT * FROM diaper;")
    # all_data = cursor.fetchall()
    # print("Diaper Table: ")
    # for x in all_data:
    #     print(x)







# tablelist: [('user_profile',), ('baby_profile',), ('relationship',), 
#             ('sqlite_sequence',), ('bottle',), ('diaper',), 
#             ('milestones',), ('sleep',), ('solid_food',)]

    # tablecontents("sleep")


    # cursor.execute(f"SELECT userID FROM user_profile WHERE username = '{user_entry}' ;")
    # user_ID = cursor.fetchone()[0]

    # cursor.execute(f"SELECT babyID FROM relationship WHERE userID = '{user_ID}' ;")
    # baby_ID = cursor.fetchone()[0]
    # print(type(baby_ID))

    # cursor.execute(f"SELECT baby_name, birthdate_time FROM baby_profile WHERE babyID = '{baby_ID}' ;")
    # baby_name = cursor.fetchone()
    # print(baby_name)




    # cursor.execute(f"SELECT userID FROM user_profile WHERE username = '{user_entry}' ;")
    # user_ID = cursor.fetchone()[0]

    # cursor.execute(f"SELECT babyID FROM relationship WHERE userID = '{user_ID}' ;")
    # baby_ID = cursor.fetchone()[0]
    # print(type(baby_ID))

    # cursor.execute(f"SELECT baby_name, birthdate_time FROM baby_profile WHERE babyID = '{baby_ID}' ;")
    # baby_name = cursor.fetchone()
    # print(baby_name)



    # print(type(bottle))
    # for x in bottle:
    #     print(x)


    # def check_for_user():
    #     cursor.execute("SELECT * FROM user_profile")
    #     user= cursor.fetchall()
    #     print(type(user))
    #     print('user', (user))
    #     if user==[]:
    #         NooB_Profile.main(root)

    
    
    # #THIS RETURNS THE USERNAME OF THE BABY!!!!!

    # timeobjectt = time.struct_time(tm_year=2022, tm_mon=3, tm_mday=15, tm_hour=22, tm_min=19, tm_sec=49, tm_wday=1, tm_yday=74, tm_isdst=1)
    # print(timeobjectt)
            
    steve = "2022-04-11 21:57:04"
    othersteve = datetime.datetime.fromisoformat("2022-04-11 21:57:04")
    secondsteve = datetime.datetime.strptime("2022-04-11 21:5","%Y-%m-%d %H:%M")
    print(secondsteve)

    txt = "welcome to the jungle"

    x= steve.split()

    print(x) 
    bottles = {}

    fulltime = time.strftime("%M:%H")
    fulldate = time.strftime("%b %d, %Y")
    datetimestr = f"{fulltime}\non\n{fulldate}"
    print("full", fulltime, fulldate, datetimestr)
    bottles["split_datetime"] = (fulldate, fulltime)
    print("split", bottles["split_datetime"][1])








# # """DATA SUBMISSION BUTTONS"""
#     def bottle_summary_frame(choice):  #3rd frame. Provides summary and enter button. 
#         #A 'choice' is passed. It is the bottle, sleep, or diaper choice.  
#         # Opens the correct window depending.
#         clear_frame(top_frame_3)
#         create_frame(tframegrid3)
#         # time_summary = 
#         # date_summary = 
#         onetwo = 1
#         sleeptime =1
        
#         if choice == "bottle":
#             bottles["datetime"] = datetime.datetime.now()
#             bottles['milk_amount'] = 6
#             print(bottles["datetime"])
#             bottle_summary_label = ctk.CTkLabel(master = top_frame_3, text = f"Summary\n {all_data['name']} had:\n {bottles['milk_amount']} oz of MILK\n at HH:MM\nMM-DD-YYYY")
#             button_text = "Enter Bottle"
#             button_func = lambda: bottle_button()
#         elif choice == "diaper":

#             if diapers['onetwo'] == 1:
#                 diapercolor = "yellow"
#             else : 
#                 diapercolor = "brown"
#             bottle_summary_label = ctk.CTkLabel(master = top_frame_3, text = f"Summary\n {all_data['name']} had \n a {diapercolor} diaper \n in the { diapers['time_of_day']} ")
#             button_text = "Enter Diaper"
#             button_func = lambda:sql_diaper()
#         elif choice == "sleep":
#             bottle_summary_label = ctk.CTkLabel(master = top_frame_3, text =f"Summary\n {all_data['name']} slept \n for X TIME \n until HH:MM")
#             button_text = "Enter Sleep"
#             button_func = lambda: sql_sleep(sleeptime)

        
#         submit_bottle_button = ctk.CTkButton(master = top_frame_3, text = button_text, command = button_func)
        
#         # top_frame_3.grid(column = 3,  padx = 5, pady = 5, row = 0, rowspan = 3)
#         bottle_summary_label.grid(column = 0, row = 0)
#         submit_bottle_button.grid(column = 0, row = 1)


    # # print(baby[0][6])
    # print("all baby info : ", baby)

    # # #this is the user's UUID number.   
    # print("userID", user)
    # # print("username", username)
    # # namee='jamie'

    # cursor.execute(f"SELECT * FROM user_profile WHERE username = '{namee}' ")
    # jamie= cursor.fetchall()
    # print(jamie)
    # utc_dt = datetime(2002, 10, 27, 6, 0, 0, tzinfo=-8)
    # print(datetime.datetime.astimezone())
    import pytz

    # # print( datetime.now(timezone.utc))
    # tz_string = datetime.datetime.now(datetime.timezone.utc).astimezone()
    # print("tzstring", tz_string)
    # dt = datetime.datetime(2022,4,10, hour=18, minute=30, second=0, tzinfo=None, fold=0)
    # print(dt)
    # print(datetime.datetime.now())
    # # print(pytz.common_timezones)


        
    # local = pytz.timezone("US/Mountain")
    # naive = datetime.datetime.strptime("2001-2-3 10:11:12", "%Y-%m-%d %H:%M:%S")
    # print('naive', naive)
    # local_dt = local.localize(naive, is_dst=True)
    # utc_dt = local_dt.astimezone(pytz.utc)
    # print(local_dt, utc_dt)
    # print(utc_dt.strftime("%Y-%m-%d %H:%M:%S"))

    # # From there, you can use the strftime() method to format the UTC datetime as needed:

    # # dt_ts = datetime.fromtimestamp(1571595618.0, tz=timezone.utc)

    # utc_dt.strftime("%Y-%m-%d %H:%M:%S")

    # print(time.mktime(2022,4,10))


    # 2022-04-10 18:30:00


# TIME PRACTICE BELOW


#these are the three data types i want : 
# print("datetime.datetime.now()",datetime.datetime.now())
# print ("time.time()", time.time())
# print("strftime", time.strftime(" %H:%M:%S, %m/%d/%Y"))

#Collects this data : 
# datetime.datetime.now() 2022-03-17 16:51:54.538873
# time.time() 1647557514.5398753
# strftime  16:51:54, 03/17/2022




#these are the two data types i want : 
# print(datetime.datetime.now())
# print (time.time())


# import time
# import datetime

# print (time.localtime())
# print (time.asctime())
# print (time.time())
# print (dir(datetime))
 #converts utc into datetime 2022-03-15 22:19:49
# print("from timestamp", datetime.datetime.fromtimestamp(1647404389))






# time.struct_time(tm_year=2022, tm_mon=3, tm_mday=15, tm_hour=22, tm_min=19, tm_sec=49, tm_wday=1, tm_yday=74, tm_isdst=1)
# Tue Mar 15 22:19:49 2022
# 1647404389.2520874


# print(time.gmtime(1647404389.2520874))  #use this to get the long key value pairs for the date.
# print()
# print (time.asctime(time.localtime(2647404589))) #use this to get a date string.


#  ISO 8601 (yyyy-MM-dd'T'HH:mm:ssZ)



    # print(datetime.datetime.fromtimestamp()



    #  14:00:00"

# # baby_profile



if __name__ == '__main__':
    main()

