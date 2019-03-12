#http://autourducode.com/le-design-patter-observer-et-ses-variantes
# observables  : notify (to observers) , add (observer)

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

# observables  : notify (state changes)
class Observer:
    def update(self, subject):
        raise NotImplementedError
