



def main(root, all_data,color):
    import datetime
    import tkinter as tk, customtkinter as ctk
    import sqlite3, datetime, time, uuid
    import tkcalendar as tkcal
    import noob_button_functions
    import Noob_Summary as summary


    top_frame_2a = ctk.CTkFrame(master = root, corner_radius = 20)
    tframegrid2a = {"frame": top_frame_2a, "column" : 2,  "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}



    time_period_buttons = {"Morning" : { "name" : "Morning",  "column" :0, "row" :0, "sticky" : "new", "window" : top_frame_2a, "command" : lambda:diaper_time("08:00:00", 'morning') }, 
                       # "Midday" : { "name" : "Midday", "column" :1, "row" :0, "sticky" : "new", "window" : top_frame_2a, "command" : lambda: custom_time_frame()},
                        "Afternoon" : { "name" : "Afternoon", "column" : 2, "row" :0, "sticky" : "new", "window" : top_frame_2a, "command" : lambda: diaper_time("14:00:00", 'afternoon')},
                        "Evening" : { "name" : "Evening", "column" : 3, "row" :0, "sticky" : "new", "window" : top_frame_2a, "command" : lambda: diaper_time("19:00:00", 'evening')},
                        "Night" : { "name" : "Night", "column" : 4, "row" :0, "sticky" : "new", "window" : top_frame_2a, "command" : lambda: diaper_time("23:00:00", 'night')}
                        }


    #Diaper Button Functions
    def yellow_press(): #when yellow diaper button is pressed.  - creates the morning, noon etc. buttons. Changes bg color. 
        noob_button_functions.clear_frame(top_frame_2a)
        noob_button_functions.create_frame(tframegrid2a)   
        noob_button_functions.button_builder(time_period_buttons)
        # if all_data['onetwo']:
        #     final_summary_frame("diaper")
        
        all_data['onetwo'] = 1
        top_frame_2a.configure(fg_color = '#e3dd20')



    def brown_press():
        noob_button_functions.clear_frame(top_frame_2a)
        noob_button_functions.create_frame(tframegrid2a)   
        noob_button_functions.button_builder(time_period_buttons)
        all_data['onetwo'] = 2
        
        top_frame_2a.configure(fg_color = '#715f1d')



    def diaper_time(time, daytime):
        #called from diaper 'morning, afternoon, etc. buttons. 
        #enters a generic time for the buttons. 
        diaper_time = f"{datetime.date.today()} {time}"
        all_data['diaper_datetime']= diaper_time
        all_data['moment_of_day']= daytime
        print(diaper_time,daytime)
        summary.main(root,all_data,"diaper")
        format  = "%Y-%m-%d %H:%M:%S"
        local_dt = datetime.datetime.strptime(diaper_time, format)
        print("local", local_dt)

        # dt_utc = local_dt.astimezone(pytz.UTC)
        # print('Datetime in UTC Time zone: ', dt_utc)
        # dt_utc_str = dt_utc.strftime(format)
        # print('Datetime string in UTC Time zone: ', dt_utc_str)



    if color == "yellow":
        yellow_press()
    elif color == "brown":
        brown_press()









if __name__ == '__main__':
    main()







        