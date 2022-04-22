



def main(root):

    import noob_login_v2 as profile
    import customtkinter as ctk
    import uuid
    import tkcalendar as tkcal
    import datetime, time, sqlite3

    
    database = sqlite3.connect('noob_database2.db')
    cursor = database.cursor()



    def create_user():
        #welcomes user, asks for username, password, baby name, baby bday. creates UUID and assigns one to the user and one to the baby.

        # new_profile_window = ctk.CTkToplevel() 
        # new_profile_window.transient(root)
        
        # new_profile_window.geometry("920x400")
        root.title("NooBorn Account Creation")
        baby_uuid = str(uuid.uuid4())
        user_uuid = str(uuid.uuid4())

        def profile_creation():
            welcome = ctk.CTkLabel(master = root, text_font = ("arial", 20), 
                                    text = "Welcome to NooBorn!\nWhere you can keep track of your child's information.\n\n\nIt looks like this is your first time using NooBorn on this device. \nPlease enter the following information :\n "
                                    )   

            user_name_label = ctk.CTkLabel(master = root, 
                # text_font = ("arial", 20),
                text = "Create a User Name")
            
            password_label = ctk.CTkLabel(master = root, 
                # text_font = ("arial", 20),
                text = "Create a Password")
            
            baby_name_label = ctk.CTkLabel(master = root, 
                # text_font = ("arial", 20),
                text = "What's your child's first name?")

            baby_bday_label = ctk.CTkLabel(master = root, 
                # text_font = ("arial", 20),
                text = "Use the calendar to set your child's birthday")

            create_profile_button = ctk.CTkButton(master = root, text = "Create Profile", command = lambda:enter_profile_button())
            cal_button = ctk.CTkButton(root, text = "Use This Date", command = lambda:format_cal_datetime(calendar,baby_bdate_label))
            login_return_button = ctk.CTkButton(root, text = "Return to Log In Screen", command = lambda:return_to_login())


            user_name_entry = ctk.CTkEntry(master=root, width = 200, placeholder_text=("User Name"))
            password_entry  = ctk.CTkEntry(master=root, width = 200, placeholder_text=("Password"))
            baby_name_entry= ctk.CTkEntry(master=root, width = 200, placeholder_text=("First Name"))
            baby_bdate_label = ctk.CTkLabel(master=root, width = 100, text = "")

            welcome.grid(column = 0, row = 0, columnspan = 2)
            user_name_label.grid(column = 0, row = 1)
            password_label.grid(column = 0, row = 2)
            baby_name_label.grid(column = 0, row = 3)
            baby_bday_label.grid(column = 0, row = 4)

            user_name_entry.grid(column = 1, row = 1)
            password_entry.grid(column = 1, row = 2)
            baby_name_entry.grid(column = 1, row = 3)
            baby_bdate_label.grid(column = 1, row = 4)

            login_return_button.grid(column = 3,  padx = 5, pady = 5, row =5, rowspan = 1)    
            cal_button.grid(column = 3,  padx = 5, pady = 5, row =2, rowspan = 1)    
            create_profile_button.grid(column = 1, row= 5, columnspan = 1)


            calendar = tkcal.Calendar(root,  
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
                #on button press, collects the user entry info and saves it. 
                #one day, it will verify information against whats in database, give error messages, 

                user_name_get = user_name_entry.get()
                password_get = password_entry.get()
                baby_name_get = baby_name_entry.get()
                baby_bday_get = baby_bdate_label.text
                birthday = format_cal_datetime(calendar,baby_bdate_label)
                if user_name_get == "" or password_get =="" or baby_name_get == "" or birthday =="":
                    window = ctk.CTkToplevel(root)
                    window.title("Error")
                    ctk.CTkLabel(master=window, text = "You didn't enter all the required information.\nPlease try again").grid(row=0)
                    ctk.CTkButton(master = window, text = "Return", command = lambda:window.destroy()).grid(row = 1)
                else:
                #attempts to control time.   they failed...
                # dt = datetime.datetime(2021, 8, 3)
                # utc_timestamp = dt.replace(tzinfo=datetime.timezone.utc).timestamp()
                # print("Username, BabyName, Baby Bday:", user_name_get, baby_name_get, birthday)
                # print("UTC Timestamp w/ TZ", utc_timestamp)
                
                    store_baby_data(baby_name_get,birthday)
                    store_user_data(user_name_get,password_get)
                    build_relationship()
                    database.commit()
                    window = ctk.CTkToplevel(root)
                    window.title("Account Created")
                    ctk.CTkLabel(master=window, text = "Thank you for making an account.\nPlease Log In").grid(row=0)
                    ctk.CTkButton(master = window, text = "Return to Log In", command = lambda:account_created(window)).grid(row = 1)

                def account_created(window):
                    return_to_login()
                    window.destroy()


                # root.withdraw()
                # new_profile_window.mainloop()
                


            def store_baby_data(babyname,babybday):
                #enters the baby data into database
                cursor.execute("INSERT INTO baby_profile (userID, babyID, datetime, utc, baby_name, birthdate_time) VALUES (?,?,?,?,?,?)",
                    [user_uuid, baby_uuid, datetime.datetime.now(), time.time(), babyname, babybday])
                database.commit()

            def store_user_data(username, password):
                #enters the user data into database
                cursor.execute("INSERT INTO user_profile (userID, datetime, utc, username, password) VALUES (?,?,?,?,?)",
                        [user_uuid, datetime.datetime.now(), time.time(), username, password])
                database.commit()
            
            def build_relationship():
                cursor.execute("INSERT INTO relationship (userID, babyID) VALUES (?,?)",
                        [user_uuid, baby_uuid])
                database.commit()



            def format_cal_datetime(datedata, label):
                #makes the calandar datetime look pretty.   turns it into  '%m/%d/%y'
                g_date = datedata.get_date()
                date_time_obj = datetime.datetime.strptime(g_date, '%m/%d/%y')
                # print('Date-time:', str(date_time_obj))
                cal_date_time = str(date_time_obj)
                birthday_label = ctk.CTkLabel(master=root, width = 100, text = f"{g_date}").grid(column = 1, row = 4)

                return cal_date_time

            def return_to_login():
                #clears the window and loads the user_log_in screen.
                for widget in root.winfo_children()[1:]:
                    widget.destroy()
                profile.main(root)

            
            
        profile_creation() 

        root.mainloop()

    create_user()







if __name__ == '__main__':
    main()










