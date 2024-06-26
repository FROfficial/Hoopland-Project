# I will use tkinter to navigate the history collected from the simulated years.
from tkinter import *

# Create the window
root = Tk()
root.title('Hoopland Tracker Application')


myLabel = Label(root, text="Hoopland Official Season Tracker").grid(row=0, column=1)

myLabel = Label(root, text="View Regular Seasons").grid(row=6, column=0)
myLabel = Label(root, text="View Post-Seasons").grid(row=7, column=0)
myLabel = Label(root, text="View Season Awards").grid(row=8, column=0)
myLabel = Label(root, text="View Hall of Fame").grid(row=9, column=0)
myLabel = Label(root, text="Update Tracker").grid(row=10, column=0)


myButton = Button(root, text="View", padx=30, pady=15).grid(row=6, column=2)
myButton = Button(root, text="View", padx=30, pady=15).grid(row=7, column=2)
myButton = Button(root, text="View", padx=30, pady=15).grid(row=8, column=2)
myButton = Button(root, text="View", padx=30, pady=15).grid(row=9, column=2)
myButton = Button(root, text="Update", padx=24, pady=15).grid(row=10, column=2)

# Run the window
root.mainloop()

# function Definitions used: