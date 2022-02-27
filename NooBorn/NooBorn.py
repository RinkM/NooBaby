import time
import calendar
import tkinter
root = tkinter.Tk()

#figure out time of day / date for that button in 2ndcolumn.



HEIGHT = 700
WIDTH = 800


#Canvas makes the window. 
canvas = tkinter.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

def main_menu():   #add the left side buttons...
    pass

#4 frames - divides the window with a frame. 
far_left_frame = tkinter.Frame(root, bg = "#326ecf",bd = 5)
far_left_frame.place(anchor = 'nw', relx= 0, rely = 0, relwidth = 1/4, relheight = 1)

left_frame = tkinter.Frame(root, bg = "#326ecf", bd = 5)
left_frame.place(anchor = 'nw', relx = .25, rely = 0, relwidth = 1/4, relheight = 1) 

right_frame = tkinter.Frame(root, bg = "#326ecf", bd = 5)
right_frame.place(anchor = 'nw', relx = .5, rely = 0, relwidth = 1/4, relheight = 1) 


far_right_frame = tkinter.Frame(root, bg = "#326ecf", bd = 5)
far_right_frame.place(anchor = 'nw', relx = .75, rely = 0, relwidth = 1/4, relheight = 1) 



#Button Creation
add_bottle_button = tkinter.Button(far_left_frame, bg = "white", fg = "blue", text ="Add a Bottle")
add_nap_button = tkinter.Button(far_left_frame, bg = "white", fg = "blue", text ="Add a Nap")
add_diaper_button = tkinter.Button(far_left_frame, bg = "white", fg = "blue", text ="Diaper Change")
settings_button = tkinter.Button(far_left_frame, bg = "white", fg = "blue", text ="Settings")


#Bottle Slider 
bottle_scale = tkinter.Scale(left_frame,orient = "horizontal",  tickinterval =2, variable = tkinter.DoubleVar(),  from_ =0.5 , to = 12, resolution = .5 )
bottle_scale.place(relx = 0, rely = 0.05, relwidth = 1, relheight = .1)
bottle_scale.set(6)

label = tkinter.Label(left_frame, text = "How many ounces?")
label.pack()


button = tkinter.Button(right_frame, text="Add bottle")
button.pack(anchor="center")


#Button Placement
#relwidth at .245 gives the gap between buttons. 
add_bottle_button.place(relx = 0, rely = 0, relwidth = 1, relheight = .245)
add_nap_button.place(relx = 0, rely = .25, relwidth = 1, relheight = .245)
add_diaper_button.place( relx = 0, rely = .5, relwidth = 1, relheight = .245)
settings_button.place(relx = 0, rely = .75, relwidth = 1, relheight = .245)





#class not going to work...
class CreateButton():
    def __init__(self, button_name, words, x, y, width, height):
        self.self = self
        self.button_name = button_name
        self.words = words
        self.x = x
        self.y = y
        self.width = width
        self.height = height





# button.pack(side = "left")

# button.grid(columns = 2)




# def split_frame():

# button.place(relx = 0, rely = 0.1)



root.mainloop()