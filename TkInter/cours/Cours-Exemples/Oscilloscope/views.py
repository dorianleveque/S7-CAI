from Tkinter import Tk,Toplevel,Canvas,Frame

from observer import Observer
from generator import *

class View(Observer):
    def __init__(self,parent,subject,bg="white"):
        print("View : __init__")
        Observer.__init__(self)
        self.subject=subject
        self.parent=parent
        self.signal_id=None
        self.canvas=Canvas(parent,bg=bg)
        self.canvas.bind("<Configure>", self.resize)
        self.width=int(self.canvas.cget("width"))
        self.height=int(self.canvas.cget("height"))

    def update(self,subject):
        print("View : update")
        signal=subject.get_signal()
        self.signal_id=self.plot_signal(signal)
    def plot_signal(self,signal,color="red"):
        width,height=self.width,self.height
        if self.signal_id!=None :
            self.canvas.delete(self.signal_id)
        if signal and len(signal)>1:
            plot=[(x*width, height/2.0*(y+1)) for (x, y) in signal]
            self.signal_id=self.canvas.create_line(plot,fill=color,smooth=1,width=3)
        return self.signal_id

    def resize(self, event):
        """
        En cas de reconfiguration de fenetre
        """
        if event:
            self.width = event.width
            self.height = event.height
##            self.width = int(event.widget.cget("width"))
##            self.height = int(event.widget.cget("height"))
##            print("View : resize cget",event.widget.cget("width"),event.widget.cget("height"))
        print("View : resize event",event.width,event.height)
        self.canvas.delete("grid")
        self.plot_signal(self.subject.get_signal())
        self.grid()

    def grid(self, steps=8):
        width,height=self.width,self.height
#        self.canvas.create_line(10,height/2,width,height/2,arrow="last",tags="grid")
#        self.canvas.create_line(10,height-5,10,5,arrow="last",tags="grid")
        step=width/steps*1.
        for t in range(1,steps+2):
            x =t*step
            self.canvas.create_line(x,0,x,height,tags="grid")
            self.canvas.create_line(0,x,width,x,tags="grid")
            self.canvas.create_line(x,height/2-4,x,height/2+4,tags="grid")
    def packing(self) :
        self.canvas.pack(expand=1,fill="both",padx=6)

if  __name__ == "__main__" : 
    root=Tk()
    model=Generator()
    view=View(root,model)
    view.grid(10)
    view.packing()
    root.mainloop()
