






def main(root, all_data):

    import customtkinter as ctk
    import Noob_Milk
    # from Noob_Sleep import sleep_button_press
    # from Noob_Diaper import yellow_press, brown_press
    
    root.geometry("1024x576")
    root.resizable(width=False, height=False)
    root.title("NooBorn Window")

    #List of Frames:
    
    top_frame_1 = ctk.CTkFrame(master = root, corner_radius = 20)
    top_frame_2 = ctk.CTkFrame(master = root, corner_radius = 20)
    tframegrid2 ={"frame": top_frame_2, "column" : 2,  "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}
    top_frame_2a = ctk.CTkFrame(master = root, corner_radius = 20)
    top_frame_3 = ctk.CTkFrame(master = root, corner_radius = 20)
    
    tframe_list = [top_frame_1,top_frame_2,top_frame_3,top_frame_2a]

    bottom_frame_master = ctk.CTkFrame(master = root, corner_radius = 20, width = 875)

    #List of instructions to place frames on screen.
    tframegrid1 = {"frame": top_frame_1, "column" : 1, "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}
    tframegrid2 ={"frame": top_frame_2, "column" : 2,  "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}
    tframegrid2a = {"frame": top_frame_2a, "column" : 2,  "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}
    tframegrid3 = {"frame": top_frame_3, "column" : 3,  "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}
    bframegrid = {"frame": bottom_frame_master, "column" : 1,  "padx" : 5, "pady" : 5, "row" : 3, "columnspan" : 3, "rowspan" : 3, "sticky": 'ew'}
    




    # top_frame_1 = ctk.CTkFrame(master = root, corner_radius = 20)
    # tframegrid1 = {"frame": top_frame_1, "column" : 1, "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}
    # tframe_list = [top_frame_1,top_frame_2,top_frame_3,top_frame_2a]



    # Lists of Buttons in Main Window.
    main_menu = {"food_button" : {"name" : "Food", "window" : root, "column" : 0, "row" :0, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1,food_menu1)},
            "sleep_button" : {"name" : "Sleep", "window" : root, "column" : 0, "row" :1, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1, sleep_menu1)},
            "diaper_button" : {"name" : "Diaper", "window" : root, "column" : 0, "row" :2, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1, diaper_menu1)},
            "milestones" : {"name" : "Milestones", "window" : root, "column" : 0, "row" :3, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1, milestones1)},
            "activities" : {"name" : "Activities", "window" : root, "column" : 0, "row" :4, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1, activities1)},
            "profile_button" : {"name" : "Profile", "window" : root, "column" : 0, "row" :5, "sticky" : "new", "command" : lambda: create_combo(tframegrid1,top_frame_1, profile1)},
            }

    food_menu1 = {"Liquid" : { "name" : "Liquid", "window" : top_frame_1, "column" : 0, "row" :0, "sticky" : "new", "command" : lambda:Noob_Milk.main() }, 
            "Solids" : { "name" : "Solids", "column" : 0, "row" :1, "sticky" : "new", "window" : top_frame_1, "command" : lambda: Noob_Milk.main()}
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

    profile1 = {"profile " : { "name" : "Profile", "window" : top_frame_1, "column" : 0, "row" :0, "sticky" : "new", "command" : lambda: button_builder(xxx)}, 
                "Info" : { "name" : "Info",  "window" : top_frame_1, "column" : 0, "row" :1, "sticky" : "new", "command" : lambda: remove_buttons(sleep_menu)},
                 "Log In" : { "name" : "Log In", "window" : top_frame_1, "column" : 0, "row" :2, "sticky" : "new", "command" : lambda: remove_buttons(sleep_menu)},
                  }


#GUI INTERFACE FUNCTIONS :

    def clear_frame(frame):     #Clears frames of all widgets
        for widget in frame.winfo_children()[1:]: #selects the widgets on the frame, 
            widget.destroy()                        #destroys all but TKINTER skin.

    def create_frame(grid):     #Places Specific frame on screen.
        grid['frame'].grid(column = grid['column'], padx = 5, pady = 2, row = grid['row'], columnspan = grid['columnspan'], rowspan = 3, sticky = grid['sticky']    )

    def forget_frame():
        for item in tframe_list:
            item.grid_forget()

    def create_combo(grid, frame, buttons):
        #combines 4 functions as one. Removes the frame, clears it,
        #recreates it with new buttons.  Used for 2nd column functions. 
        forget_frame()
        clear_frame(frame)        
        create_frame(grid)
        button_builder(buttons)

    def button_builder(button_list):  #creates and places buttons on screen
        for x in button_list.values():
            (x['button']) = ctk.CTkButton((x['window']), text_font = ("arial", 20),  text = x['name'], height = 50, command = x['command'])
            x['button'].grid(column = x['column'],pady = 10,padx = 3, row = x['row'], sticky = x['sticky'])
        return button_list













    button_builder(main_menu)
    for k,v in all_data.items():
        print (k,v)
    print("all_data" ,all_data['name'])







if __name__ == '__main__':
    main()


