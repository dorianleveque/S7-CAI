from Tkinter import *

root = Tk()
root.title('Radiobutton')

fruit=[('Option 1', 1), ('Option 2', 2), ('Option 3', 3),
       ('Option 4', 4), ('Option 5', 5), ('Option 6', 6)]
var = IntVar()
for text, value in fruit:
    Radiobutton(root, text=text, value=value, variable=var).pack(anchor=W)
var.set(3)
root.mainloop()
