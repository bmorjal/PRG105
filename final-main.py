import tkinter
import tkinter.messagebox


class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Welcome Menu')

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.add = tkinter.Radiobutton(self.top_frame, text='Addition', variable=self.radio_var, value=1)
        self.sub = tkinter.Radiobutton(self.top_frame, text='Subtraction', variable=self.radio_var, value=2)
        self.multi = tkinter.Radiobutton(self.top_frame, text='Multiplication', variable=self.radio_var, value=3)
        self.div = tkinter.Radiobutton(self.top_frame, text='Division', variable=self.radio_var, value=4)

        self.add.pack(anchor='w', padx=20)
        self.sub.pack(anchor='w', padx=20)
        self.multi.pack(anchor='w', padx=20)
        self.div.pack(anchor='w', padx=20)

        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.master.destroy)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

    def open_menu(self):
        if self.radio_var.get() == 1:
            _ = AddGUI(self.master)
        elif self.radio_var.get() == 2:
            _ = SubGUI(self.master)
        elif self.radio_var.get() == 3:
            _ = MultiGUI(self.master)
        elif self.radio_var.get() == 4:
            _ = DivGUI(self.master)
        else:
            tkinter.messagebox.showinfo('Function', 'still under construction')


class AddGUI:
    def __init__(self, master):
        self.add = tkinter.Toplevel(master)
        self.add.title("Addition Calculator")

        self.top_frame = tkinter.Frame(self.add)
        self.middle_frame = tkinter.Frame(self.add)
        self.bottom_frame = tkinter.Frame(self.add)

        self.add_label1 = tkinter.Label(self.top_frame, text='Enter first number: ')
        self.add_entry1 = tkinter.Entry(self.top_frame, width=15)
        self.add_label1.pack(side='left')
        self.add_entry1.pack(side='left')

        self.add_label2 = tkinter.Label(self.middle_frame, text='Enter second number:')
        self.add_entry2 = tkinter.Entry(self.middle_frame, width=15)
        self.add_label2.pack(side='left')
        self.add_entry2.pack(side='left')

        self.value = tkinter.StringVar()
        self.results = tkinter.Label(self.bottom_frame, textvariable=self.value)
        self.calc = tkinter.Button(self.bottom_frame, text="Calculate", command=self.calculate)
        self.back_button = tkinter.Button(self.bottom_frame, text="Main Menu", command=self.back)

        self.results.pack(side="top")
        self.calc.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def calculate(self):
        one = float(self.add_entry1.get())
        two = float(self.add_entry2.get())

        total = "The total is " + format(one + two, ",.2f")
        self.value.set(total)

    def back(self):
        self.add.destroy()


class SubGUI:
    def __init__(self, master):
        self.sub = tkinter.Toplevel(master)
        self.sub.title("Subtraction Calculator")

        self.top_frame = tkinter.Frame(self.sub)
        self.middle_frame = tkinter.Frame(self.sub)
        self.bottom_frame = tkinter.Frame(self.sub)

        self.sub_label1 = tkinter.Label(self.top_frame, text='Enter first number: ')
        self.sub_entry1 = tkinter.Entry(self.top_frame, width=15)
        self.sub_label1.pack(side='left')
        self.sub_entry1.pack(side='left')

        self.sub_label2 = tkinter.Label(self.middle_frame, text='Enter second number:')
        self.sub_entry2 = tkinter.Entry(self.middle_frame, width=15)
        self.sub_label2.pack(side='left')
        self.sub_entry2.pack(side='left')

        self.value = tkinter.StringVar()
        self.results = tkinter.Label(self.bottom_frame, textvariable=self.value)
        self.calc = tkinter.Button(self.bottom_frame, text="Calculate", command=self.calculate)
        self.back_button = tkinter.Button(self.bottom_frame, text="Main Menu", command=self.back)

        self.results.pack(side="top")
        self.calc.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def calculate(self):
        one = float(self.sub_entry1.get())
        two = float(self.sub_entry2.get())

        total = "The total is " + format(one - two, ",.2f")
        self.value.set(total)

    def back(self):
        self.sub.destroy()


class MultiGUI:
    def __init__(self, master):
        self.multi = tkinter.Toplevel(master)
        self.multi.title("Multiplication Calculator")

        self.top_frame = tkinter.Frame(self.multi)
        self.middle_frame = tkinter.Frame(self.multi)
        self.bottom_frame = tkinter.Frame(self.multi)

        self.multi_label1 = tkinter.Label(self.top_frame, text='Enter first number: ')
        self.multi_entry1 = tkinter.Entry(self.top_frame, width=15)
        self.multi_label1.pack(side='left')
        self.multi_entry1.pack(side='left')

        self.multi_label2 = tkinter.Label(self.middle_frame, text='Enter second number:')
        self.multi_entry2 = tkinter.Entry(self.middle_frame, width=15)
        self.multi_label2.pack(side='left')
        self.multi_entry2.pack(side='left')

        self.value = tkinter.StringVar()
        self.results = tkinter.Label(self.bottom_frame, textvariable=self.value)
        self.calc = tkinter.Button(self.bottom_frame, text="Calculate", command=self.calculate)
        self.back_button = tkinter.Button(self.bottom_frame, text="Main Menu", command=self.back)

        self.results.pack(side="top")
        self.calc.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def calculate(self):
        one = float(self.multi_entry1.get())
        two = float(self.multi_entry2.get())

        total = "The total is " + format(one * two, ",.2f")
        self.value.set(total)

    def back(self):
        self.multi.destroy()


class DivGUI:
    def __init__(self, master):
        self.Div = tkinter.Toplevel(master)
        self.Div.title("Division Calculator")

        self.top_frame = tkinter.Frame(self.Div)
        self.middle_frame = tkinter.Frame(self.Div)
        self.bottom_frame = tkinter.Frame(self.Div)

        self.Div_label1 = tkinter.Label(self.top_frame, text='Enter first number: ')
        self.Div_entry1 = tkinter.Entry(self.top_frame, width=15)
        self.Div_label1.pack(side='left')
        self.Div_entry1.pack(side='left')

        self.Div_label2 = tkinter.Label(self.middle_frame, text='Enter second number:')
        self.Div_entry2 = tkinter.Entry(self.middle_frame, width=15)
        self.Div_label2.pack(side='left')
        self.Div_entry2.pack(side='left')

        self.value = tkinter.StringVar()
        self.results = tkinter.Label(self.bottom_frame, textvariable=self.value)
        self.calc = tkinter.Button(self.bottom_frame, text="Calculate", command=self.calculate)
        self.back_button = tkinter.Button(self.bottom_frame, text="Main Menu", command=self.back)

        self.results.pack(side="top")
        self.calc.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def calculate(self):
        one = float(self.Div_entry1.get())
        two = float(self.Div_entry2.get())

        total = "The total is " + format(one / two, ",.2f")
        self.value.set(total)

    def back(self):
        self.Div.destroy()


def main():
    # create a window
    root = tkinter.Tk()
    # call the GUI and send it the root menu
    # use _ as variable name because the variable will not be needed after instantiating GUI
    # the GUI itself will handles the remaining program logic
    _ = GUI(root)
    # control the mainloop from main instead of the class
    root.mainloop()


main()
