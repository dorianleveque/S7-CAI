from Tkinter import Canvas,Scale
from observer import *

class Screen(Observer):
    def __init__(self,parent,bg="white"):
        self.canvas=Canvas(parent,bg=bg)
        print("parent",parent.cget("width"),parent.cget("height"))
        self.magnitude=Scale(parent,length=250,orient="horizontal",
                         label="Magnitude", sliderlength=20,
                         showvalue=0,from_=0,to=5,
                         tickinterval=25)
    def update(self,model):
        print("View update")
        signal=model.get_signal()
        self.plot_signal(signal)

    def get_magnitude(self):
        return self.magnitude
        
    def plot_signal(self,signal,color="red"):
        w,h=self.canvas.cget("width"),self.canvas.cget("height")
        width,height=int(w),int(h)
#        print(self.canvas.find_withtag("signal"))
        if self.canvas.find_withtag("signal") :
            self.canvas.delete("signal")
        if signal and len(signal) > 1:
            plot = [(x*width, height/2.0*(y+1)) for (x, y) in signal]
            signal_id = self.canvas.create_line(plot, fill=color, smooth=1, width=3,tags="signal")
        return

    def grid(self, steps):
        w,h=self.canvas.cget("width"),self.canvas.cget("height")
        width,height=int(w),int(h)
        self.canvas.create_line(10,height/2,width,height/2,arrow="last")
        self.canvas.create_line(10,height-5,10,5,arrow="last")
        step=(width-10)/steps*1.
        for t in range(1,steps+2):
            x =t*step
            self.canvas.create_line(x,height/2-4,x,height/2+4)

    def packing(self) :
        self.canvas.pack()
        self.magnitude.pack()
 
