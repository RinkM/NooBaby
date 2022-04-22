
"""
GOAL - Cut this window into pieces!    300 lines!




Noob_window.py
Creates the main window of the app, which includes the data type buttons. 
Allows user to navigate the menus on screen and store information.

Information is stored in sqlite3 database with various tables for different information.
Longterm Goal : Have a bottom window that uses that sqldata to create graphs / visuals for the health information about baby. 

Will need access to UUID and Baby UUID information. 
Maybe... I should just write the final buttons.. now.. then carry stuff over to get there?   Does that work?   
Think backwards.   [3]
Time passed since thinking backwards....I've thought backwards. I still need the UUID information....[2]


4/6/22
ALL_data as it currently get passed in. 
all data:  {'user': '3033b7a7-58d8-4c45-b0aa-13786d643ce5', 'baby': '5b1632cd-cd97-49c1-9bef-82665f0f5c5a', 'name': 'TestBaby', 'bday': '2022-01-04 00:00:00'}

Change bottle references to MILK or SOLID FOODS




4/7
was working on diaper sql entry and time gather.  completed the diaper gather.  worked on bottle, but struggled. 
"""



def window_main(root, all_data):

    import tkinter as tk, customtkinter as ctk
    import sqlite3, datetime, time, uuid
    import tkcalendar as tkcal
    import pytz


    #Turn On for testing without going through main window:
    # root = ctk.CTk() 


    print(all_data)

    root.geometry("1024x576")
    root.resizable(width=False, height=False)
    root.title("NooBorn Window")

    #List of Frames:
    
    top_frame_1 = ctk.CTkFrame(master = root, corner_radius = 20)
    top_frame_2 = ctk.CTkFrame(master = root, corner_radius = 20)
    top_frame_2a = ctk.CTkFrame(master = root, corner_radius = 20)
    top_frame_3 = ctk.CTkFrame(master = root, corner_radius = 20)
    
    tframe_list = [top_frame_1,top_frame_2,top_frame_3,top_frame_2a]

    bottom_frame_master = ctk.CTkFrame(master = root, corner_radius = 20, width = 875)

    #List of instructions to place frames on screen.
    tframegrid1 = {"frame": top_frame_1, "column" : 1, "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}
    tframegrid2 ={"frame": top_frame_2, "column" : 2,  "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}
    tframegrid2a = {"frame": top_frame_2a, "column" : 2,  "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}
    tframegrid3 = {"frame": top_frame_3, "column" : 3,  "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}
    bframegrid = {"frame": bottom_frame_master, "column" : 1,  "padx" : 5, "pady" : 5, "row" : 3, "columnspan" : 3, "rowspan" : 3, "sticky": 'ew'}
    


    #Bottom Frame : 
    # bottom_frame_1 = ctk.CTkFrame(master = bottom_frame_master, corner_radius = 20)
    # bottom_frame_2 = ctk.CTkFrame(master = bottom_frame_master, corner_radius = 20)
    # bottom_frame_2a = ctk.CTkFrame(master = bottom_frame_master, corner_radius = 20)
    # bottom_frame_3 = ctk.CTkFrame(master = bottom_frame_master, corner_radius = 20)

    
    #Extra Frame Placements for Bottom
    # bframegrid1 = {"frame": bottom_frame_1, "`column" :0, "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}
    # bframegrid2 ={"frame": bottom_frame_2, "column" : 1,  "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}
    # bframegrid2a = {"frame": bottom_frame_2a, "column" : 1,  "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}
    # bframegrid3 = {"frame": bottom_frame_3, "column" : 2,  "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}

    # bottom_left = ctk.CTkLabel(master = bottom_frame_master, text = "Food Info \nWill Be Displayed Here")
    # bottom_center = ctk.CTkLabel(master = bottom_frame_master, text = "Sleep Info \nWill Be Displayed Here")
    # bottom_right = ctk.CTkLabel(master = bottom_frame_master, text = "Milestone Info \nWill Be Displayed Here")


#TIME COLLECTION CLASSES - Used to create date /time entry widgets. 
#These classes are the only code I've 'stolen' from stackoverflow.  
# Original source was here : 
# https://stackoverflow.com/questions/57034118/time-picker-for-tkinter







    #make babyID = a variable.  But... how do I do it with the username? 
    # How do I match the username with the baby?






    button_builder(main_menu)
    print("all_data" ,all_data['name'])



if __name__ == '__main__':
    window_main()



