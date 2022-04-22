



import customtkinter as ctk
import sqlite3, datetime, time, uuid
import tkcalendar as tkcal


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk() 
root.geometry("1024x576")
root.resizable(width=False, height=False)
root.title("NooBorn Test Window")


root.mainloop()







# if __name__ == '__main__':
#     main()


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


