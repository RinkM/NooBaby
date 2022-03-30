import sqlite3

database = sqlite3.connect('noob_database.db')


def create_tables():
    
    cursor = database.cursor()


    cursor.execute("""CREATE TABLE IF NOT EXISTS bottle (
            bottle_num integer UNIQUE, 
            datetime text,
            utc integer,  
            amount integer NOT NULL,
            baby_id integer, 
            product text,
            product_id integer
            ) """) 

    cursor.execute("""CREATE TABLE IF NOT EXISTS diaper(
                table_id text,
                diaper_num integer, 
                datetime text,
                utc integer,
                onetwo integer NOT NULL,
                baby_id integer 
                )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS sleep(
                table_id text,
                bottle_num integer, 
                datetime text,
                utc integer,
                start_time integer, 
                end_time integer,
                duration integer NOT NULL,
                baby_id integer
                )""")


    cursor.execute("""CREATE TABLE IF NOT EXISTS solid_food(
                table_id text,
                solid_food_num integer, 
                datetime text,
                utc integer,
                baby_id integer FOREIGN  KEY,
                food_name text,
                amount integer NOT NULL
        )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS milestones(
                table_id text,
                stone_num integer,
                stone_name text, 
                stone_description text,
                stone_acheived integer,
                stone_text_achieve text, 
                datetime text,
                utc integer,
                baby_id integer FOREIGN  KEY
        )""")


    cursor.execute("""CREATE TABLE IF NOT EXISTS baby_profile (
                table_id text,
                profile_num integer, 
                datetime text,
                utc integer,
                baby_id integer PRIMARY KEY,
                baby_name text,
                birthdate_utc integer,
                birthdate_time text NOT NULL,
                sex integer,
                unique_user_str text,
                unique_user blob
        )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS user_profile (
                table_id text,
                unique_user_str text PRIMARY KEY,
                unique_user blob,
                user_num integer, 
                datetime text,
                utc integer,
                baby_id integer,
                username text,
                password text
        )""")







    #this saves the database. 
    database.commit()
    #testing version



    # this closes the database.
    database.close()





# cursor.execute("SELECT * FROM bottle3;")
# cursor.description
# # print("cursor description: ", cursor.description)
# print("cursor fetchall: ",cursor.fetchall())


    # #testing version
    # cursor.execute("SELECT * FROM bottle3;")
    # cursor.description
    # print("before data", cursor.description)











# #This is set up to test things in tkinter.

# #Think of it as a canvas. 









# ##########################################
# ##################### MAIN MENU ######################
# ##########################################
# all_open_wigits ={}
# def main():
    
#     import tkinter, customtkinter as ctk
#     import random #For the bottle notice. 
#     import sqlite3
#     import datetime
#     import time
#     database = sqlite3.connect('noob_database.db')
#     cursor = database.cursor()

#     ctk.set_appearance_mode("dark")
#     ctk.set_default_color_theme("dark-blue")
#     root = ctk.CTk() 
#     root.geometry("1024x576")
#     root.resizable(width=False, height=False)
#     root.title("NooBorn Test Window")


#     all_frames = {"top_frame_1" : {"name" : "top_frame_1", "column" : 1, "row" : 0, "rowspan" : 3, "columnspan" : 1},
#                 "top_frame_2" : {"name" : "top_frame_2","column" : 2, "row" : 0, "rowspan" : 3, "columnspan" : 1},
#                 "top_frame_3" : {"name" : "top_frame_3","column" : 3, "row" : 0, "rowspan" : 3, "columnspan" : 1},
#                 "bottom_frame" : {"name" : "top_frame_1","column" : 1, "row" : 3, "rowspan" : 3, "columnspan" : 4} 
                
#                 }

#     tf1 = {"name" : "top_frame_1", "column" : 1, "row" : 0, "rowspan" : 3, "columnspan" : 1, "object" : None}
#     tf2 = {"name" : "top_frame_2","column" : 2, "row" : 0, "rowspan" : 3, "columnspan" : 1, "object" : None}
#     tf3 = {"name" : "top_frame_3","column" : 3, "row" : 0, "rowspan" : 3, "columnspan" : 1, "object" : None}
#     bf =  {"name" : "bottom_frame","column" : 1, "row" : 3, "rowspan" : 3, "columnspan" : 3, "object" : None} 


#     top_frame_1 = ctk.CTkFrame(master = root, corner_radius = 20)
#     top_frame_2 = ctk.CTkFrame(master = root, corner_radius = 20)
#     top_frame_2a = ctk.CTkFrame(master = root, corner_radius = 20)
#     top_frame_3 = ctk.CTkFrame(master = root, corner_radius = 20)
#     bottom_frame = ctk.CTkFrame(master = root, corner_radius = 20)

#     # liquid_top_frame_3.grid_propagate(1)

    
#     tframegrid1 = {"frame": top_frame_1, "column" : 1, "padx" : 5, "pady" : 5, "row" : 0, "rowspan" : 3}
#     tframegrid2 ={"frame": top_frame_2, "column" : 2,  "padx" : 5, "pady" : 5, "row" : 0, "rowspan" : 3}
#     tframegrid2a = {"frame": top_frame_2a, "column" : 2,  "padx" : 5, "pady" : 5, "row" : 0, "rowspan" : 3}
#     tframegrid3 = {"frame": top_frame_3, "column" : 3,  "padx" : 5, "pady" : 5, "row" : 0, "rowspan" : 3}
#     bframegrid = {"frame": bottom_frame, "column" : 1,  "padx" : 5, "pady" : 5, "row" : 4, "rowspan" : 3}


# #WORKSPACE - 

#     def bottle_summary_frame():  #3rd frame. Provides summary and enter button. 
#         # create_frames(liquid_top_frame_3)
#         # top_frame_3.grid (column = 3,  padx = 5, pady = 5, row = 0, rowspan = 3)
#         bottle_summary_label = ctk.CTkLabel(master = top_frame_3, text = "Summary\n BABYNAME had:\n XAMOUNT of XPRODUCT\n at HH:MM\nMM-DD-YYYY")
#         submit_bottle_button = ctk.CTkButton(master = top_frame_3, text = "Enter Bottle", command = lambda : bottle_button())
        
#         # liquid_top_frame_3.grid(column = 3,  padx = 5, pady = 5, row = 0, rowspan = 3)
#         bottle_summary_label.grid(column = 0, row = 0)
#         submit_bottle_button.grid(column = 0, row = 1)



#     def clear_frame(frame):
#         print("from clear_frame",frame.winfo_children())
#         for widget in frame.winfo_children()[1:]: #selects the widgets on the frame, 
#             widget.destroy()                        #destroys all but canvas
        
#     def create_frame(grid):
#         grid['frame'].grid(column = grid['column'], padx = 5, pady = 5, row = grid['row'], rowspan = 3)
        

#     create_frame(tframegrid3)
#     bottle_summary_frame()
    
    
#     clear_frame(top_frame_3)
    
#     bottle_summary_frame()














#     root.mainloop()

# if __name__ == '__main__':
#     main()


