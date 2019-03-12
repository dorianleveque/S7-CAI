# http://autourducode.com/le-design-patter-observer-et-ses-variantes
# observables  : notify (to observers) , add (observer)
from Tkinter import Tk,Toplevel,Frame,Scale,Label,IntVar

class Subject(object):
    def __init__(self):
        self.observers=[]
    def notify(self):
        for obs in self.observers:
            obs.update(self)
    def attach(self, obs):
        if not hasattr(obs,"update"):
            raise ValueError("Observer must have an update() method")
        self.observers.append(obs)
    def detach(self, obs):
        if obs in self.observers :
            self.observers.remove(obs)

class Car(Subject):
    def __init__(self):
        Subject.__init__(self)
        self.speed=0
        self.rpm=1000
        self.gearbox_speed=0
        self.gearbox=[0,0.006,0.009,0.012,0.014]
    def accelerate(self,value):
#        print("accelerate",self.gearbox_speed)
        if value==0 :
            self.rpm=1000
        else :
            self.rpm=1000*value
            self.speed=self.rpm*self.gearbox[self.gearbox_speed]
        self.notify()
    def downshift(self,value):
        self.gearbox_speed=value
        self.speed=self.rpm*self.gearbox[self.gearbox_speed]
        self.rpm=+1000
        self.notify()
    def upshift(self,value):
        if value<len(self.gearbox):
            self.gearbox_speed=value
            self.speed=self.rpm*self.gearbox[self.gearbox_speed]
            if self.rpm > 1000 :
                self.rpm-=1000
            self.notify()
    def get_gearbox(self) :
            return self.gearbox
    def get_gearbox_speed(self) :
            return self.gearbox_speed
    def get_speed(self) :
            return self.speed
    def set_speed(self,speed) :
            self.speed=speed

# observers  :  update (state of the Model has  changed)
class Observer:
    def update(self, subject):
        raise NotImplementedError

class Dashboard(Observer) :
    def __init__(self,parent):
        self.parent=parent
        self.speed=Label(parent)
        self.rpm=Label(parent)
        self.speed.pack()
        self.rpm.pack()
    def update(self, subject):
#        print("update()",subject.rpm,subject.speed)
        if subject.rpm>=1 and subject.speed>=0  :
            self.speed.configure(text=str(subject.speed))
            self.rpm.configure(text=str(subject.rpm))
        else :
            self.speed.configure(text=str(0))
            self.rpm.configure(text=str(0))

# observers  :  change the state of the Model)

class Gearbox :
    def __init__(self,parent,model):
        self.model=model
        self.speed_data=IntVar()
        self.accelerator=Scale(parent,variable=self.speed_data,
                               label="Acceleration",
                               orient="horizontal",length=200,
                               from_=0,to=10,
                               showvalue=0,
                               tickinterval=1,
                               command=self.update_speed)
        self.gear_data=IntVar()
        self.gear=Scale(parent,variable=self.gear_data,
                             label="Gear Speed",
                             orient="horizontal",length=200,
                             from_=0,to=4,
                             showvalue=0,
                             tickinterval=1,
                             command=self.update_gear)
        self.accelerator.pack()
        self.gear.pack()

    def update_speed(self,event):
        self.model.accelerate(self.speed_data.get())

    def update_gear(self,event):
#        print("update_gear()",self.model.get_gearbox_speed())
#        print("update_gear()",self.gear_data.get())
        if self.model.get_gearbox_speed() < self.gear_data.get() :
            self.model.upshift(self.gear_data.get())
        elif self.model.get_gearbox_speed() > self.gear_data.get() :
            self.model.downshift(self.gear_data.get())
        self.speed_data.set(self.speed_data.get()-2)
    
if __name__ == "__main__" :
    root=Tk()
    model=Car()
    view=Dashboard(root)
    model.attach(view)
    control=Gearbox(root,model)
##    view=Dashboard(root)
##    model.attach(view)
##    control=Gearbox(root,model)
####    top=Toplevel()
####    view=Dashboard(top)
####    model=Car()
####    model.attach(view)
####    control=Gearbox(top,model)
    root.mainloop()

