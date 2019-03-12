from math import sin,pi
from Tkinter import Tk,Toplevel,Canvas,Scale
from observer import *

class Generator(Subject) :
    def __init__(self):
        Subject.__init__(self)
        self.signal=[]
        self.a,self.f,self.p=1.0,1.0,0.0
        self.generate_signal()
    def set_magnitude(self,a):
        self.a=a
        self.generate_signal()
    def generate_signal(self):
        del self.signal[0:]
        samples=1000
        for t in range(0, samples,5):
            samples=float(samples)
            e=self.a*sin((2*pi*self.f*(t*1.0/samples))
                         -self.p)
            self.signal.append((t*1.0/samples,e))
        self.notify()
        return self.signal
    def get_signal(self) :
        return self.signal
class Controller :
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.view.magnitude.bind("<B2-Motion>",
                                 self.update_magnitude)
    def update_magnitude(self,event):
        x=int(event.widget.get())
        self.model.set_magnitude(x)
        self.model.generate_signal()

class Screen(Observer):
    def __init__(self,parent,bg="white"):
        self.canvas=Canvas(parent,bg=bg)
        self.signal_id=None
        self.magnitude=Scale(parent,length=250,
                             orient="horizontal",
                             label="Magnitude",
                             sliderlength=20,
                             showvalue=0,from_=0,to=5,
                             tickinterval=25)
    def update(self,model):
        signal=model.get_signal()
        self.plot_signal(signal)
    def plot_signal(self,signal,color="red"):
        signal_id=None
        w=self.canvas.cget("width")
        h=self.canvas.cget("height")
        width,height=int(w),int(h)
        if self.canvas.find_withtag("signal") :
            self.canvas.delete("signal")
        if signal and len(signal) > 1:
            plot=[ (x*width, height/2.0*(y+1))
                    for (x, y) in signal ]
            signal_id=self.canvas.create_line(plot,
                                         fill=color,
                                         smooth=1,
                                         width=3,
                                         tags="signal")
        return signal_id

    def grid(self, steps):
        w=self.canvas.cget("width")
        h=self.canvas.cget("height")
        width,height=int(w),int(h)
        self.canvas.create_line(10,height/2,
                                width,height/2,
                                arrow="last")
        self.canvas.create_line(10,height-5,
                                10,5,arrow="last")
        step=(width-10)/steps*1.
        for t in range(1,steps+2):
            x =t*step
            self.canvas.create_line(x,height/2-4,
                                        x,height/2+4)
    def packing(self) :
        self.canvas.pack()
        self.magnitude.pack()
        
if __name__ == "__main__" :
    root = Tk()
    root.title("Oscilloscope v.1")
    model=Generator()
    view=Screen(root)
    view.grid(8)
    model.attach(view)
    view.update(model)
    view.packing()
    ctrl=Controller(model,view)
    top=Toplevel(root)
    view=Screen(top,model)
    view.grid(20)
    view.packing()
    model.attach(view)
    root.mainloop()
