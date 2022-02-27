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

#Getting an image into tkinter
def test_funtion(entry):
    print ("You wrote:", entry)

# background_image = tkinter.PhotoImage (file = '/Rainywindow2.png')


# background_label = tkinter.Label(root, image = background_image)
# background_label.place(anchor = "n", relx = .5, rely = 0)

#Frame can divide the window in 'frames' relx and rely = relative to 0.  Theyre written, they're centered. 
#frame is a location (container?) can use it instead of root.


#TOP FRAME
top_frame = tkinter.Frame(root, bg = "Indigo", bd = 5)
top_frame.place(anchor = 'n', relx = .5, rely = .1, relwidth = .75, relheight = .1) 

entry = tkinter.Entry(top_frame, bg = "white", font = 40)
entry.place(relx = 0, rely = 0, relwidth = .65, relheight = 1 )

get_weather_button = tkinter.Button(
top_frame, bg = "white", fg = "blue", text ="Look out the window",
font = 40, command = lambda: test_funtion(entry.get())
)

get_weather_button.place(relx = .7, rely = 0, relwidth = .3, relheight = 1 )



#LOWER FRAME
lower_frame = top_frame = tkinter.Frame(root, bg = "Indigo", bd = 5)
lower_frame.place(anchor = 'n', relx = .5, rely = .3, relwidth = .75, relheight = .6) 


response = tkinter.Label(lower_frame, text = "This is a label.", bg = 'white', font= 40, bd = 5)
response.place(anchor = 'n', relx = .5, relwidth = 1, relheight = 1) 








# frame = tkinter.Frame(root, bg = "#326ecf")
# frame.place(relx = 0, rely = 0, relwidth = .2, relheight = .2)

# frame2 = tkinter.Frame(root, bg = "#326ecf")
# frame2.place(relx = 0.2, rely = .2,relwidth = .2, relheight = .2)

# frame3 = tkinter.Frame(root, bg = "#326ecf")
# frame3.place(relx = 0.4, rely = 0.4, relwidth = .2, relheight = .2)

# frame4 = tkinter.Frame(root, bg = "#326ecf")
# frame4.place(relx = 0.6, rely = 0.6, relwidth = .2, relheight = .2)






#Make a button!
                    #root = window location
# button = tkinter.Button(frame, bg = "white", fg = "blue", text ="Hello")
# button2 = tkinter.Button(frame2, text = "What's up?")
# button3 = tkinter.Button(frame3, bg = "black", fg = "white", text ="#3")
# button4 = tkinter.Button(frame4, bg = "white", fg = "black", text ="#4")
# button.pack()
# button2.pack()
# button3.pack()
# button4.pack()


# #make a label
# # label = tkinter.Label(frame, text = "This is a label.", bg = 'orange' )
# # label2 = tkinter.Label(frame2, text = "This is label2.", bg = 'red' )
# # label3 = tkinter.Label(frame3, text = "This is label3.", bg = 'purple', fg = "white" )
# # label4 = tkinter.Label(frame4, text = "This is label4.", bg = 'grey', fg = "white" )
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







#what is pillow ? Image library.  











root.mainloop()