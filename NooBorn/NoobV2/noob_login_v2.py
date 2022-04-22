
"""
NooB_Profile
Purpose : Creates a GUI for the log in screen. Asks for username / password, creates 
new accounts, and (for my own testing purposes) allows you to skip this screen

Tests username and password entry information against what is stored.  Gatekeeps the rest of the program. 

Uses custom tkinter to create the GUI. Also uses TkCalander 

Also, currently creates root window without geometry. Need to pass a window through main()function called root for full function.


"""


def main(root):
        
    import customtkinter as ctk
    import sqlite3, datetime, time, uuid
    import tkcalendar as tkcal
    import noob_buttons
    import Noob_Create_User

    # root Window Settings : 

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    
    #Turn On for testing:
    # root = ctk.CTk() 

    # root.geometry("1024x576")
    root.resizable(width=False, height=False)
    root.title("NooBorn Log In")

    #database setup :
    database = sqlite3.connect('noob_database2.db')
    cursor = database.cursor()

    def user_log_in():
        #creates and places the labels, entryboxes, and text for the main log in screen. does not collect data except through button functions. 

        welcome_label = ctk.CTkLabel(master = root, text_font = ("arial", 20), 
                                text = "Welcome to NooBorn!\nPlease enter your username \nand password to continue.\n"
                                )
        new_account_label = ctk.CTkLabel(master = root, text_font = ("arial", 20), 
                                text = "Or create a new account\n"
                                )                                

        username_entry = ctk.CTkEntry(master=root, width = 200, placeholder_text=("User Name"))
        pword_entry = ctk.CTkEntry(master=root, width = 200, placeholder_text=("Password"))

        enter_username_button = ctk.CTkButton(master = root, text = "Log In", command = lambda:enter_button())
        create_account_button = ctk.CTkButton(master = root, text = "Create a new account", command = lambda:create_account_buttons())
        skip_username_button = ctk.CTkButton(master = root, text = "Username?\nI don't need no stinking username.", command = lambda: skip_entry())

        welcome_label.grid(column = 0, row = 0, columnspan = 2)  
        new_account_label.grid(column = 0, row = 4)

        username_entry.grid(column = 0, row = 1, columnspan = 1, padx = 3, pady = 3 )  
        pword_entry.grid(column = 0, row = 2, padx = 3, pady = 3 )

        enter_username_button.grid(column = 0, row = 3, columnspan = 1)
        create_account_button.grid(column = 0, row = 5, columnspan = 1, padx = 5, pady = 5)
        skip_username_button.grid(column = 0, row = 6, columnspan = 1, padx = 5, pady = 5)




        def enter_username():
            #on button press, 1) collects username/password entries. 2) tests them against the database. 3) allows entry to profile. 
        # def collect_username_pw():
            user_entry = username_entry.get() #1
            password_entry = pword_entry.get()

            cursor.execute(f"SELECT userID, password FROM user_profile WHERE username = '{user_entry}';")
            id_pw = cursor.fetchone()
            user_ID = id_pw[0]
            password = id_pw[1]
            # cursor.execute(f"SELECT password FROM user_profile WHERE username = '{user_entry}' ;")
            # password = cursor.fetchone()[1]
        #     return (user_ID, password_entry, password)

        # def user_test(user_ID, password, password_entry):
            if password !=password_entry:
                #Open a window that says "Password doesn't match. Try again." 
                window = ctk.CTkToplevel(root)
                window.title("Error")
                ctk.CTkLabel(master=window, text = "Password doesn't match. Try again.").grid(row=0)
                ctk.CTkButton(master = window, text = "Try Again", command = lambda:window.destroy()).grid(row = 1)
                window.mainloop()
            else: 
                def select_baby_id(user_ID):   #later on, add a way to select a name to it.   
                    cursor.execute(f"SELECT babyID FROM relationship WHERE userID = '{user_ID}' ;")
                    baby_ID = cursor.fetchone()[0]
                    print(type(baby_ID))
                    return baby_ID

                def collect_baby_info(baby_ID):
                    cursor.execute(f"SELECT babyID, baby_name, birthdate_time FROM baby_profile WHERE babyID = '{baby_ID}' ;")
                    baby_info = cursor.fetchone()
                    print(baby_info)
                    return baby_info
                
                
                baby_id = select_baby_id(user_ID)
                baby_info = collect_baby_info(baby_id)
                all_data = {"user": user_ID, "baby":baby_info[0], "name":baby_info[1], "bday":baby_info[2]}
                print("all data: ", all_data)
                print(all_data["name"])
                print("Welcome to NooBorn")
                return all_data
                


        def enter_button():
            
            all_data = enter_username()
            print(all_data)
            for widget in root.winfo_children()[0:]:
                widget.destroy()
            noob_buttons.main(root, all_data)

        def skip_entry():
            all_data = {'user': '3033b7a7-58d8-4c45-b0aa-13786d643ce5', 'baby': '5b1632cd-cd97-49c1-9bef-82665f0f5c5a', 'name': 'TestBaby', 'bday': '2022-01-04 00:00:00'}
            for widget in root.winfo_children()[0:]:
                widget.destroy()
            noob_buttons.main(root, all_data)


        def create_account_buttons():
            #clears the window and loads the create_user screen.
            for widget in root.winfo_children()[1:]:
                widget.destroy()
            Noob_Create_User.main(root)

        root.mainloop()



        # new_profile_window.mainloop()
        # root.mainloop()
    user_log_in()

    root.mainloop()

# root = ctk.CTk() 

if __name__ == '__main__':
    main()