import tkinter


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        # converts to strings
        self.name_value = tkinter.StringVar()
        self.street_value = tkinter.StringVar()
        self.csz_value = tkinter.StringVar()
        # sets the frames for objects
        self.info_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        # labels for the info, connects to the string conversion
        self.name_label = tkinter.Label(self.info_frame, textvariable=self.name_value)
        self.street_label = tkinter.Label(self.info_frame, textvariable=self.street_value)
        self.csz_label = tkinter.Label(self.info_frame, textvariable=self.csz_value)
        # packs and places them in
        self.name_label.pack()
        self.street_label.pack()
        self.csz_label.pack()
        # buttons
        self.show_info_button = tkinter.Button(self.button_frame, text="Show info", command=self.show)
        self.quit_button = tkinter.Button(self.button_frame, text="Quit", command=self.main_window.destroy)
        # positions the buttons
        self.show_info_button.pack(side="left")
        self.quit_button.pack(side="right")
        # sets the both frames into positions
        self.info_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()
    # Show has the values being used in command show
    
    def show(self):
        self.name_value.set("Blake Morjal")
        self.street_value.set("8900 NW Highway")
        self.csz_value.set("Crystal Lake, IL, 60012")


mygui = MyGui()
