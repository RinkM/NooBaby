import tkinter as tk
import time
root = tk.Tk()




class Collect_Date(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        # create_frame(tframegrid2)
        # self.geometry("600x500")
        #variables for current Date
        current_month = time.strftime("%m")
        current_day = time.strftime("%d")
        current_year = time.strftime("%Y")

        enter_date_label = tk.Label(self, text = "Enter Date")
        self.reg=self.register(self.month_valid) #not sure about register. refers to the method below. 
        self.monthstr=tk.StringVar(self,f"{current_month}")    #sets the number in the box.  could be current time. 
        self.month = tk.Spinbox(self,from_=0,to=12, 
                                wrap=True,validate='focusout', validatecommand=(self.reg,'%P'),
                                invalidcommand=self.month_invalid, textvariable=self.monthstr,width=2,
                                font = "arial, 20", fg = "#eae6f5",
                                buttonbackground = "#000000", bd =2, bg = "#000000", 
                                )

        self.reg2=self.register(self.day_valid)
        self.daystr=tk.StringVar(self,f'{current_day}')
        self.day = tk.Spinbox(self,from_=0,to=31,wrap=True,validate='focusout',
                                validatecommand=(self.reg2,'%P'),
                                invalidcommand=self.day_invalid,textvariable=self.daystr,
                                width=2, font = "arial, 20", fg = "#eae6f5",
                                buttonbackground = "#000000", bd =2, bg = "#000000", 
                                
                                )

        self.reg3=self.register(self.year_valid)
        self.yearstr=tk.StringVar(self,f'{current_year}')
        self.year = tk.Spinbox(self,from_=2021,to=2030,wrap=True,validate='focusout',
                                validatecommand=(self.reg3,'%P'),
                                invalidcommand=self.year_invalid,textvariable=self.yearstr,
                                width=4, font = "arial, 20", fg = "#eae6f5",
                                buttonbackground = "#000000", bd =2, bg = "#000000",
                                )
                    #I ADDED a lot of what's below.  It can be more better...
                                # https://stackoverflow.com/questions/57034118/time-picker-for-tkinter

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
        if (input.isdigit() and int(input) in range(2020,2030) and len(input) in range(4)):
            valid = True
        else:
            valid = False
        if not valid:
            self.year.after_idle(lambda: self.year.config(validate='focusout'))
        return valid


root.mainloop()