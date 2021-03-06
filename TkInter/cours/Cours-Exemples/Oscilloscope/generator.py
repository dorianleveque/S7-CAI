from math import sin,pi
from observer import Subject

class Generator(Subject) :
    def __init__(self,a=1.0,f=1.0,p=0.0):
        print("Generator : __init__")
        Subject.__init__(self)
        self.signal=[]
        self.a,self.f,self.p=a,f,p
    def get_signal(self):
        return self.signal
    def get_magnitude(self):
        return self.a
    def set_magnitude(self,a):
        self.a=a
        self.generate_signal()
    def get_frequency(self):
        return self.f
    def set_frequency(self,f):
        self.f=f
        self.generate_signal()
    def get_phase(self):
        return self.p
    def set_phase(self,p):
        self.p=p
        self.generate_signal()
    def generate_signal(self):
        print("Generator :generate_signal")
        del self.signal[0:]
        samples=1000
        for t in range(0, samples,5):
            samples=float(samples)
            e=self.a*sin((2*pi*self.f*(t*1.0/samples))-self.p)
            self.signal.append((t*1.0/samples,e))
        self.notify()
        return self.signal
