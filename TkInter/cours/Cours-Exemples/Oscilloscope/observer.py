class Subject(object):
    def __init__(self):
        print("Subject : __init__")
        self.observers=[]
    def notify(self):
        print("Subject : notify",self.observers)
        for obs in self.observers:
            obs.update(self)
    def attach(self, obs):
        if not hasattr(obs,"update"):
            raise ValueError("Observer must have an update() method")
        print("Subject : attach",obs)
        self.observers.append(obs)
    def detach(self, obs):
        print("Subject : detach",obs)
        if obs in self.observers :
            self.observers.remove(obs)

# observer : update (observable state changes, change observable states)
class Observer:
    def __init__(self):
        print("Observer : __init__")
    def update(self,subject):
        print("Observer : update",self.observers)
