from math import pi,sin
from observer import *

class Generator(Subject):
    def __init__(self,a=1.0,f=1.0,p=0.0,name="Unnamed", color="red"):
        Subject.__init__(self)
        self.signal = []
        self.a, self.f, self.p = a, f, p
        self.generate_signal()
        self.name = name
        self.color = color
        self.visible = True

    def generate_signal(self):
        del self.signal[0:]
        samples=1000
        for t in range(0,samples,5):
            samples=float(samples)
            e=self.a*sin((2*pi*self.f*(t*1.0/samples))-self.p)
            self.signal.append((t*1.0/samples,e))
        self.notify()

    def is_visible(self):
        return self.visible

    def display(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_magnitude(self,a):
        self.a=a
        self.generate_signal()
    
    def get_magnitude(self):
        return self.a
    
    def set_frequency(self,f):
        self.f=f
        self.generate_signal()
    
    def get_frequency(self):
        return self.f
    
    def set_phase(self,p):
        self.p=p
        self.generate_signal()
    
    def get_phase(self):
        return self.p

    def get_signal(self):
        return self.signal
