import tkinter


import tkinter


# #this will create a small window 
# # create label = The output on the window
# def font():
#     font = "Arial Bold", 50
#     return font




# def tkinter1():    
#     window = tkinter.Tk()
#     window.title("GUI")
#     label = tkinter.Label(window, text = "Hello World!").pack()
#     l1 = label(window,text="Welcome to Nooborn.", font = font() )
#     window.geometry('350x200')
#     l1.grid(column = 0, row = 0)
#     window.mainloop()



# tkinter1()

# #label widget
# # create text 

# def label_widget():
#     return





import tkinter
import urllib


root = tkinter.Tk()  #made our first window. 

# def helloCallBack():
#    tkinter.MessageBox.showinfo( "Hello Python", "Hello World")

HEIGHT = 700
WIDTH = 800


#Canvas Makes the window. 
canvas = tkinter.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

#Frame can divide the window in 'frames' relx and rely = relative to 0.  Theyre written, they're centered. 
#frame is a location (container?) can use it instead of root.


# frame = tkinter.Frame(root, bg = "#326ecf")
# frame.place(relx = 0, rely = 0, relwidth = .2, relheight = .2)

# frame2 = tkinter.Frame(root, bg = "#326ecf")
# frame2.place(relx = 0, rely = .2,relwidth = .2, relheight = .2)

# frame3 = tkinter.Frame(root, bg = "#326ecf")
# frame3.place(relx = 0, rely = 0.4, relwidth = .2, relheight = .2)

# frame4 = tkinter.Frame(root, bg = "#326ecf")
# frame4.place(relx = 0, rely = 0.6, relwidth = .2, relheight = .2)

bigframe = tkinter.Frame(root, bg = "white")




#Make a button!
#                     #root = window location
# button = tkinter.Button(frame, bg = "white", fg = "blue", text ="Hello")
# button2 = tkinter.Button(frame2, text = "What's up?")
# button3 = tkinter.Button(frame3, bg = "black", fg = "white", text ="#3")
# button4 = tkinter.Button(frame4, bg = "white", fg = "black", text ="#4")
# button.pack()
# button2.pack()
# button3.pack()
# button4.pack()


# #make a label
# label = tkinter.Label(frame, text = "This is a label.", bg = 'orange' )
# label2 = tkinter.Label(frame2, text = "This is label2.", bg = 'red' )
# label3 = tkinter.Label(frame3, text = "This is label3.", bg = 'purple', fg = "white" )
# label4 = tkinter.Label(frame4, text = "This is label4.", bg = 'grey', fg = "white" )
# label.pack()
# label2.pack()
# label3.pack()
# label4.pack()


# #make an entry (place to type.)
# entry1 = tkinter.Entry(frame, bg = "lightgreen")
# entry2 = tkinter.Entry(frame2, bg = "lightgreen")
# entry3 = tkinter.Entry(frame3, bg = "lightgreen")
# entry4 = tkinter.Entry(frame4, bg = "lightgreen")
# entry1.pack()
# entry2.pack()
# entry3.pack()
# entry4.pack()



# radio = tkinter.Scale(bigframe, text = "radio", )
# radio.place(relx = .8)





def sel():
   selection = "Value = " + str(var.get())
   label.config(text = selection)



main = tkinter.Tk()
var = tkinter.DoubleVar()
bottle_scale = tkinter.Scale( main, variable = var,  from_ =0.5 , to = 20, resolution = .5 )
bottle_scale.pack(anchor='center')
bottle_scale.set(6)
# bottle_scale.place(anchor = "n", relx = 0, rely = 0)


button = tkinter.Button(main, text="Add bottle", command=sel)
button.pack(anchor="center")

label = tkinter.Label(main, text = "How many ounces?")
label.pack()











root.mainloop()




