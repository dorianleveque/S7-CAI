# -*- coding: utf-8 -*-
from Tkinter import Tk,Toplevel,Scale,Frame,Canvas,IntVar

from observer import Observer
from generator import *

from views import *
from controls import *

class Oscilloscope(object) :
    def __init__(self,parent):
        print("Oscilloscope : __init__")
        self.model=Generator()
        self.view=View(parent,self.model)
        self.model.attach(self.view)
        self.view.grid(10)
        self.controls=Controller(parent,self.model)

    def get_model(self) :
        return self.model
    def set_model(self,model) :
        self.model=model
    
    def packing(self) :
        self.view.packing()
        self.controls.packing()
        
if  __name__ == "__main__" : 
    root=Tk()
    oscillo=Oscilloscope(root)
    oscillo.packing()

##    top=Toplevel()
##    oscillo=Oscilloscope(top)
##    oscillo.packing()
##
##    top=Toplevel()
##    view=View(top,oscillo.get_model())
##    oscillo.get_model().attach(view)
##    view.grid(10)
##    view.packing()
    
    root.mainloop()
