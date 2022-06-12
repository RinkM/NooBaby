
import customtkinter as ctk
    #List of Frames:

#GUI INTERFACE FUNCTIONS :

def clear_frame(frame):     #Clears frames of all widgets
    for widget in frame.winfo_children()[1:]: #selects the widgets on the frame, 
        widget.destroy()                        #destroys all but TKINTER skin.

def create_frame(grid):     #Places Specific frame on screen.
    grid['frame'].grid(column = grid['column'], padx = 5, pady = 2, row = grid['row'], columnspan = grid['columnspan'], rowspan = 3, sticky = grid['sticky']    )

def forget_frame(all_frames):
    for item in all_frames:
        item.grid_forget()

def create_combo(grid, frame, buttons,all_frames):
    #combines 4 functions as one. Removes the frame, clears it,
    #recreates it with new buttons.  Used for 2nd column functions. 
    forget_frame(all_frames)
    clear_frame(frame)        
    create_frame(grid)
    button_builder(buttons)

def button_builder(button_list):  #creates and places buttons on screen
    for x in button_list.values():
        (x['button']) = ctk.CTkButton((x['window']), text_font = ("arial", 20),  text = x['name'], height = 50, command = x['command'])
        x['button'].grid(column = x['column'],pady = 10,padx = 3, row = x['row'], sticky = x['sticky'])
    return button_list





