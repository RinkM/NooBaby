

# NEW NOTES - Trying to use macslate to convert datetime to UTC.  Can't remember how...
# Trying to create the submit buttons

# reorganize SQL - make it so important info is first.   




"""
3/31 
with sql and log in.    need to get through the log in gate to get into the program. the log in runs first? 
if it succeeds, it creates the program.  
stores the userID and babyID so it can always be accessed. 



Goals for the future - 
THink about making the API by itself in it's own application.  Finish the SQL THINGS. Then look up API what I have...
How to turn this into website with flask.  Use that to change the visuals again.  It will need to be updated.

Use panda / numpy etc. practice with duolingo data? maybe?



"""

#for check for users funcation at end.  how do I get to draw the buttons?   
#does it need to return something?    while loop to check the profile..?something like that?  
#data in username location breaks the loop?   creates the drawbutton function?   maybe....

# OTHER GUI
# https://ttkbootstrap.readthedocs.io/en/latest/#features

# TO DO
#Add time to the sleep button.
# can i fix time entry?
#diaper buttons (day of week)   turn the time on behind them.
# work on bottom Grid placement    put something in there. A picture?  
# work on variables for summary tabs
# work on sleep button - How long what time wake up ?     Long sleep , short sleep - changes the slider amount. 
#work on data entry / writing.   How to make accurate?   use a list?   add to it as button is pressed. 
# enter the list into db.
#first time user profile.   make a simple one.  baby name. Baby age.  
# baby profile?  How to create?   Entry information?  think dischord



##########################################
##################### MAIN MENU ######################
##########################################


def main1():
    
    #my other programs : 
    # from NooB_Profile import main as profilee
    import NooB_Profile
    import NooB_MakeDB

    import tkinter as tk, customtkinter as ctk
    import random #For the bottle notice. 
    import sqlite3, datetime, time, uuid
    from os.path import exists
    import tkcalendar as tkcal


    database = sqlite3.connect('noob_database.db')
    cursor = database.cursor()




    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    
    root = ctk.CTk() 
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
    bottom_frame_1 = ctk.CTkFrame(master = bottom_frame_master, corner_radius = 20)
    bottom_frame_2 = ctk.CTkFrame(master = bottom_frame_master, corner_radius = 20)
    bottom_frame_2a = ctk.CTkFrame(master = bottom_frame_master, corner_radius = 20)
    bottom_frame_3 = ctk.CTkFrame(master = bottom_frame_master, corner_radius = 20)
    

    # background_image = tkinter.PhotoImage (file = 'sleep-cycles.png')
    # background_label = tkinter.Label(bottom_frame_master, image = background_image)
    # background_label.place(anchor = "n", relx = .5, rely = 0)

    # bottom_frame_master.grid_propagate(1) #makes width and height matter.

    #List of instructions to place frames on screen.
    tframegrid1 = {"frame": top_frame_1, "column" : 1, "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}
    tframegrid2 ={"frame": top_frame_2, "column" : 2,  "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}
    tframegrid2a = {"frame": top_frame_2a, "column" : 2,  "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}
    tframegrid3 = {"frame": top_frame_3, "column" : 3,  "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}
    bframegrid = {"frame": bottom_frame_master, "column" : 1,  "padx" : 5, "pady" : 5, "row" : 3, "columnspan" : 3, "rowspan" : 3, "sticky": 'ew'}
    bframegrid1 = {"frame": bottom_frame_1, "`column" :0, "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}
    bframegrid2 ={"frame": bottom_frame_2, "column" : 1,  "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}
    bframegrid2a = {"frame": bottom_frame_2a, "column" : 1,  "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}
    bframegrid3 = {"frame": bottom_frame_3, "column" : 2,  "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}

    bottom_left = ctk.CTkLabel(master = bottom_frame_master, text = "Food Info \nWill Be Displayed Here")
    bottom_center = ctk.CTkLabel(master = bottom_frame_master, text = "Sleep Info \nWill Be Displayed Here")
    bottom_right = ctk.CTkLabel(master = bottom_frame_master, text = "Milestone Info \nWill Be Displayed Here")
    

    # bottom_frame_master.columnconfigure(0, minsize=297)
    # bottom_frame_master.columnconfigure(1,minsize=297)
    # bottom_frame_master.columnconfigure(2,minsize=297)
    
    # top_frame_1.columnconfigure(0,minsize = 200)
    def bottom_frame():
        bottom_frame_master.grid(column = 1, row = 2, columnspan = 3, rowspan = 3,  )
        bottom_left.grid(column = 0, row = 0, sticky = 'ns')
        bottom_center.grid(column = 1, row = 0)
        bottom_right.grid(column = 2, row = 0)
    


#TIME COLLECTION CLASSES




    class Collect_Date(ctk.CTkFrame):
        def __init__(self,parent):
            super().__init__(parent)
            # self.geometry("600x500")



            month = time.strftime("%m")
            day = time.strftime("%d")
            year = time.strftime("%Y")
            create_frame(tframegrid2)


            enter_date_label = ctk.CTkLabel(master = top_frame_2, text = "Enter Date")
            

            self.reg=self.register(self.month_valid) #not sure about register. refers to the method below. 
            self.monthstr=tk.StringVar(self,f"{month}")    #sets the number in the box.  could be current time. 
            self.month = tk.Spinbox(self,from_=0,to=12, 
                                    wrap=True,validate='focusout', validatecommand=(self.reg,'%P'),
                                    invalidcommand=self.month_invalid, textvariable=self.monthstr,width=2,
                                    font = "arial, 20", fg = "#eae6f5",
                                    buttonbackground = "#000000", bd =2, bg = "#000000", 
                                    
                                    )
            
            self.reg2=self.register(self.day_valid)
            
            
            self.daystr=tk.StringVar(self,f'{day}')
            self.day = tk.Spinbox(self,from_=0,to=31,wrap=True,validate='focusout',
                                    validatecommand=(self.reg2,'%P'),
                                    invalidcommand=self.day_invalid,textvariable=self.daystr,
                                    width=2, font = "arial, 20", fg = "#eae6f5",
                                    buttonbackground = "#000000", bd =2, bg = "#000000", 
                                    
                                    )

            self.reg3=self.register(self.year_valid)
            self.yearstr=tk.StringVar(self,f'{year}')
            self.year = tk.Spinbox(self,from_=2021,to=2030,wrap=True,validate='focusout',
                                    validatecommand=(self.reg3,'%P'),
                                    invalidcommand=self.year_invalid,textvariable=self.yearstr,
                                    width=4, font = "arial, 20", fg = "#eae6f5",
                                    buttonbackground = "#000000", bd =2, bg = "#000000", 
                                    
                                    )

                                    #I ADDED a lot of what's below.  It can be more better...
                                    # https://stackoverflow.com/questions/57034118/time-picker-for-tkinter


            baby_bday_button = ctk.CTkButton(self, text = "Enter", command = lambda:get_time(self.month,self.day, self.year))
            
            def get_time(month, day, year):
                print (self.monthstr, self.daystr, self.yearstr)
                time_entered = f"{month.get()}/{day.get()}/{year.get()}"
                print("get_time - returns:", time_entered)
                return(time_entered)

            enter_date_label.grid(column=1, row =1)
            
            self.month.grid(row=2,column=0)
            self.day.grid(row=2,column=1)
            self.year.grid(row=2,column=2)
            baby_bday_button.grid(row=3,column=0, columnspan = 3)
            
            get_month = self.month.get()
            get_day = self.day.get()
            get_year = self.year.get()
            time_entered = f"{self.month.get()}:{self.day.get()}/{self.year.get()}"
            print(time_entered)
            print(get_month, get_day)
            
        def month_invalid(self):
            self.monthstr.set('6')
        def month_valid(self,input):
            if (input.isdigit() and int(input) in range(12) and len(input) in range(1,3)):
                valid = True
            else:
                valid = False
            if not valid:
                self.month.after_idle(lambda: self.month.config(validate='focusout'))
            return valid
        def day_invalid(self):
            self.daystr.set('15')
        def day_valid(self,input):
            if (input.isdigit() and int(input) in range(31) and len(input) in range(1,3)):
                valid = True
            else:
                valid = False
            if not valid:
                self.day.after_idle(lambda: self.day.config(validate='focusout'))
            return valid
        
        def year_invalid(self):
            self.yearstr.set('2022')
        def year_valid(self,input):
            if (input.isdigit() and int(input) in range(2021,2030) and len(input) in range(4)):
                valid = True
            else:
                valid = False
            if not valid:
                self.year.after_idle(lambda: self.year.config(validate='focusout'))
            return valid
        


    class Collect_Time(ctk.CTkFrame):
        def __init__(self,parent):
            super().__init__(parent)
            # self.geometry("600x500")
            # create_frame(tframegrid2)

            #USE STRPTIME TO GET THE DATE TO LOOK RIGHT

            enter_date_label = ctk.CTkLabel(master = top_frame_2, text = "Enter Time")
            

            min = time.strftime("%M")
            hour = time.strftime("%H")
            self.reg=self.register(self.hour_valid) #not sure about register. refers to the method below. 
            self.hourstr=tk.StringVar(self,f"{hour}")    #sets the number in the box.  could be current time. 
            self.hour = tk.Spinbox(self,from_=0,to=23, 
                                    wrap=True,validate='focusout', validatecommand=(self.reg,'%P'),
                                    invalidcommand=self.hour_invalid, textvariable=self.hourstr,width=2,
                                    font = "arial, 20", fg = "#eae6f5",
                                    buttonbackground = "#000000", bd =2, bg = "#000000", 
                                    
                                    )
            
            self.reg2=self.register(self.min_valid)
            
            
            self.minstr=tk.StringVar(self,f'{min}')
            self.min = tk.Spinbox(self,from_=00,to=59,wrap=True,validate='focusout',
                                    validatecommand=(self.reg2,'%P'),
                                    invalidcommand=self.min_invalid,textvariable=self.minstr,
                                    width=2, font = "arial, 20", fg = "#eae6f5",
                                    buttonbackground = "#000000", bd =2, bg = "#000000", 
                                    )

                                    #I ADDED a lot of what's below.  It can be more better...
                                    # https://stackoverflow.com/questions/57034118/time-picker-for-tkinter


            baby_bday_button = ctk.CTkButton(self, width = 100, text = "Enter", command = lambda:get_time())
            
            def get_time():
                time_entered = f"{self.hour.get()}:{self.min.get()}"
                print("get_time - returns:", time_entered)
                return(time_entered)


            enter_date_label.grid(column=0, row = 1)    
            
            self.hour.grid(row=2,column=0)
            self.min.grid(row=2,column=1)
            
            baby_bday_button.grid(row=3,column=0, columnspan = 2)
            get_hour = self.hour.get()
            get_min = self.min.get()
            time_entered = f"{self.hour.get()}:{self.min.get()}"
            print(time_entered)
            print(get_hour, get_min)
            
        def hour_invalid(self):
            self.hourstr.set('10')
        def hour_valid(self,input):
            if (input.isdigit() and int(input) in range(24) and len(input) in range(1,3)):
                valid = True
            else:
                valid = False
            if not valid:
                self.hour.after_idle(lambda: self.hour.config(validate='focusout'))
            return valid
        def min_invalid(self):
            self.minstr.set('30')
        def min_valid(self,input):
            if (input.isdigit() and int(input) in range(60) and len(input) in range(1,3)):
                valid = True
            else:
                valid = False
            if not valid:
                self.min.after_idle(lambda: self.min.config(validate='focusout'))
            return valid
        
        # def get_time(self):
        #     time = f"{self.min.get():self.hour.get()}"
        #     return print(time)





    # List of Buttons
    main_menu = {"food_button" : {"name" : "Food", "window" : root, "column" : 0, "row" :0, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1,food_menu1)},
            "sleep_button" : {"name" : "Sleep", "window" : root, "column" : 0, "row" :1, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1, sleep_menu1)},
            "diaper_button" : {"name" : "Diaper", "window" : root, "column" : 0, "row" :2, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1, diaper_menu1)},
            "milestones" : {"name" : "Milestones", "window" : root, "column" : 0, "row" :3, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1, milestones1)},
            "activities" : {"name" : "Activities", "window" : root, "column" : 0, "row" :4, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1, activities1)},
            "profile_button" : {"name" : "Profile", "window" : root, "column" : 0, "row" :5, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1, profile1)},
            }

    food_menu1 = {"Liquid" : { "name" : "Liquid", "window" : top_frame_1, "column" : 0, "row" :0, "sticky" : "new", "command" : lambda:current_time_frame() }, 
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


    time_period_buttons = {"Morning" : { "name" : "Morning",  "column" :0, "row" :0, "sticky" : "new", "window" : top_frame_2a, "command" : lambda:get_time_period("08:00:00", 'morning') }, 
                       # "Midday" : { "name" : "Midday", "column" :1, "row" :0, "sticky" : "new", "window" : top_frame_2a, "command" : lambda: custom_time_frame()},
                        "Afternoon" : { "name" : "Afternoon", "column" : 2, "row" :0, "sticky" : "new", "window" : top_frame_2a, "command" : lambda: get_time_period("14:00:00", 'afternoon')},
                        "Evening" : { "name" : "Evening", "column" : 3, "row" :0, "sticky" : "new", "window" : top_frame_2a, "command" : lambda: get_time_period("19:00:00", 'evening')},
                        "Night" : { "name" : "Night", "column" : 4, "row" :0, "sticky" : "new", "window" : top_frame_2a, "command" : lambda: get_time_period("23:00:00", 'night')}
                        }


    profile1 = {"profile " : { "name" : "Profile", "window" : top_frame_1, "column" : 0, "row" :0, "sticky" : "new", "command" : lambda: button_builder(xxx)}, 
                "Info" : { "name" : "Info",  "window" : top_frame_1, "column" : 0, "row" :1, "sticky" : "new", "command" : lambda: remove_buttons(sleep_menu)},
                 "Log In" : { "name" : "Log In", "window" : top_frame_1, "column" : 0, "row" :2, "sticky" : "new", "command" : lambda: remove_buttons(sleep_menu)},
                  }








    def clear_frame(frame):     #Clears frames of all widgets
        print("from clear_frame",frame.winfo_children())
        for widget in frame.winfo_children()[1:]: #selects the widgets on the frame, 
            widget.destroy()                        #destroys all but canvas
        
    def create_frame(grid):     #Places frame on screen.
        grid['frame'].grid(column = grid['column'], padx = 5, pady = 2, row = grid['row'], columnspan = grid['columnspan'], rowspan = 3, sticky = grid['sticky']    )
        

    def forget_frame():
        for item in tframe_list:
            item.grid_forget()


    def create_combo(grid, frame, buttons):
        forget_frame()
        clear_frame(frame)        
        create_frame(grid)
        button_builder(buttons)

    


    def button_builder(button_list):
        for x in button_list.values():
            (x['button']) = ctk.CTkButton((x['window']), text_font = ("arial", 20),  text = x['name'], height = 50, command = x['command'])
            x['button'].grid(column = x['column'],pady = 10,padx = 3, row = x['row'], sticky = x['sticky'])
        #     all_open_buttons.update(button_list)
        # print("COUNT OF OPEN BUTTONS : \n",len(all_open_buttons))
        return button_list


    #Submits data to database. uses the button input to submit data to sqlite.  #need to fix the variables. 
    def bottle_button():    
        id = random.randint(30,40000)
        cursor.execute("INSERT INTO bottle (bottle_num, datetime, utc, amount, baby_id, product, product_id) VALUES (?,?,?,?,?,?,?)",
                    [id, datetime.datetime.now(), time.time(), 180, 803, 'Powder Milk', 100])
        database.commit()
        print("Bottle Data Captured")


    def current_time_frame():   #displays current time and allows you to edit it. 
        
        clear_frame(top_frame_2)
        create_frame(tframegrid2)
        bottle_summary_frame("bottle")

        how_much_label = ctk.CTkLabel(master = top_frame_2, text = "How much milk?")
        
        def slider_event(value):
            amount_entry_label = ctk.CTkLabel(master = top_frame_2, text = f"{value} oz")
            amount_entry_label.grid(column = 0,  padx = 5, pady = 5, row = 0, rowspan = 1)
        
        
        amount_slider = ctk.CTkSlider(master=top_frame_2, from_=0, to=12,number_of_steps = 12, command=slider_event)
        time_entry_label = ctk.CTkLabel(master = top_frame_2, text = "TIME:")
        date_entry_label = ctk.CTkLabel(master = top_frame_2, text = "DATE:")

        this_time = time.strftime("%H:%M")
        this_date = time.strftime("%m/%d/%Y")
        current_time_label = ctk.CTkLabel(master = top_frame_2, text = this_time)
        current_date_label = ctk.CTkLabel(master = top_frame_2, text = this_date)
        custom_time_button = ctk.CTkButton(master = top_frame_2, text = "Use a custom time", command = lambda: custom_time_frame())
        
        how_much_label.grid(column = 0,  padx = 5, pady = 5, row =0, rowspan = 1)     
        amount_slider.grid(column = 1,  padx = 5, pady = 5, row = 0, rowspan = 1, columnspan=2)

        time_entry_label.grid(column = 0, row = 1)
        date_entry_label.grid(column = 0, row = 2)

        current_time_label.grid(column = 1, row = 1)
        current_date_label.grid(column = 1, row = 2)

        custom_time_button.grid(column = 0, row = 3, columnspan = 2)


    def custom_time_frame():    #allows you to adjust the time you enter. 
    
        clear_frame(top_frame_2)
        create_frame(tframegrid2)
        bottle_summary_frame("bottle")

        how_much_label = ctk.CTkLabel(master = top_frame_2, text = "How much milk?")
        
        def slider_event(value):
            amount_entry_label = ctk.CTkLabel(master = top_frame_2, text = f"{value} oz")
            amount_entry_label.grid(column = 0,  padx = 5, pady = 5, row = 0, rowspan = 1)

        amount_slider = ctk.CTkSlider(master=top_frame_2, from_=0, to=12,number_of_steps = 24, command=slider_event)


        how_much_label.grid(column = 0,  padx = 5, pady = 5, row =0, rowspan = 1)     
        amount_slider.grid(column = 1,  padx = 5, pady = 5, row = 0, rowspan = 1, columnspan=2)

        time_entry = Collect_Time(top_frame_2).grid(column = 0, row = 2, rowspan= 3, padx = 5, pady = 5,)
        date_entry = Collect_Date(top_frame_2).grid(column = 1, row = 2, rowspan = 3, padx = 5, pady = 5,)
        # print(time_entry.hour.get())
        


        # hour_entry = ctk.CTkEntry(master=top_frame_2, 
        #                     width = 35,
        #                     placeholder_text=time.strftime("%H"))
        # minute_entry = ctk.CTkEntry(master=top_frame_2, 
        #                     width = 35,
        #                     placeholder_text=time.strftime("%M"))
        # day_entry = ctk.CTkEntry(master=top_frame_2, 
        #                     width = 35,
        #                     placeholder_text=time.strftime("%m"))
        # month_entry = ctk.CTkEntry(master=top_frame_2, 
        #                     width = 35,
        #                     placeholder_text=time.strftime("%d"))
        # year_entry = ctk.CTkEntry(master=top_frame_2, 
        #                     width = 45,
        #                     placeholder_text=time.strftime("%Y"))

        # time_entry_label = ctk.CTkLabel(master = top_frame_2, text = "TIME:")
        # date_entry_label = ctk.CTkLabel(master = top_frame_2, text = "DATE:")
        # use_current_time_button = ctk.CTkButton(master = top_frame_2, text = "Use current time", command = lambda: current_time_frame())



        # time_entry_label.grid(column = 0, row = 1)
        # date_entry_label.grid(column = 0, row = 2)

        # hour_entry.grid(column= 1, row = 1)
        # minute_entry.grid(column= 2, row = 1)
        # day_entry.grid(column= 1, row = 2)
        # month_entry.grid(column= 2, row = 2)
        # year_entry.grid(column= 3, row = 2)
        
        # use_current_time_button.grid(column = 0, row = 3, columnspan = 2)

        # Functions to store USERNAME / PAssword profoile information. 
    def store_baby_data(babyname,babybday):
        # print(["baby_profile", "Profile_NUM", str(datetime.datetime.now()), time.time(), baby_uuid, babyname, babybday, user_uuid])

        cursor.execute("INSERT INTO baby_profile (table_id, profile_num, datetime, utc, baby_id, baby_name, birthdate_time, unique_user_str) VALUES (?,?,?,?,?,?,?,?)",
            ["baby_profile", "Profile_NUM", datetime.datetime.now(), time.time(), baby_uuid, babyname, babybday, user_uuid])
        database.commit()

    def store_user_data(username):
        cursor.execute("INSERT INTO user_profile (table_id, unique_user_str, datetime, utc, username) VALUES (?,?,?,?,?)",
                ["user_profile", user_uuid, datetime.datetime.now(), time.time(), username])
        database.commit()

        
    diaperStatus = 0
    diaper_summary_time = ""
    #it's not updating the window.  need to regrid?

    def bottle_summary_frame(choice):  #3rd frame. Provides summary and enter button. 
        
        clear_frame(top_frame_3)
        create_frame(tframegrid3)
        # time_summary = 
        # date_summary = 
        
        if choice == "bottle":
            bottle_summary_label = ctk.CTkLabel(master = top_frame_3, text = "Summary\n BABYNAME had:\n XAMOUNT of XPRODUCT\n at HH:MM\nMM-DD-YYYY")
            button_text = "Enter Bottle"
        elif choice == "diaper":
            bottle_summary_label = ctk.CTkLabel(master = top_frame_3, text = f"Summary\n BABYNAME had \n a COLOR diaper \n in the {diaper_summary_time}")
            button_text = "Enter Diaper"
        elif choice == "sleep":
            bottle_summary_label = ctk.CTkLabel(master = top_frame_3, text = "Summary\n BABYNAME slept \n for X TIME \n until HH:MM")
            button_text = "Enter Sleep"

        
        submit_bottle_button = ctk.CTkButton(master = top_frame_3, text = button_text, command = lambda : bottle_button())
        
        top_frame_3.grid(column = 3,  padx = 5, pady = 5, row = 0, rowspan = 3)
        bottle_summary_label.grid(column = 0, row = 0)
        submit_bottle_button.grid(column = 0, row = 1)

        #how to submit ? 


    # diaper time



    # diaper, table_id, diaper_num, datetime, utc, onetwo, baby_id
    def sql_diaper(diaperStatus, babyuuid): 
        cursor.execute("INSERT INTO diaper (table_id, datetime, utc, onetwo, baby_id) VALUES (?,?,?,?,?)",
        ["diaper", datetime.datetime.now(), time.time(), diaperStatus, BABYID_GET])

    def get_time_period(time, daytime):
        diaper_time = f"{datetime.date.today()} {time}"
        diaper_summary_time = daytime
        print(diaper_time,diaper_summary_time)

    #make babyID = a variable.  But... how do I do it with the username? 
    # How do I match the username with the baby?


    def yellow_press():
        clear_frame(top_frame_2a)
        create_frame(tframegrid2a)   
        button_builder(time_period_buttons)
        bottle_summary_frame("diaper")
        diaperStatus = 1
        top_frame_2a.configure(fg_color = '#e3dd20')
        

        

    def brown_press():
        clear_frame(top_frame_2a)
        create_frame(tframegrid2a)   
        button_builder(time_period_buttons)
        diaperStatus = 2
        bottle_summary_frame("diaper")
        top_frame_2a.configure(fg_color = '#715f1d')



    def sleep_button_press():
        clear_frame(top_frame_2)
        create_frame(tframegrid2)   
        bottle_summary_frame('sleep')

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
    
    



    
    # def check_for_user():
    #     cursor.execute("SELECT * FROM user_profile")
    #     user= cursor.fetchall()
    #     print(type(user))
    #     print('user', (user))
    #     if user==[]:
    #         NooB_Profile.main(root)


            

        
        # else:
        #     
            






    ####PROGRAM LOOP HERE########



    # button_builder(main_menu)
    # check_for_user()
    NooB_Profile.main(root)
    root.mainloop()





if __name__ == '__main__':
    main1()



# #the list of columns  - 
# The entry code for the database. Each table's code.

# # def bottle_button():    
# #     id = random.randint(30,4000)
#     # bottle_num, datetime, utc, amount, baby_id, product, product_id
#     cursor.execute("INSERT INTO bottle3 (bottle_num, datetime, utc, amount, baby_id, product, product_id) VALUES (?,?,?,?,?,?,?)",
#                 [id, datetime.datetime.now(), time.time(), 180, 803, 'Powder Milk', 100])

# # diaper, table_id, diaper_num, datetime, utc, onetwo, baby_id
#     cursor.execute("INSERT INTO diaper (diaper, table_id, diaper_num, datetime, utc, onetwo, baby_id) VALUES (?,?,?,?,?,?,?)",
#                 [id, datetime.datetime.now(), time.time(), 180, 803, 'Powder Milk', 100])

# # sleep, table_id, bottle_num, datetime, utc, start_time, end_time, duration, baby_id
#     cursor.execute("INSERT INTO sleep (table_id, bottle_num, datetime, utc, start_time, end_time, duration, baby_id) VALUES (?,?,?,?,?,?,?,?)",
#                 [id, datetime.datetime.now(), time.time(), 180, 803, 'Powder Milk', 100])

# # solid_food, table_id, solid_food_num, datetime, utc, baby_id, food_name, amount
#     cursor.execute("INSERT INTO solid_food (table_id, solid_food_num, datetime, utc, baby_id, food_name, amount) VALUES (?,?,?,?,?,?,?)",
#                 [id, datetime.datetime.now(), time.time(), 180, 803, 'Powder Milk', 100])

# # milestones, table_id, stone_num, stone_name, stone_description, stone_acheived, stone_text_achieve, datetime, utc, baby_id
#     cursor.execute("INSERT INTO milestones (table_id, stone_num, stone_name, stone_description, stone_acheived, stone_text_achieve, datetime, utc, baby_id) VALUES (?,?,?,?,?,?,?,?,?)",
#                 [id, datetime.datetime.now(), time.time(), 180, 803, 'Powder Milk', 100])

# # baby_profile, table_id, profile_num, datetime, utc, baby_id, baby_name, birthdate_utc, birthdate_time, sex, unique_user_str, unique_user
#     baby_UUID = uuid.uuid4()
#     cursor.execute("INSERT INTO baby_profile (table_id, profile_num, datetime, utc, baby_id, baby_name, birthdate_utc, birthdate_time, sex, unique_user_str) VALUES (?,?,?,?,?,?,?,?,?,?)",
#                 [TABLE_ID_GET, Profile NUM, datetime.datetime.now(), time.time(), baby_UUID, BABY_NAME_GET, BIRTHDAY_GET, BIRTHDAY_GETTIME, UNIQUE USER ID FROM OTHER TABLE])

# # user_profile, table_id, unique_user_str, unique_user, user_num, datetime, utc, baby_id, username, password
# user_uuid = uuid.uuid4()

#     cursor.execute("INSERT INTO user_profile (table_id, unique_user_str, datetime, utc, username) VALUES (?,?,?,?,?)",
#                 [TABLE ID???, user_uuid, datetime.datetime.now(), time.time(), USER_NAME_GET])

# pass

# import uuid
# user_uuid = uuid.uuid4()

#     database.commit()
#     print("Bottle Data Captured")



# # ()
















