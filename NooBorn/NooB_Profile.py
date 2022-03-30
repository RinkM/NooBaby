
def main(rootwindow):
    
    import customtkinter as ctk
    import sqlite3, datetime, time, uuid
    import tkcalendar as tkcal


    database = sqlite3.connect('noob_database.db')
    cursor = database.cursor()
    
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    

    def user_log_in():
        
        return_user_window = ctk.CTkToplevel() 
        return_user_window.transient(rootwindow)
        return_user_window.title("NooBorn User Log In")
        return_user_window.geometry("350x350")
        
        welcome_label = ctk.CTkLabel(master = return_user_window, text_font = ("arial", 20), 
                                text = "Welcome to NooBorn!\nPlease enter your username \nand password to continue.\n"
                                )
        new_account_label = ctk.CTkLabel(master = return_user_window, text_font = ("arial", 20), 
                                text = "Or create a new account\n"
                                )                                
        username_entry = ctk.CTkEntry(master=return_user_window, width = 200, placeholder_text=("User Name"))
        password_entry = ctk.CTkEntry(master=return_user_window, width = 200, placeholder_text=("Password"))

        enter_username_button = ctk.CTkButton(master = return_user_window, text = "Log In", command = lambda:enter_username())
        create_account_button = ctk.CTkButton(master = return_user_window, text = "Create a new account", command = lambda:create_account_button())
        skip_username_button = ctk.CTkButton(master = return_user_window, text = "Username?\nI don't need no stinking username.")

        welcome_label.grid(column = 0, row = 0, columnspan = 2)  
        username_entry.grid(column = 0, row = 1, columnspan = 1, padx = 3, pady = 3 )  
        password_entry.grid(column = 0, row = 2, padx = 3, pady = 3 )
        enter_username_button.grid(column = 0, row = 3, columnspan = 1)
        new_account_label.grid(column = 0, row = 4)

        create_account_button.grid(column = 0, row = 5, columnspan = 1, padx = 5, pady = 5)
        skip_username_button.grid(column = 0, row = 6, columnspan = 1, padx = 5, pady = 5)

        def enter_username():

            database = sqlite3.connect('noob_database.db')
            cursor = database.cursor()

            user_entry = username_entry.get()
            password = password_entry.get()
            
            cursor.execute("SELECT username FROM user_profile")
            user_sql= cursor.fetchall()
            
            
            database.close()

        def create_account_button():
            pass


        return_user_window.mainloop()


    def create_user():

        new_profile_window = ctk.CTkToplevel() 
        new_profile_window.transient(rootwindow)
        new_profile_window.title("NooBorn Account Creation")
        new_profile_window.geometry("920x400")

        baby_uuid = str(uuid.uuid4())
        user_uuid = str(uuid.uuid4())

        def profile_creation():
            welcome = ctk.CTkLabel(master = new_profile_window, text_font = ("arial", 20), 
                                    text = "Welcome to NooBorn!\nWhere you can keep track of your child's information.\n\n\nIt looks like this is your first time using NooBorn on this device. \nPlease enter the following information :\n "
                                    )   

            user_name_label = ctk.CTkLabel(master = new_profile_window, 
                # text_font = ("arial", 20),
                text = "Create a User Name")
            
            baby_name_label = ctk.CTkLabel(master = new_profile_window, 
                # text_font = ("arial", 20),
                text = "What's your child's first name?")

            baby_bday_label = ctk.CTkLabel(master = new_profile_window, 
                # text_font = ("arial", 20),
                text = "Use the calendar to set your child's birthday")

            create_profile_button = ctk.CTkButton(master = new_profile_window, text = "Create Profile", command = lambda:enter_profile_button())

            user_name_entry = ctk.CTkEntry(master=new_profile_window, width = 200, placeholder_text=("User Name"))
            baby_name_entry= ctk.CTkEntry(master=new_profile_window, width = 200, placeholder_text=("First Name"))
            baby_bdate_label = ctk.CTkLabel(master=new_profile_window, width = 100, text = "")

            welcome.grid(column = 0, row = 0, columnspan = 2)

            user_name_label.grid(column = 0, row = 1)
            baby_name_label.grid(column = 0, row = 2)
            baby_bday_label.grid(column = 0, row = 3)

            user_name_entry.grid(column = 1, row = 1)
            baby_name_entry.grid(column = 1, row = 2)
            baby_bdate_label.grid(column = 1, row = 3)


            create_profile_button.grid(column = 0, row= 4, columnspan = 2)


            calendar = tkcal.Calendar(new_profile_window,  
                                selectforeground  = "#0015ff",
                                foreground = '#271ea6',  
                                showweeknumbers = False,
                                firstweekday = "sunday",
                                background = "#f3f2f5",
                                font = "arial, 12",
                                selectmode = 'day',)
            
            calendar.grid(column = 3,  
                        padx = 5,
                        pady = 5, 
                        row =0,
                        rowspan = 1)     





            def enter_profile_button():
                
                user_name_get = user_name_entry.get()
                baby_name_get = baby_name_entry.get()
                baby_bday_get = baby_bdate_label.text
                birthday = format_cal_datetime(calendar,baby_bdate_label)

                dt = datetime.datetime(2021, 8, 3)
                utc_timestamp = dt.replace(tzinfo=datetime.timezone.utc).timestamp()
                print("Username, BabyName, Baby Bday:", user_name_get, baby_name_entry.get(), baby_bday_get )
                print("UTC Timestamp w/ TZ", utc_timestamp)
                store_baby_data(baby_name_entry.get(),birthday)
                store_user_data(user_name_entry.get())
                new_profile_window.withdraw()
                lambda: function()
                
                # new_profile_window.mainloop()
                


            def store_baby_data(babyname,babybday):
                # print(["baby_profile", "Profile_NUM", str(datetime.datetime.now()), time.time(), baby_uuid, babyname, babybday, user_uuid])

                cursor.execute("INSERT INTO baby_profile (table_id, profile_num, datetime, utc, baby_id, baby_name, birthdate_time, unique_user_str) VALUES (?,?,?,?,?,?,?,?)",
                    ["baby_profile", "Profile_NUM", datetime.datetime.now(), time.time(), baby_uuid, babyname, babybday, user_uuid])
                database.commit()

            def store_user_data(username):
                cursor.execute("INSERT INTO user_profile (table_id, unique_user_str, datetime, utc, username) VALUES (?,?,?,?,?)",
                        ["user_profile", user_uuid, datetime.datetime.now(), time.time(), username])
                database.commit()


            def format_cal_datetime(datedata, label):
                g_date = datedata.get_date()
                date_time_obj = datetime.datetime.strptime(g_date, '%m/%d/%y')
                # print('Date-time:', str(date_time_obj))
                cal_date_time = str(date_time_obj)
                label = ctk.CTkLabel(master=new_profile_window, width = 100, text = f"{g_date}").grid(column = 1, row = 3)

                return cal_date_time
            

            cal_button = ctk.CTkButton(new_profile_window, text = "Use This Date",
                                    command = lambda:format_cal_datetime(calendar,baby_bdate_label))
            cal_button.grid(column = 3,  padx = 5, pady = 5, row =2, rowspan = 1)    
            
            
        profile_creation() 
            
            
            
        new_profile_window.mainloop()
            
         


        
    

        # new_profile_window.mainloop()
        # root.mainloop()
    user_log_in()
    # create_user()
    
    
    
     




if __name__ == '__main__':
    main()