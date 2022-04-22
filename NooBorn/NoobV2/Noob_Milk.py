


def main(root, all_data):


    import tkinter as tk, customtkinter as ctk
    import sqlite3, datetime, time, uuid
    import tkcalendar as tkcal
    from noob_buttons import button_builder, create_frame, clear_frame
    from Noob_Summary import final_summary_frame

    top_frame_2 = ctk.CTkFrame(master = root, corner_radius = 20)
    tframegrid2 ={"frame": top_frame_2, "column" : 2,  "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}



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
        all_data['milk_amount'] = ounces
        all_data['milk_datetime'] = datetime.datetime.strptime(f"{custom_datetime_entry}","%Y-%m-%d %H:%M")
        final_summary_frame("bottle")
        return(ounces, custom_datetime_entry)

        # time_entry = Collect_Time(top_frame_2).grid(column = 0, row = 2, rowspan= 3, padx = 5, pady = 5,)
        # date_entry = Collect_Date(top_frame_2).grid(column = 1, row = 2, rowspan = 3, padx = 5, pady = 5,)

    def slider_event(value):    #activates whenever the slider is slid. collects value and updates the onscreen text.
            amount_entry_label = ctk.CTkLabel(master = top_frame_2, text_font = ("arial", 20), text = f"{value} oz")
            amount_entry_label.grid(column = 0,columnspan = 2,  padx = 5, pady = 5, row = 1, rowspan = 1)
            all_data['milk_amount'] = value
            return value

    custom_time_frame()







if __name__ == '__main__':
    main()











