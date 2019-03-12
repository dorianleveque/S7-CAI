# -*- coding: utf-8 -*-
from math import sin, pi
#from tkinter import *
from Tkinter import *
# import tkinter.filedialog
# import tkFileDialog

class Oscilloscope(Canvas):
    "Oscilloscope: version 1"
    def __init__(self,parent=None, width=200,height=150, formats= [('Postcript','*.ps')]):
        Canvas.__init__(self)
        parent.title("Oscilloscope : version 1")
        self.width,self.height=width,height
        self.configure(width=self.width,height=self.height)
        self.curve=[]
        self.formats = formats
    def grid(self, steps):
        self.create_line(10,self.height/2,
                         self.width,self.height/2,
                         arrow="last")
        self.create_line(10, self.height-5, 10, 5, arrow="last")
        step=(self.width-10)/steps*1.
        for t in range(1,steps+2):
            x =t*step
            self.create_line(x,self.height/2-4,x,self.height/2+4)

    def vibration(self,mag=10,phase=0,freq=1):
        del self.curve[0:]
        milliseconds=1000
        duration=milliseconds*1.0
        step=(self.width-10)/duration*1.0
        for t in range(0,milliseconds+1,5):
            e=mag*sin(2*pi*freq*(t/duration)-phase)
            x=10+t*step
            y=self.height/2-e*self.height/25
            self.curve.append((x,y))
        return
    def draw_curve(self,color="red"):
        if len(self.curve) > 1 :
            curve_id = self.create_line(self.curve,fill=color,smooth=1)
        return curve_id

    def save(self) :
        nomFichier = tkFileDialog.asksaveasfilename(parent=root,filetypes=self.formats,title="Sauvez l'image sous...")

        self.postscript(file="oscillo.ps", colormode='color')
if __name__ == "__main__" :
    root = Tk()
    oscillo = Oscilloscope(root,300)
    oscillo.configure(bg ='ivory', bd=2, relief="sunken")
    oscillo.grid(8)
    oscillo.vibration(10, 1.2, 2)
    oscillo.draw_curve()
    oscillo.vibration(phase=1.57)
    oscillo.draw_curve(color="purple")
    oscillo.vibration(phase=3.14)
    oscillo.draw_curve(color="dark green")
    oscillo.pack()
#    oscillo.save()
    root.mainloop()
