import time
import tkinter
root = tkinter.Tk()




HEIGHT = 700
WIDTH = 800


#Canvas makes the window. 
canvas = tkinter.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

#divides the window with a frame. 
frame = tkinter.Frame(root, bg = "#326ecf")
frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

add_bottle_button = tkinter.Button(frame, bg = "white", fg = "blue", text ="Add a Bottle")
add_nap_button = tkinter.Button(frame, bg = "white", fg = "blue", text ="Add a Nap")
add_diaper = tkinter.Button(frame, bg = "white", fg = "blue", text ="Diaper Change")
settings_button = tkinter.Button(frame, bg = "white", fg = "blue", text ="Settings")

#relwidth at .245 gives the gap between buttons. 
add_bottle_button.place(relx = 0, rely = 0, relwidth = .245, relheight = .245)
add_nap_button.place(relx = 0, rely = .25, relwidth = .245, relheight = .245)
add_diaper.place( relx = 0, rely = .5, relwidth = .245, relheight = .245)
settings_button.place(relx = 0, rely = .75, relwidth = .245, relheight = .245)





# button.pack(side = "left")

# button.grid(columns = 2)




def split_frame():
    frame.place(relwidth = .5, relheight = .5)

# button.place(relx = 0, rely = 0.1)



root.mainloop()