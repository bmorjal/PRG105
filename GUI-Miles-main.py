import tkinter


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.middle_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.title_gallons = tkinter.Label(self.top_frame, text="How many gallons does your car hold: ")
        self.entry_gallon = tkinter.Entry(self.top_frame, width=15)
        self.title_gallons.pack(side="top")
        self.entry_gallon.pack(side="bottom")

        self.title_miles = tkinter.Label(self.middle_frame, text="How many miles did you travel: ")
        self.entry_miles = tkinter.Entry(self.middle_frame, width=15)
        self.title_miles.pack(side="top")
        self.entry_miles.pack(side="bottom")

        self.value = tkinter.StringVar()
        self.results = tkinter.Label(self.bottom_frame, textvariable=self.value)
        self.calc = tkinter.Button(self.bottom_frame, text="Calculate", command=self.calculate)
        self.quit = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        self.results.pack(side="top")
        self.calc.pack(side="left")
        self.quit.pack(side="right")

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def calculate(self):
        gas = float(self.entry_gallon.get())
        miles = float(self.entry_miles.get())

        mpg = "You get " + format(miles/gas, ",.2f") + " miles per gallon"
        self.value.set(mpg)


mygui = MyGui()
