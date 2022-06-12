



def main(root):

    import customtkinter as ctk
    #List of Frames:
    global top_frame_1

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









if __name__ == '__main__':
    main()


