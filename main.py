#The FrontEnd


from tkinter import *
import tkinter.messagebox


class Application:

    def __init__(self, root):
        self.root = root
        self.root.title("")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg = "#0000ff")

      

        

        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Grades = StringVar()
        Nationality = StringVar()
        Street_Name = StringVar()
        postal_Code = StringVar()
        City = StringVar()
        phone_number = StringVar()
        Email_address = StringVar()
        Study_Name = StringVar()
        Year_of_Study = StringVar()
        Study_counsellor = StringVar()

        




    
root = Tk()
app= Application(root)
root.mainloop()

    

    

    















