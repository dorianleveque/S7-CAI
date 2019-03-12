#http://python.6.x6.nabble.com/TK-MVC-td1119473.html

#!/usr/bin/python
from observer import *
import Tkinter as tk

class Model(Subject):
    def __init__(self, names=[]):
        Subject.__init__(self)
        self._data = names
    def get_data(self):
        return self._data
    def insert(self,name):
        self._data.append(name)
        self.notify()
    def delete(self, index):
        del self._data[index]
        self.notify()

class View(Observer):
    def __init__(self,parent):
         self.parent=parent
         self.list=tk.Listbox(parent)
         self.list.configure(height=4)
         self.list.pack()
         self.entry=tk.Entry(parent)
         self.entry.pack()
    def update(self,model):
        self.list.delete(0, "end")
        for data in model.get_data():
            self.list.insert("end", data)

class Controller(object):
     def __init__(self,model,view):
          self.model,self.view = model,view
          self.view.entry.bind("<Return>",
                               self.enter_action)
          self.view.list.bind("<Delete>",
                              self.delete_action)
     def enter_action(self, event):
          data = self.view.entry.get()
          self.model.insert(data)
     def delete_action(self, event):
          for index in self.view.list.curselection():
             self.model.delete(int(index))

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Men")
    names=["Jean", "John", "Joe"]
    model = Model(names)
    view = View(root)
    view.update(model)
    model.attach(view)
    ctrl = Controller(model,view)
    top = tk.Toplevel()
    top.title("Men")
    view = View(top)
    view.update(model)
    model.attach(view)
    ctrl = Controller(model,view)
    top = tk.Toplevel()
    top.title("Women")
    names=["Jeanne", "Joanna", "Jeanette"]
    model = Model(names)
    view = View(top)
    view.update(model)
    model.attach(view)
    ctrl = Controller(model,view)
    root.mainloop()
