import customtkinter as ctk
import tkcalendar as tkcal
import time
import tkinter as tk


min = time.strftime("%M")
hour = time.strftime("%H")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk() 
root.geometry("1024x576")
root.resizable(width=False, height=False)
root.title("NooBorn Test Window")
print ("rootsize", root.bbox())


top_frame_2 = ctk.CTkFrame(master = root, corner_radius = 20) 
tframegrid2 ={"frame": top_frame_2, "column" : 2, 
             "padx" : 5, "pady" : 5, "row" : 0,
             "columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}

def create_frame(grid):     #Places frame on screen.
    grid['frame'].grid(column = grid['column'],
    padx = 5, pady = 2, row = grid['row'], 
    columnspan = grid['columnspan'], rowspan = 3, 
    sticky = grid['sticky']    
    )





class Collect_Date(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        # self.geometry("600x500")



        month = time.strftime("%m")
        day = time.strftime("%d")
        year = time.strftime("%Y")
        create_frame(tframegrid2)


        enter_date_label = ctk.CTkLabel(master = top_frame_2, text = "Enter Date")
        enter_date_label.grid(column=0, row = 0)

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
            time_entered = f"{month.get()}:{day.get()}/{year.get()}"
            print("get_time - returns:", time_entered)
            return(time_entered)

        baby_bday_button.grid(row=2,column=0, columnspan = 3)
        self.month.grid(row=1,column=0)
        self.day.grid(row=1,column=1)
        self.year.grid(row=1,column=2)
        
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
    

    # def get_time(self):
    #     time = f"{self.min.get():self.month.get()}"
    #     return print(time)
        
# root = ctk.CTk() 


# class Collect_Time(ctk.CTkFrame):
#     def __init__(self,parent):
#         super().__init__(parent)
#         # self.geometry("600x500")
#         create_frame(tframegrid2)
#         self.reg=self.register(self.hour_valid) #not sure about register. refers to the method below. 
#         self.hourstr=tk.StringVar(self,f"{hour}")    #sets the number in the box.  could be current time. 
#         self.hour = tk.Spinbox(self,from_=0,to=23, 
#                                 wrap=True,validate='focusout', validatecommand=(self.reg,'%P'),
#                                 invalidcommand=self.hour_invalid, textvariable=self.hourstr,width=2,
#                                 font = "arial, 20", fg = "#eae6f5",
#                                 buttonbackground = "#000000", bd =2, bg = "#000000", 
                                
#                                 )
          
#         self.reg2=self.register(self.min_valid)
        
        
#         self.minstr=tk.StringVar(self,f'{min}')
#         self.min = tk.Spinbox(self,from_=0,to=59,wrap=True,validate='focusout',
#                                 validatecommand=(self.reg2,'%P'),
#                                 invalidcommand=self.min_invalid,textvariable=self.minstr,
#                                 width=2, font = "arial, 20", fg = "#eae6f5",
#                                 buttonbackground = "#000000", bd =2, bg = "#000000", 
                                
#                                 )

#                                 #I ADDED a lot of what's below.  It can be more better...
#                                 # https://stackoverflow.com/questions/57034118/time-picker-for-tkinter


#         baby_bday_button = ctk.CTkButton(self, width = 100, text = "Enter", command = lambda:get_time(self.hour,self.min))
        
#         def get_time(hour, min):
#             print (self.hourstr, self.minstr)
#             time_entered = f"{hour.get()}:{min.get()}"
#             print("get_time - returns:", time_entered)
#             return(time_entered)

#         baby_bday_button.grid(row=1,column=0, columnspan = 2)
#         self.hour.grid(row=0,column=0)
#         self.min.grid(row=0,column=1)
        
#         get_hour = self.hour.get()
#         get_min = self.min.get()
#         time_entered = f"{self.hour.get()}:{self.min.get()}"
#         print(time_entered)
#         print(get_hour, get_min)

#     def hour_invalid(self):
#         self.hourstr.set('10')
#     def hour_valid(self,input):
#         if (input.isdigit() and int(input) in range(24) and len(input) in range(1,3)):
#             valid = True
#         else:
#             valid = False
#         if not valid:
#             self.hour.after_idle(lambda: self.hour.config(validate='focusout'))
#         return valid
#     def min_invalid(self):
#         self.minstr.set('30')
#     def min_valid(self,input):
#         if (input.isdigit() and int(input) in range(60) and len(input) in range(1,3)):
#             valid = True
#         else:
#             valid = False
#         if not valid:
#             self.min.after_idle(lambda: self.min.config(validate='focusout'))
#         return valid
    
#     def get_time(self):
#         time = f"{self.min.get():self.hour.get()}"
#         return print(time)
        
# root = ctk.CTk() 




Collect_Date(top_frame_2).grid()

# get_hour = Collect_Time(top_frame_2).hour.get()
# get_min = Collect_Time(top_frame_2).min.get()
# time_entered = f"{self.hour.get()}:{self.min.get()}"
# print(time_entered)

# print(get_hour, get_min)
    
root.mainloop()



Collect_Time(top_frame_2)











# import tkinter as tk

# class App(tk.Frame):
#     def __init__(self,parent):
#         super().__init__(parent)
#         # self.geometry("600x500")
#         self.reg=self.register(self.hour_valid)
#         self.hourstr=tk.StringVar(self,'10')
#         self.hour = tk.Spinbox(self,from_=0,to=23,wrap=True,validate='focusout',validatecommand=(self.reg,'%P'),invalidcommand=self.hour_invalid,textvariable=self.hourstr,width=2)
#         self.reg2=self.register(self.min_valid)
#         self.minstr=tk.StringVar(self,'30')
#         self.min = tk.Spinbox(self,from_=0,to=59,wrap=True,validate='focusout',validatecommand=(self.reg2,'%P'),invalidcommand=self.min_invalid,textvariable=self.minstr,width=2)
#         self.hour.grid()
#         self.min.grid(row=0,column=1)
#     def hour_invalid(self):
#         self.hourstr.set('10')
#     def hour_valid(self,input):
#         if (input.isdigit() and int(input) in range(24) and len(input) in range(1,3)):
#             valid = True
#         else:
#             valid = False
#         if not valid:
#             self.hour.after_idle(lambda: self.hour.config(validate='focusout'))
#         return valid
#     def min_invalid(self):
#         self.minstr.set('30')
#     def min_valid(self,input):
#         if (input.isdigit() and int(input) in range(60) and len(input) in range(1,3)):
#             valid = True
#         else:
#             valid = False
#         if not valid:
#             self.min.after_idle(lambda: self.min.config(validate='focusout'))
#         return valid
# root = tk.Tk()
# App(root).pack()
# root.mainloop()


# import datetime
# import time
# from turtle import bgcolor

# utc_formate = 1627948800.0
# # dtformat = 2022-03-23




# import tkinter as kin
# import customtkinter as ctk
# import random #For the bottle notice. 
# import sqlite3
# import datetime
# import time
# import tkcalendar as tkcal







# database = sqlite3.connect('noob_database.db')
# cursor = database.cursor()

# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("dark-blue")
# root = ctk.CTk() 
# root.geometry("1024x576")
# root.resizable(width=False, height=False)
# root.title("NooBorn Test Window")


# top_frame_2 = ctk.CTkFrame(master = root, corner_radius = 20) 
# tframegrid2 ={"frame": top_frame_2, "column" : 2, 
#              "padx" : 5, "pady" : 5, "row" : 0,
#              "columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}

# def create_frame(grid):     #Places frame on screen.
#     grid['frame'].grid(column = grid['column'],
#     padx = 5, pady = 2, row = grid['row'], 
#     columnspan = grid['columnspan'], rowspan = 3, 
#     sticky = grid['sticky']    
#     )




# def grab_date():
#     g_date = cal.get_date()
#     date_time_obj = datetime.datetime.strptime(g_date, '%m/%d/%y')
#     print('Date-time:', str(date_time_obj))
# # date = kin.Label(top_frame_2, text = "")
# # date.grid(column = 1,  padx = 5, pady = 5, row =2, rowspan = 1)     

# cal = tkcal.Calendar(top_frame_2,  
#                     selectforeground  = "#0015ff",
#                     foreground = '#271ea6',  
#                     showweeknumbers = False,
#                     firstweekday = "sunday",
#                     background = "#f3f2f5",
#                     font = "arial, 12",
#                     selectmode = 'day', )
 
# cal.grid(column = 0,  
#             padx = 5,
#             pady = 5, 
#             row =0,
#             rowspan = 1)     
 


# #THERE IT IS!!!!! - 
#     # print('Date:', str(date_time_obj.date()),date_time_obj.timestamp())
#     # print('Time:', date_time_obj.timestamp())

    

# kin.Button(top_frame_2, text = "Set Date",
#        command = grab_date).grid(column = 0,  padx = 5, pady = 5, row =2, rowspan = 1)     
 

 

# create_frame(tframegrid2)




# # Execute Tkinter
# root.mainloop()





# # import datetime
# # # timestamp = .replace(tzinfo=datetime.timezone.utc).timestamp()
# # # print(timestamp)


# # # 1627948800.0









# # # def macslate():
# # #     import tkinter, customtkinter as ctk
# # #     import random #For the bottle notice. 
# # #     import sqlite3
# # #     import datetime
# # #     import time
# # #     database = sqlite3.connect('noob_database.db')
# # #     cursor = database.cursor()

# # #     ctk.set_appearance_mode("dark")
# # #     ctk.set_default_color_theme("dark-blue")
# # #     root = ctk.CTk() 
# # #     root.geometry("1024x576")
# # #     root.resizable(width=False, height=False)
# # #     root.title("NooBorn Test Window")


# # #     #place a frame : 
# # #     top_frame_1 = ctk.CTkFrame(master = root, corner_radius = 20)
# # #     top_frame_1.grid(column = 0, row = 0)
# # #     top_frame_2 = ctk.CTkFrame(master = root, corner_radius = 20)
# # #     top_frame_2.grid(column = 1, row = 0)
# # #     # y_framegrid = {"frame": yellow_frame, "column" :1, "padx" : 5, "pady" : 5, "row" : 2, "rowspan" : 1}
# # #     # b_framegrid = {"frame": brown_frame, "column" : 0, "padx" : 5, "pady" : 5, "row" :2, "rowspan" :1}

# # #     main_menu = {"food_button" : {"name" : "Food", "window" : root, "column" : 0, "row" :0, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1,food_menu1)},
# # #                 "sleep_button" : {"name" : "Sleep", "window" : root, "column" : 0, "row" :1, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1, sleep_menu1)},
# # #                 "diaper_button" : {"name" : "Diaper", "window" : root, "column" : 0, "row" :2, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1, diaper_menu1)},
# # #                 "milestones" : {"name" : "Milestones", "window" : root, "column" : 0, "row" :3, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1, milestones1)},
# # #                 "activities" : {"name" : "Activities", "window" : root, "column" : 0, "row" :4, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1, activities1)},
# # #                 "profile_button" : {"name" : "Profile", "window" : root, "column" : 0, "row" :5, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1, profile1)},
# # #                 }

# # #     diaper_menu1 = {"Yellow" : { "name" : "Yellow", "window" : top_frame_1, "column" : 1, "row" :2, "sticky" : "new", "command" : lambda: yellow_press()}, 
# # #                         "Brown" : { "name" : "Brown", "window" : top_frame_1, "column" : 1, "row" :3, "sticky" : "new", "command" : lambda: brown_press()}
# # #                         }



# # #     time_period_buttons = {"Morning" : { "name" : "Morning",  "column" :0, "row" :1, "sticky" : "new", "window" : top_frame_2, "command" : lambda:current_time_frame() }, 
# # #                             "Midday" : { "name" : "Midday", "column" :1, "row" :1, "sticky" : "new", "window" : top_frame_2, "command" : lambda: custom_time_frame()},
# # #                             "Afternoon" : { "name" : "Afternoon", "column" : 2, "row" :1, "sticky" : "new", "window" : top_frame_2, "command" : lambda: custom_time_frame()},
# # #                             "Evening" : { "name" : "Evening", "column" : 3, "row" :1, "sticky" : "new", "window" : top_frame_2, "command" : lambda: custom_time_frame()},
# # #                             "Night" : { "name" : "Night", "column" : 4, "row" :1, "sticky" : "new", "window" : top_frame_2, "command" : lambda: custom_time_frame()}
# # #                             }


# # #     def switch_event():
# # #         button_builder(time_period_buttons)
# # #         yellow_frame =  ctk.CTkFrame(master = top_frame_1, corner_radius = 20, fg_color = '#e3dd20')
# # #         brown_frame =  ctk.CTkFrame(master = top_frame_1, corner_radius = 20, fg_color = '#715f1d')
# # #         if switch_1.get() == 1:
# # #             forget_frame(brown_frame)
# # #             yellow_frame.grid(column = 0, padx = 5, pady = 5, row =2, rowspan =1)
# # #             # create_frame(y_framegrid)

# # #         elif switch_1.get() ==2:
# # #             forget_frame(yellow_frame)
# # #             brown_frame.grid(column = 0, padx = 5, pady = 5, row =2, rowspan =1)
# # #             # create_frame(b_framegrid)
# # #             # yellow_frame.grid_forget()


# # #     def create_frame(grid):     #Places frame on screen.
# # #         grid['frame'].grid(column = grid['column'], padx = 5, pady = 5, row = grid['row'], rowspan = 3)

# # #     def forget_frame(frame):
# # #             frame.grid_forget()

# # #     # morning
# # #     # midday
# # #     # afternoon
# # #     # evening
# # #     # night


# # #     def button_builder(button_list):
# # #         for x in button_list.values():
# # #             (x['button']) = ctk.CTkButton((x['window']), text_font = ("arial", 20),  text = x['name'], height = 60, command = x['command'])
# # #             x['button'].grid(column = x['column'],pady = 10, row = x['row'], sticky = x['sticky'])
# # #         #     all_open_buttons.update(button_list)
# # #         # print("COUNT OF OPEN BUTTONS : \n",len(all_open_buttons))
# # #         return button_list


# # #     # switch_var = tkinter.IntVar(1)


# # #     # def diaper_button_push():
# # #     #     create_frame()

# # #     switch_1 = ctk.CTkSwitch(master=top_frame_2, text= "Yellow\n or \nBrown?", command=switch_event,
# # #                                 onvalue = 1, offvalue= 2)

# # #     switch_1.grid(column = 0, row = 0)








# # #     root.mainloop()