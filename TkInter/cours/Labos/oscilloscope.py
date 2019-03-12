from Tkinter import Tk,Toplevel,Canvas,Scale
from observer import *
from generator import *
from view import *
from controller import *
 
if  __name__ == "__main__" : 
    root=Tk()
    model=Generator()
    view=Screen(root)
    view.grid(8)
    view.update(model)
    model.attach(view)
    ctrl=Controller(model,view)
    view.packing()

    root.mainloop()
    
     
