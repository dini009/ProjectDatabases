#The FrontEnd


from tkinter import *
import tkinter.messagebox

class Student:

    def __init__(self,root):
        self.root = root
        self.root.title("Database system")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg = "#0000ff")

        #Creating variables and assigning each one an empty value so user can enter their own values.
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


        self.Title_label = Label(Title_Frame, font = ('arial', 40, 'bold'), text = "Database management System", bg = "white")
        self.Title_label.grid()

        


if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()

    

    

    















