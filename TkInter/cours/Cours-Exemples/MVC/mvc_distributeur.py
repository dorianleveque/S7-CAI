from observer import *


class ATM(Subject):
    def __init__(self,amount):
        Subject.__init__(self)
        self.amount=amount
    def fill(self,amount):
        self.amount=self.amount+amount
        self.notify()
    def distribute(self,amount):
        self.amount=self.amount-amount
        self.notify()

class Amount(Observer):
    def __init__(self,name):
        self.name=name
    def update(self, subject):
        print(self.name, subject.amount)

if __name__ == "__main__" :
    amount=100
    dab = ATM(amount)
    obs=Amount("Observer 1")
    dab.attach(obs)
    obs=Amount("Observer 2")
    dab.attach(obs)
    n=5
    for i in range(1,amount/20) :
        dab.distribute(i*10)
    dab.detach(obs)
    dab.fill(amount)
