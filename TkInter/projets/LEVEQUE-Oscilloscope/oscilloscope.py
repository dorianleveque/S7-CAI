# -*- coding: utf-8 -*-
from Tkinter import Tk,Toplevel,Canvas,Scale
from tkMessageBox import * 
from observer import *
from generator import *
from view import *
from controller import *
import os
 
class Oscilloscope(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.option_add('*tearOff', False)
        self.option_readfile('config.txt')
        self.protocol('WM_DELETE_WINDOW', self.exit)
        self.models      = []
        signal1 = Generator(name="X", color='red')
        signal2 = Generator(name="Y", color='blue')
        self.add_model(signal1)
        self.add_model(signal2)
        self.view       = Screen(self)
        self.controls   = Controller(self, self.view)
        signal1.attach(self.view)
        signal2.attach(self.view)
        self.view.update(self.models)
        self.__last_save = {}
        
    def get_model(self, index) :
        print index
        return self.models[index]

    def get_models(self):
        return self.models

    def add_model(self,model) :
        self.models.append(model)
    
    def packing(self) :
        self.view.packing()

    def exit(self):
        if self.__is_new_save():
            if askyesno('Quitter ?', 
            """
            Des modifications ont été effectuées.
            Voulez vous sauvegarder ?
            """):
                self.save()
        self.destroy()

    def help(self):
        showinfo("A propos de nous", 
        """
        Cette application est le résultat d'une découverte de 
        TkInter au cours d'un de nos enseignement à l'ENIB
        (Ecole National d'Ingénieur de Brest)

        Créé par LEVEQUE Dorian (d5levequ@enib.fr)
        Version 1.0
        """)

    def open(self):
        formats = [('JSON','*.json')]
        filename = tkFileDialog.askopenfilename(title = "Selectionnez le fichier",filetypes = formats)
        if len(filename) > 0:
            print "Lecture en cours dans %s" % filename    
            with open(filename, "r") as f:
                data = json.load(f)
                self.models = []
                color=['red', 'blue', 'green']
                for index, key in enumerate(data):
                    signal = Generator(name=key, color=color[index])
                    signal.set_magnitude(data[key]['magnitude'])
                    signal.set_frequency(data[key]['frequency'])
                    signal.set_phase(data[key]['phase'])
                    self.add_model(signal)
                    signal.attach(self.view)
                self.view.update(self.get_models())
                self.controls.update_controls()

    def new(self):
        if self.__is_new_save():
            if askyesno('Sauvegarder ?', 
            """
            Des modifications ont été effectuées.
            Voulez vous sauvegarder ?
            """):
                self.save()
            signal = Generator()
            self.set_model(signal)
            signal.attach(self.view)
            self.view.update(self.get_model())
            self.controls.update_controls()

    def save(self):
        formats = [('JSON','*.json')]
        filename = tkFileDialog.asksaveasfilename(filetypes=formats,title="Sauvez le fichier sous...",initialfile="signals",defaultextension="*.*")
        filename = filename
        if len(filename) > 0:
            print "Sauvegarde en cours dans %s" % filename         
            with open(filename, "w") as f:
                json.dump(self.__create_save(), f)

    def __create_save(self):
        data = {}
        for m in self.get_models():
            data[m.get_name()] = {
                    'magnitude'   : m.get_magnitude(),
                    'frequency'   : m.get_frequency(),
                    'phase'       : m.get_phase()
                    }
        self.__last_save = data
        return data

    def __get_last_save(self):
        return self.__last_save

    def __is_new_save(self):
        """ Check if we have new change """
        last_save = self.__get_last_save()
        new_save = self.__create_save()
        for signal in new_save:
            if signal in last_save:
                for attribut in new_save[signal]:
                    if attribut in last_save[signal]:
                        if new_save[signal][attribut] == last_save[signal][attribut]:
                            return False
                        else:
                            return True
                    else:
                        return True
            else:
                return True

if  __name__ == "__main__" : 
 
    oscillo = Oscilloscope()
    oscillo.packing()    
    oscillo.mainloop()
    
     
