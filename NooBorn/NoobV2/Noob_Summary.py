


def main(root, all_data, choice):


    import customtkinter as ctk
    import sqlite3, datetime, time
    import noob_button_functions
    
    top_frame_3 = ctk.CTkFrame(master = root, corner_radius = 20)
    tframegrid3 = {"frame": top_frame_3, "column" : 3,  "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}

    database = sqlite3.connect('noob_database2.db')
    cursor = database.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")#turns foreign keys on.




# """DATA SUBMISSION BUTTONS"""
    def final_summary_frame(choice):  #Uses 3rd Tkinter frame. Provides summary of all entered data plus a submit button. 
        #'choice' is passed. It determines what is drawn in the 3rd frame: the bottle, sleep, or diaper choice.  
        # Opens the correct window depending.
        noob_button_functions.clear_frame(top_frame_3)
        noob_button_functions.create_frame(tframegrid3)
        onetwo = 1
        sleeptime =1
        
        if choice == "bottle":
            # all_data["datetime"] = datetime.datetime.now()
            # all_data['milk_amount'] = 6
            print(all_data["milk_datetime"])
            date_entry = all_data['milk_datetime'].strftime("%m-%d-%Y")
            time_entry = all_data['milk_datetime'].strftime("%H:%M")
            bottle_summary_label = ctk.CTkLabel(master = top_frame_3,text_font = ("arial", 12), text = f"Summary:\n\n At {time_entry}\non\n{date_entry}, \n{all_data['name']} had:\n {all_data['milk_amount']} oz of MILK.").grid(column = 0, row = 0)
            button_text = "Enter Bottle"
            button_func = lambda: bottle_button()

        elif choice == "diaper":

            if all_data['onetwo'] == 1:
                diapercolor = "yellow"
            else : 
                diapercolor = "brown"
            bottle_summary_label = ctk.CTkLabel(master = top_frame_3,text_font = ("arial", 12), text = f"Summary:\n\n During the\n{all_data['moment_of_day']},\n{all_data['name']} had \n a {diapercolor} diaper. \n ").grid(column = 0, row = 0)
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




    def bottle_button():    
        #Enters data into Bottle Table
        cursor.execute("INSERT INTO bottle ( babyID, datetime, utc, amount, product, product_id) VALUES (?,?,?,?,?,?)",
                    [all_data['baby'], datetime.datetime.now(), time.time(), all_data['milk_amount'], 'Powder Milk', 801])
        database.commit()
        print("Bottle Logged")



    def sql_diaper(): 
        #Enters data into Diaper Table
        cursor.execute("INSERT INTO diaper (babyID, datetime, onetwo) VALUES (?,?,?)",
                        [all_data['baby'], all_data['diaper_datetime'], all_data['onetwo']])
        database.commit()
        print("Diaper Logged")



    def sql_sleep(sleeptime):
        #Enters data into Sleep Table
        cursor.execute("INSERT INTO sleep (babyID, datetime, utc, onetwo) VALUES (?,?,?,?)",
            [all_data['baby'], datetime.datetime.now(), time.time(),time])
        database.commit()
        print("Sleep Logged")


    final_summary_frame(choice)

if __name__ == '__main__':
    main()






        