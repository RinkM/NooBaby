
"""


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

    #List of Dictionaries to be entered into DB. Think of them as storage containers. 
    diapers = {}
    bottles = {}
    sleeps = {}
    foods = {}


    #Turn On for testing without going through main window:
    # root = ctk.CTk() 
    

    print(all_data)

    root.geometry("1024x576")
    root.resizable(width=False, height=False)
    root.title("NooBorn Window")

    
    database = sqlite3.connect('noob_database2.db')
    cursor = database.cursor()

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



    class Collect_Date(ctk.CTkFrame):
        def __init__(self,parent):
            super().__init__(parent)
            create_frame(tframegrid2)
            # self.geometry("600x500")
            #variables for current Date
            current_month = time.strftime("%m")
            current_day = time.strftime("%d")
            current_year = time.strftime("%Y")

            enter_date_label = ctk.CTkLabel(self, text = "Enter Date")
            # self.reg=self.register(self.month_valid) #not sure about register. refers to the method below. 
            self.monthstr=tk.StringVar(self,f"{current_month}")    #sets the number in the box.  could be current time. 
            self.month = tk.Spinbox(self,from_=0,to=12, state="readonly",
                                    wrap=True,validate='focusout', 
                                    #validatecommand=(self.reg,'%P'),
                                    #invalidcommand=self.month_invalid, 
                                    textvariable=self.monthstr,width=2,
                                    font = "arial, 20", fg = "#eae6f5",
                                    buttonbackground = "#000000", bd =2, bg = "#000000", readonlybackground ="#000000",
                                    )

            # self.reg2=self.register(self.day_valid)
            self.daystr=tk.StringVar(self,f'{current_day}')
            self.day = tk.Spinbox(self,from_=0,to=31,wrap=True,validate='focusout',state="readonly",
                                    #validatecommand=(self.reg2,'%P'),
                                    #invalidcommand=self.day_invalid,
                                    textvariable=self.daystr,
                                    width=2, font = "arial, 20", fg = "#eae6f5",
                                    buttonbackground = "#000000", bd =2, bg = "#000000", readonlybackground ="#000000",
                                    
                                    )

            # self.reg3=self.register(self.year_valid)
            self.yearstr=tk.StringVar(self,f'{current_year}')
            self.year = tk.Spinbox(self,from_=2021,to=2030,wrap=True,validate='focusout',state = "readonly",
                                    #validatecommand=(self.reg3,'%P'),
                                    #invalidcommand=self.year_invalid,
                                    textvariable=self.yearstr,
                                    width=4, font = "arial, 20", fg = "#eae6f5",
                                    buttonbackground = "#000000", bd =2,readonlybackground ="#000000",  bg = "#000000",
                                    )
                        #I ADDED a lot of the below code to store the entered data. below.  It can be more better...
                                    

            # enter_button = ctk.CTkButton(self, text = "Enter", command = lambda:get_date(self.month,self.day, self.year))
            


            enter_date_label.grid(column=1, row =2, columnspan = 3)
            
            self.month.grid(row=3,column=0)
            self.day.grid(row=3,column=1)
            self.year.grid(row=3,column=2)
            # baby_bday_button.grid(row=4,column=0, columnspan = 3)
            
            get_month = self.month.get()
            get_day = self.day.get()
            get_year = self.year.get()
            time_entered = f"{self.month.get()}:{self.day.get()}/{self.year.get()}"
            print("time_entered, from class", time_entered)
            print(get_month, get_day, get_year)

        def get_date(self, month, day, year):
            print (self.monthstr, self.daystr, self.yearstr)
            time_entered = f"{month.get()}/{day.get()}/{year.get()}"
            print("get_date - returns:", time_entered)
            return(time_entered)


            #below code is pointless now, but I'm too scared to delete it.  
        # def month_invalid(self):
        #     self.monthstr.set('6')
        # def month_valid(self,input):
        #     if (input.isdigit() and int(input) in range(12) and len(input) in range(1,3)):
        #         valid = True
        #     else:
        #         valid = False
        #     if not valid:
        #         self.month.after_idle(lambda: self.month.config(validate='focusout'))
        #     return valid
        # def day_invalid(self):
        #     self.daystr.set('15')
        # def day_valid(self,input):
        #     if (input.isdigit() and int(input) in range(31) and len(input) in range(1,3)):
        #         valid = True
        #     else:
        #         valid = False
        #     if not valid:
        #         self.day.after_idle(lambda: self.day.config(validate='focusout'))
        #     return valid
        # def year_invalid(self):
        #     self.yearstr.set('2022')
        # def year_valid(self,input):
        #     if (input.isdigit() and int(input) in range(2020,2030) and len(input) in range(4)):
        #         valid = True
        #     else:
        #         valid = False
        #     if not valid:
        #         self.year.after_idle(lambda: self.year.config(validate='focusout'))
        #     return valid



    class Collect_Time(ctk.CTkFrame):
        def __init__(self,parent):
            super().__init__(parent)
            # self.geometry("600x500")
            # create_frame(tframegrid2)

            #USE STRPTIME TO GET THE DATE TO LOOK RIGHT
            #variables for current Time
            current_min = time.strftime("%M")
            current_hour = time.strftime("%H")


            enter_date_label = ctk.CTkLabel(self, text = "Enter Time")

            # self.reg=self.register(self.hour_valid) #not sure about register. refers to the method below. 
            self.hourstr=tk.StringVar(self,f"{current_hour}")    #sets the number in the box.  could be current time. 
            self.hour = tk.Spinbox(self,from_=0,to=23,
                                    wrap=True,validate='focusout',
                                    # validatecommand=(self.reg,'%P'),
                                    state = "readonly",
                                    # invalidcommand=self.hour_invalid,
                                    textvariable=self.hourstr,
                                    width=2,
                                    font = "arial, 20", fg = "#eae6f5",
                                    buttonbackground = "#000000", bd =2, bg = "#000000", readonlybackground ="#000000",
                                    
                                    )
            
            # self.reg2=self.register(self.min_valid)
            self.minstr=tk.StringVar(self,f'{current_min}')
            self.min = tk.Spinbox(self,from_=00,to=59,wrap=True,validate='focusout', state = "readonly",
                                    # validatecommand=(self.reg2,'%P'),
                                    # invalidcommand=self.min_invalid,
                                    textvariable=self.minstr,
                                    width=2, font = "arial, 20", fg = "#eae6f5",
                                    buttonbackground = "#000000", bd =2, bg = "#000000", readonlybackground ="#000000",
                                    )

                                    #I ADDED a lot of what's below.  It can be more better...
                                    # https://stackoverflow.com/questions/57034118/time-picker-for-tkinter


            enter_button = ctk.CTkButton(self, width = 100, text = "Enter", command = lambda:get_time())

            enter_date_label.grid(column=0, row = 1, columnspan = 2)    
            self.hour.grid(row=2,column=0)
            self.min.grid(row=2,column=1)
            # baby_bday_button.grid(row=3,column=0, columnspan = 2)

            get_hour = self.hour.get()
            get_min = self.min.get()
            time_entered = f"{self.hour.get()}:{self.min.get()}"
            print(time_entered)
            print(get_hour, get_min)

            #does this function do anything?
            def get_time():
                time_entered = f"{self.hour.get()}:{self.min.get()}"
                print("get_time - returns:", time_entered)
                return(time_entered)


            #CODE BELOW WAS USED TO VALIDATE THE DATA BEING ENTERED.....BUT I MADE THE SPINBOXES READONLY....THEY DON'T NEED TO VALIDATE THE DATA ANYMORE.
        # def hour_invalid(self):
        #     self.hourstr.set('10')
        # def hour_valid(self,input):
        #     if (input.isdigit() and int(input) in range(24) and len(input) in range(1,3)):
        #         valid = True
        #     else:
        #         valid = False
        #     if not valid:
        #         self.hour.after_idle(lambda: self.hour.config(validate='focusout'))
        #     return valid
        # def min_invalid(self):
        #     self.minstr.set('30')
        # def min_valid(self,input):
        #     if (input.isdigit() and int(input) in range(60) and len(input) in range(1,3)):
        #         valid = True
        #     else:
        #         valid = False
        #     if not valid:
        #         self.min.after_idle(lambda: self.min.config(validate='focusout'))
        #     return valid
        
        # def get_time(self):
        #     time = f"{self.min.get():self.hour.get()}"
        #     return print(time)





    # Lists of Buttons in Main Window.
    main_menu = {"food_button" : {"name" : "Food", "window" : root, "column" : 0, "row" :0, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1,food_menu1)},
            "sleep_button" : {"name" : "Sleep", "window" : root, "column" : 0, "row" :1, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1, sleep_menu1)},
            "diaper_button" : {"name" : "Diaper", "window" : root, "column" : 0, "row" :2, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1, diaper_menu1)},
            "milestones" : {"name" : "Milestones", "window" : root, "column" : 0, "row" :3, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1, milestones1)},
            "activities" : {"name" : "Activities", "window" : root, "column" : 0, "row" :4, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1, activities1)},
            "profile_button" : {"name" : "Profile", "window" : root, "column" : 0, "row" :5, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1, profile1)},
            }

    food_menu1 = {"Liquid" : { "name" : "Liquid", "window" : top_frame_1, "column" : 0, "row" :0, "sticky" : "new", "command" : lambda:custom_time_frame() }, 
            "Solids" : { "name" : "Solids", "column" : 0, "row" :1, "sticky" : "new", "window" : top_frame_1, "command" : lambda: custom_time_frame()}
            }

    milestones1 = {"Goals" : { "name" : "Milestone Goals", "window" : top_frame_1, "column" : 0, "row" :0, "sticky" : "new", "command" : lambda: button_builder(xxx)}, 
                     "Accomplishments" : { "name" : "Accomplishments", "window" : top_frame_1, "column" : 0, "row" :1, "sticky" : "new", "command" : lambda: remove_buttons(sleep_menu)}
                     }

    activities1= {"Games" : { "name" : "Games", "window" : top_frame_1, "column" : 0, "row" :0, "sticky" : "new", "command" : lambda: button_builder(xxx)}, 
                 "Songs" : { "name" : "Songs", "window" : top_frame_1, "column" : 0, "row" :1, "sticky" : "new", "command" : lambda: remove_buttons(sleep_menu)}
                 }

    sleep_menu1 = {"Short Nap" : { "name" : "Short Nap", "window" : top_frame_1, "column" : 0, "row" :0, "sticky" : "new", "command" : lambda: sleep_button_press()}, 
                     "Full Sleep" : { "name" : "Full Sleep", "window" : top_frame_1, "column" : 0, "row" :1, "sticky" : "new", "command" : lambda: sleep_button_press()}
                     }

    diaper_menu1 = {"Yellow" : { "name" : "Yellow", "window" : top_frame_1, "column" : 0, "row" :0, "sticky" : "new", "command" : lambda: yellow_press()}, 
                    "Brown" : { "name" : "Brown", "window" : top_frame_1, "column" : 0, "row" :1, "sticky" : "new", "command" : lambda: brown_press()}
                      }


    time_period_buttons = {"Morning" : { "name" : "Morning",  "column" :0, "row" :0, "sticky" : "new", "window" : top_frame_2a, "command" : lambda:diaper_time("08:00:00", 'morning') }, 
                       # "Midday" : { "name" : "Midday", "column" :1, "row" :0, "sticky" : "new", "window" : top_frame_2a, "command" : lambda: custom_time_frame()},
                        "Afternoon" : { "name" : "Afternoon", "column" : 2, "row" :0, "sticky" : "new", "window" : top_frame_2a, "command" : lambda: diaper_time("14:00:00", 'afternoon')},
                        "Evening" : { "name" : "Evening", "column" : 3, "row" :0, "sticky" : "new", "window" : top_frame_2a, "command" : lambda: diaper_time("19:00:00", 'evening')},
                        "Night" : { "name" : "Night", "column" : 4, "row" :0, "sticky" : "new", "window" : top_frame_2a, "command" : lambda: diaper_time("23:00:00", 'night')}
                        }


    profile1 = {"profile " : { "name" : "Profile", "window" : top_frame_1, "column" : 0, "row" :0, "sticky" : "new", "command" : lambda: button_builder(xxx)}, 
                "Info" : { "name" : "Info",  "window" : top_frame_1, "column" : 0, "row" :1, "sticky" : "new", "command" : lambda: remove_buttons(sleep_menu)},
                 "Log In" : { "name" : "Log In", "window" : top_frame_1, "column" : 0, "row" :2, "sticky" : "new", "command" : lambda: remove_buttons(sleep_menu)},
                  }


#GUI INTERFACE FUNCTIONS :

    def clear_frame(frame):     #Clears frames of all widgets
        # print("from clear_frame",frame.winfo_children())
        for widget in frame.winfo_children()[1:]: #selects the widgets on the frame, 
            widget.destroy()                        #destroys all but TKINTER skin.
        
    def create_frame(grid):     #Places Specific frame on screen.
        grid['frame'].grid(column = grid['column'], padx = 5, pady = 2, row = grid['row'], columnspan = grid['columnspan'], rowspan = 3, sticky = grid['sticky']    )
        

    def forget_frame():
        for item in tframe_list:
            item.grid_forget()


    def create_combo(grid, frame, buttons):
        #combines 4 functions as one. Removes the frame, clears it,
        #recreates it with new buttons.  Used for 2nd column functions. 
        forget_frame()
        clear_frame(frame)        
        create_frame(grid)
        button_builder(buttons)

    


    def button_builder(button_list):  #creates and places buttons on screen
        for x in button_list.values():
            (x['button']) = ctk.CTkButton((x['window']), text_font = ("arial", 20),  text = x['name'], height = 50, command = x['command'])
            x['button'].grid(column = x['column'],pady = 10,padx = 3, row = x['row'], sticky = x['sticky'])
        #     all_open_buttons.update(button_list)
        # print("COUNT OF OPEN BUTTONS : \n",len(all_open_buttons))
        return button_list

    #Functions to create the bottle frames and log the information:
    def custom_time_frame():    #allows user to select the date/time and milk amount in oz. button press sets the time. 
    
        clear_frame(top_frame_2)
        create_frame(tframegrid2)
        

        how_much_label = ctk.CTkLabel(master = top_frame_2,text_font = ("arial", 12), text = "How many ounces of milk?")
        amount_slider = ctk.CTkSlider(master=top_frame_2, from_=0, to=12,number_of_steps = 24, command=slider_event)
        amount_entry_label = ctk.CTkLabel(master = top_frame_2, text_font = ("arial", 20), text = "6.0 oz ")
        collect_button = ctk.CTkButton(master = top_frame_2, text_font = ("arial", 12), text = "Set Time and Amount", command = lambda:get_datetime(amount_slider.get(),custom_time,custom_date) )

        how_much_label.grid(column = 0,  padx = 5, pady = 5, row =2, rowspan = 1)     
        amount_slider.grid(column = 1,  padx = 5, pady = 5, row = 2, rowspan = 1, columnspan=2)
        amount_entry_label.grid(column = 0, columnspan = 2,  padx = 5, pady = 5, row = 1, rowspan = 1)
        collect_button.grid(column = 0, row = 4, padx = 5, pady = 5, columnspan=2)

        custom_time = Collect_Time(top_frame_2)
        custom_date = Collect_Date(top_frame_2)
        
        custom_time.grid(column = 0, row = 0, rowspan= 1, padx = 5, pady = 5,)
        custom_date.grid(column = 1, row = 0, rowspan = 1, padx = 5, pady = 5,)
        # get_datetime(amount_slider)

    def get_datetime(ounces,custom_time,custom_date):
        #cleans up entered DATETIME into an object. Also, collects bottle info upon button hit. 
        custom_datetime_entry = f"{custom_date.year.get()}-{custom_date.month.get()}-{custom_date.day.get()} {custom_time.hour.get()}:{custom_time.min.get()}"
        bottles['milk_amount'] = ounces
        bottles['datetime'] = datetime.datetime.strptime(f"{custom_datetime_entry}","%Y-%m-%d %H:%M")
        final_summary_frame("bottle")
        return(ounces, custom_datetime_entry)

        # time_entry = Collect_Time(top_frame_2).grid(column = 0, row = 2, rowspan= 3, padx = 5, pady = 5,)
        # date_entry = Collect_Date(top_frame_2).grid(column = 1, row = 2, rowspan = 3, padx = 5, pady = 5,)

    def slider_event(value):    #activates whenever the slider is slid. collects value and updates the onscreen text.
            amount_entry_label = ctk.CTkLabel(master = top_frame_2, text_font = ("arial", 20), text = f"{value} oz")
            amount_entry_label.grid(column = 0,columnspan = 2,  padx = 5, pady = 5, row = 1, rowspan = 1)
            bottles['amount'] = value
            return value


    #Diaper Button Functions
    def yellow_press(): #when yellow diaper button is pressed.  - creates the morning, noon etc. buttons. Changes bg color. 
        clear_frame(top_frame_2a)
        create_frame(tframegrid2a)   
        button_builder(time_period_buttons)
        # if diapers['onetwo']:
        #     final_summary_frame("diaper")
        
        diapers['onetwo'] = 1
        top_frame_2a.configure(fg_color = '#e3dd20')



    def brown_press():
        clear_frame(top_frame_2a)
        create_frame(tframegrid2a)   
        button_builder(time_period_buttons)
        diapers['onetwo'] = 2
        
        top_frame_2a.configure(fg_color = '#715f1d')



    def sleep_button_press():
        clear_frame(top_frame_2)
        create_frame(tframegrid2)   
        final_summary_frame('sleep')

        def minute_slider_event(value):
            minute_label = ctk.CTkLabel(master = top_frame_2, text = f"{value} Minutes")
            minute_label.grid(column = 0,  padx = 5, pady = 5, row =1, rowspan = 1)     
        def hour_slider_event(value):
            hour_label = ctk.CTkLabel(master = top_frame_2, text = f"{value} Hours")
            hour_label.grid(column = 0,  padx = 5, pady = 5, row =3, rowspan = 1)     
            
        #labels : 
        how_long_sleep = ctk.CTkLabel(master = top_frame_2, text = "How long did the baby sleep for?")
        minute_label = ctk.CTkLabel(master = top_frame_2, text = "Minutes")
        hour_label = ctk.CTkLabel(master = top_frame_2, text = "Hours")

        #Sliders : 
        minute_slider = ctk.CTkSlider(master=top_frame_2, from_=0, to=60,number_of_steps = 12, command=minute_slider_event)
        hour_slider = ctk.CTkSlider(master=top_frame_2,  from_=0, to=16,number_of_steps = 32, command=hour_slider_event)
        
        #Grid Placement : 
        how_long_sleep.grid(column = 0,  padx = 5, pady = 5, row =0, rowspan = 1)
        minute_label.grid(column = 0,  padx = 5, pady = 5, row =1, rowspan = 1)     
        minute_slider.grid(column = 0,  padx = 5, pady = 5, row = 2, rowspan = 1, columnspan=1)

        hour_label.grid(column = 0,  padx = 5, pady = 5, row = 3, rowspan = 1)     
        hour_slider.grid(column = 0,  padx = 5, pady = 5, row = 4, rowspan = 1, columnspan=1)











# """DATA SUBMISSION BUTTONS"""
    def final_summary_frame(choice):  #Uses 3rd Tkinter frame. Provides summary of all entered data plus a submit button. 
        #'choice' is passed. It determines what is drawn in the 3rd frame: the bottle, sleep, or diaper choice.  
        # Opens the correct window depending.
        clear_frame(top_frame_3)
        create_frame(tframegrid3)
        onetwo = 1
        sleeptime =1
        
        if choice == "bottle":
            # bottles["datetime"] = datetime.datetime.now()
            # bottles['milk_amount'] = 6
            print(bottles["datetime"])
            date_entry = bottles['datetime'].strftime("%m-%d-%Y")
            time_entry = bottles['datetime'].strftime("%H:%M")
            bottle_summary_label = ctk.CTkLabel(master = top_frame_3,text_font = ("arial", 12), text = f"Summary:\n\n At {time_entry}\non\n{date_entry}, \n{all_data['name']} had:\n {bottles['milk_amount']} oz of MILK.").grid(column = 0, row = 0)
            button_text = "Enter Bottle"
            button_func = lambda: bottle_button()

        elif choice == "diaper":

            if diapers['onetwo'] == 1:
                diapercolor = "yellow"
            else : 
                diapercolor = "brown"
            bottle_summary_label = ctk.CTkLabel(master = top_frame_3,text_font = ("arial", 12), text = f"Summary:\n\n During the\n{diapers['time_of_day']},\n{all_data['name']} had \n a {diapercolor} diaper. \n ").grid(column = 0, row = 0)
            button_text = "Enter Diaper"
            button_func = lambda:sql_diaper()
        elif choice == "sleep":
            bottle_summary_label = ctk.CTkLabel(master = top_frame_3,text_font = ("arial", 12), text =f"Summary:\n\n {all_data['name']} slept \n for X TIME \n until HH:MM").grid(column = 0, row = 0)
            button_text = "Enter Sleep"
            button_func = lambda: sql_sleep(sleeptime)
        submit_bottle_button = ctk.CTkButton(master = top_frame_3, text = button_text, command = button_func)

        # top_frame_3.grid(column = 3,  padx = 5, pady = 5, row = 0, rowspan = 3)
        # bottle_summary_label.grid(column = 0, row = 0)
        submit_bottle_button.grid(column = 0, row = 1)










#     def final_summary_frame(choice):  #3rd frame. Provides summary and enter button. 
#         #A 'choice' is passed. It is the bottle, sleep, or diaper choice.  
#         # Opens the correct window depending.
#         clear_frame(top_frame_3)
#         create_frame(tframegrid3)
#         if choice == "bottle":
#             button_text = "Enter Bottle"
#             button_func = lambda: bottle_button()
#             dt = bottles['datetime']

#             final_sum_text = f"Summary\n {all_data['name']} had:\n {bottles['milk_amount']} oz of MILK\n at {dt.hour}:{dt.min}\non\n{dt.month} {dt.day}, {dt.year}"
            
#             submit_bottle_button = ctk.CTkButton(master = top_frame_3, text = button_text, command = button_func)
#             submit_bottle_button.grid(column = 0, row = 1)


#         elif choice == "diaper":
#             if diapers['onetwo'] == 1:
#                 diapercolor = "yellow"
#             else : 
#                 diapercolor = "brown"
#             button_text = "Enter Diaper"
#             button_func = lambda:sql_diaper()
#             final_summary_label = ctk.CTkLabel(master = top_frame_3, text = f"Summary\n {all_data['name']} had \n a {diapercolor} diaper \n in the { diapers['time_of_day']} ")
#             final_summary_label.grid(column = 0, row = 0)
#             submit_bottle_button = ctk.CTkButton(master = top_frame_3, text = button_text, command = button_func)
#             submit_bottle_button.grid(column = 0, row = 1)

#         elif choice == "sleep":
#             button_text = "Enter Sleep"
#             button_func = lambda: sql_sleep(sleeptime)
#             final_summary_label = ctk.CTkLabel(master = top_frame_3, text =f"Summary\n {all_data['name']} slept \n for X TIME \n until HH:MM")
#             final_summary_label.grid(column = 0, row = 0)
#             submit_bottle_button = ctk.CTkButton(master = top_frame_3, text = button_text, command = button_func)
#             submit_bottle_button.grid(column = 0, row = 1)


#         final_summary_label = ctk.CTkLabel(master = top_frame_3, text = final_sum_text)
#         final_summary_label.grid(column = 0, row = 0)

#         # submit_bottle_button = ctk.CTkButton(master = top_frame_3, text = button_text, command = button_func)
        
#         top_frame_3.grid(column = 3,  padx = 5, pady = 5, row = 0, rowspan = 3)
#         # final_summary_label.grid(column = 0, row = 0)
#         # submit_bottle_button.grid(column = 0, row = 1)



        # def frame3_widgets(label,button_text,button_func):
        #     submit_bottle_button = ctk.CTkButton(master = top_frame_3, text = button_text, command = button_func)
            
        #     top_frame_3.grid(column = 3,  padx = 5, pady = 5, row = 0, rowspan = 3)
        #     final_summary_label.grid(column = 0, row = 0)
        #     submit_bottle_button.grid(column = 0, row = 1)

        #how to submit ? 


    def diaper_time(time, daytime):
        #called from diaper 'morning, afternoon, etc. buttons. 
        #enters a generic time for the buttons. 
        diaper_time = f"{datetime.date.today()} {time}"
        diapers['datetime']= diaper_time
        diapers['time_of_day']= daytime
        print(diaper_time,daytime)
        final_summary_frame("diaper")
        format  = "%Y-%m-%d %H:%M:%S"
        local_dt = datetime.datetime.strptime(diaper_time, format)
        print("local", local_dt)

        dt_utc = local_dt.astimezone(pytz.UTC)
        print('Datetime in UTC Time zone: ', dt_utc)
        dt_utc_str = dt_utc.strftime(format)
        print('Datetime string in UTC Time zone: ', dt_utc_str)


    def bottle_button():    
        #Enters data into Bottle Table
        cursor.execute("INSERT INTO bottle ( babyID, datetime, utc, amount, product, product_id) VALUES (?,?,?,?,?,?)",
                    [all_data['baby'], datetime.datetime.now(), time.time(), bottles['amount'], 'Powder Milk', 801])
        database.commit()
        print("Bottle Logged")



    def sql_diaper(): 
        #Enters data into Diaper Table
        cursor.execute("INSERT INTO diaper (babyID, datetime, onetwo) VALUES (?,?,?)",
                        [all_data['baby'], diapers['datetime'], diapers['onetwo']])
        database.commit()
        print("Diaper Logged")



    def sql_sleep(sleeptime):
        #Enters data into Sleep Table
        cursor.execute("INSERT INTO sleep (babyID, datetime, utc, onetwo) VALUES (?,?,?,?)",
            [all_data['baby'], datetime.datetime.now(), time.time(),time])
        database.commit()
        print("Sleep Logged")


    #make babyID = a variable.  But... how do I do it with the username? 
    # How do I match the username with the baby?






    button_builder(main_menu)
    print("all_data" ,all_data['name'])



if __name__ == '__main__':
    window_main(root,all_data)



