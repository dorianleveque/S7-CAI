# -*- coding: utf-8 -*-

from Tkinter import Tk,Toplevel,Scale,Frame,IntVar

from observer import Observer
from generator import *

class Controller(Observer):
    def __init__(self,parent,subject):
        print("Controller : __init__")
        self.subject=subject
        self.amp=IntVar()
        self.scale_amp=Scale(parent,variable=self.amp,
                          label="Amplitude",
                          orient="horizontal",length=250,
                          from_=0,to=5,relief="sunken",
                          sliderlength=20,tickinterval=1,
                          command=self.update_amplitude)
        self.freq=IntVar()
        self.scale_freq=Scale(parent,variable=self.freq,
                          label="Frequence",
                          orient="horizontal",length=250,
                          from_=0,to=5,relief="sunken",
                          sliderlength=20,tickinterval=1,
                          command=self.update_frequence)
    def update(self,subject):
        pass
    def update_amplitude(self,event):
        print("Controller : update_amplitude",self.amp.get())
        self.subject.set_magnitude(self.amp.get())
    def update_frequence(self,event):
        print("Controller : update_frequence",self.freq.get())
        self.subject.set_frequency(self.freq.get())
    def packing(self) :
        self.scale_amp.pack(expand=1,fill="x",padx=6)
        self.scale_freq.pack(expand=1,fill="x",padx=6)

if  __name__ == "__main__" : 
    root=Tk()
    model=Generator()
    oscillo=Controller(root,model)
    oscillo.packing()
    root.mainloop()
