#The FrontEnd


from tkinter import *
import tkinter.messagebox

class Student:

    def __init__(self,root):
        self.root = root
        self.root.title("Database system")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg = "#0000ff")

    #Creating variables and assigning each one.
        Firstname = StringVar()
        Surname = StringVar()
        Dob = StringVar()
        Age = StringVar()
        Mobile = StringVar()
        Post_Code = StringVar()



        Basic_Frame = Frame(self.root, bg = "#0000ff")
        Basic_Frame.grid()

        Title_Frame = Frame(Basic_Frame, bd = 2, padx = 54, pady = 8, bg= "#FFFFFF", relief = RIDGE)
        Title_Frame.pack(side=TOP)


        self.Title_label = Label(Title_Frame, font = ('arial, 40, bold'), text = "Database management", bg = "white")
        self.Title_label.grid()

        Frame_Button = Frame(Basic_Frame, bd=2, width = 1350, height = 70, padx = 18, pady=10, bg = "white", relief=RIDGE)
        Frame_Button.pack(side = BOTTOM)

        DataFrame = Frame(Basic_Frame, bd = 1, width = 1300, height = 600, padx = 20, relief=RIDGE, bg = "white")
        DataFrame.pack(side = BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width = 1000, height = 600, padx = 20, relief=RIDGE, bg = "blue")
        DataFrameLEFT.pack(side = LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width = 450, height = 200, padx = 31, pady=3, relief=RIDGE, BG = "white")
        DataFrameRIGHT.pack(side = RIGHT)


if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()

    
