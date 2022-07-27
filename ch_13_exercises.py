"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import tkinter
import tkinter.messagebox

# TODO 13.2 Using the tkinter Module
print("=" * 10, "Section 13.2 using tkinter", "=" * 10)
# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter. Use the class name MyGUI2


class MyGui2:

    def __init__(self):

        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text='Blake Morjal')
        self.label.pack()
        tkinter.mainloop()


# my_gui = MyGui2()


# TODO 13.3 Adding a label widget
print("=" * 10, "Section 13.3 adding a label widget", "=" * 10)
# Add a label to MyGUI2 (above) that prints your first and last name; pack the label
# Create an instance of MyGUI2

# TODO 13.4 Organizing Widgets with Frames
print("=" * 10, "Section 13.4 using frames", "=" * 10)
# Create a MyGUI3 class that creates a window with two frames
# In the top Frame add labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester
# Create an instance of MyGUI3


class MyGui3:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text="Blake Morjal")
        self.label2 = tkinter.Label(self.top_frame, text="Web design and development")

        self.label1.pack(side="top")
        self.label2.pack(side="top")

        self.label3 = tkinter.Label(self.bottom_frame, text="PRG 105")
        self.label4 = tkinter.Label(self.bottom_frame, text="PRG 147")

        self.label3.pack(side="left")
        self.label4.pack(side="left")

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


# my_gui3 = MyGui3()


# TODO 13.5 Button Widgets and info Dialog Boxes
print("=" * 10, "Section 13.5 button widgets and info dialogs", "=" * 10)
# Create a GUI that will tell a joke
# Use a button to show the punch line, which should appear in a dialog box
# Create an instance of the GUI


class MyGui4:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.joke = tkinter.Label(self.main_window, text="Why did the chicken climb the ladder?")

        self.why = tkinter.Button(self.main_window, text="Why?", command=self.punchline)

        self.joke.pack()
        self.why.pack()

        tkinter.mainloop()

    def punchline(self):
        tkinter.messagebox.showinfo("Response", "Because it didn't wanna become deep fried!")


# mygui4 = MyGui4()


# TODO 13.6 getting input / 13.7 Using Labels as output fields
print("=" * 10, "Section 13.6-13.7 input and output using Entry and Label", "=" * 10)
# Using the program in 13.10 kilo converter as a sample,
# create a program to convert inches to centimeters

print("Honestly I have no idea, I don't have access to the book, so I'm stumped on this one")
