


#MAKE FRAME FOR SLEEP.  



def main(root, all_data):
# new imports...

    import tkinter as tk, customtkinter as ctk

    import noob_button_functions
    import Noob_Summary as summary


    top_frame_2_sleep = ctk.CTkFrame(master = root, corner_radius = 20)
    tframegrid2_sleep ={"frame": top_frame_2_sleep, "column" : 2,  "padx" : 5, "pady" : 5, "row" : 0,"columnspan" : 1, "rowspan" : 3, "sticky": 'ew'}

    def sleep_button_press():
        noob_button_functions.clear_frame(top_frame_2_sleep)
        noob_button_functions.create_frame(tframegrid2_sleep)
        summary.main(root,all_data,"sleep")

        def minute_slider_event(value):
            minute_label = ctk.CTkLabel(master = top_frame_2_sleep, text = f"{value} Minutes")
            minute_label.grid(column = 0,  padx = 5, pady = 5, row =1, rowspan = 1)     
        def hour_slider_event(value):
            hour_label = ctk.CTkLabel(master = top_frame_2_sleep, text = f"{value} Hours")
            hour_label.grid(column = 0,  padx = 5, pady = 5, row =3, rowspan = 1)     
            
        #labels : 
        how_long_sleep = ctk.CTkLabel(master = top_frame_2_sleep, text = "How long did the baby sleep for?")
        minute_label = ctk.CTkLabel(master = top_frame_2_sleep, text = "Minutes")
        hour_label = ctk.CTkLabel(master = top_frame_2_sleep, text = "Hours")

        #Sliders : 
        minute_slider = ctk.CTkSlider(master=top_frame_2_sleep, from_=0, to=60,number_of_steps = 12, command=minute_slider_event)
        hour_slider = ctk.CTkSlider(master=top_frame_2_sleep,  from_=0, to=16,number_of_steps = 32, command=hour_slider_event)
        
        #Grid Placement : 
        how_long_sleep.grid(column = 0,  padx = 5, pady = 5, row =0, rowspan = 1)
        minute_label.grid(column = 0,  padx = 5, pady = 5, row =1, rowspan = 1)     
        minute_slider.grid(column = 0,  padx = 5, pady = 5, row = 2, rowspan = 1, columnspan=1)

        hour_label.grid(column = 0,  padx = 5, pady = 5, row = 3, rowspan = 1)     
        hour_slider.grid(column = 0,  padx = 5, pady = 5, row = 4, rowspan = 1, columnspan=1)


    sleep_button_press()






if __name__ == '__main__':
    main()


