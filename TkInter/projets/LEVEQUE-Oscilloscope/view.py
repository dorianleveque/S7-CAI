# -*- coding: utf-8 -*-
from Tkinter import Canvas,Scale, Frame, Menu, Menubutton, RIGHT, LEFT, LabelFrame, Checkbutton
import ttk
import tkFileDialog
import json
from observer import *

class MenuBar(Frame):
    def __init__(self,parent):
        Frame.__init__(self,borderwidth=2)
        self.parent = parent

        # File Button Menu
        button_file = Menubutton(self,text="Fichier")
        menu_file   = Menu(button_file)
        menu_file.add_command(label="Nouveau",  command = self.parent.new)
        menu_file.add_command(label="Ouvrir",  command = self.parent.open)
        menu_file.add_command(label ="Sauvegarder",command = self.parent.save)
        menu_file.add_command(label ="Quitter",command = self.parent.exit)
        button_file.configure(menu=menu_file)
        button_file.pack(side=LEFT, fill="x")

        # Help Button Menu
        button_file = Menubutton(self, text="Aide")
        menu_help   = Menu(button_file)
        menu_help.add_command(label="A propos de nous", command = self.parent.help)
        button_file.configure(menu=menu_help)
        button_file.pack(side=LEFT)





class Screen(Observer):
    def __init__(self, parent, bg="white"):
        self.menu_bar = MenuBar(parent)
        self.canvas = Canvas(parent,bg=bg, name="screen")
        self.frameControl = Frame(parent)
        self.frameLabelSignals = LabelFrame(self.frameControl, text="Signaux", padx=20, pady=20)
        self.frameLabelMode = LabelFrame(self.frameControl, text="Mode", padx=20, pady=20)
        self.panelControl = ttk.Notebook(self.frameLabelSignals)
        self.checkbox_signalX = Checkbutton(self.frameLabelMode, text="Signal X")
        self.checkbox_signalY = Checkbutton(self.frameLabelMode, text="Signal Y")
        self.checkbox_XY = Checkbutton(self.frameLabelMode, text="XY")
        
        self.panel_control_page = [] # contient les références de mes curseurs
        
        for p in parent.get_models():
            self.addPage(p.get_name())
        
    def addPage(self, name):
        page = ttk.Frame(self.panelControl)
        self.panelControl.add(page, text='signal ' + name)

        visible_checkbox = Checkbutton(page, text="Afficher")
        magnitude = Scale(page, length=250,orient="horizontal",
                         label="Amplitude", sliderlength=20,
                         showvalue=0,from_=0,to=5,
                         tickinterval=1, name="magnitudeScale")
        frequency = Scale(page,length=250,orient="horizontal",
                         label="Frequency", sliderlength=20,
                         showvalue=0,from_=0,to=100,
                         tickinterval=10, name="frequencyScale")
        phase = Scale(page,length=250,orient="horizontal",
                         label="Phase", sliderlength=20,
                         showvalue=0,from_=0,to=360,
                         tickinterval=60, name="phaseScale")
        visible_checkbox.pack(expand=1,fill="x")
        magnitude.pack(expand=1,fill="both",pady=6)
        frequency.pack(expand=1,fill="both",pady=6)
        phase.pack(expand=1,fill="both",pady=6)
        self.panel_control_page.append({
            'magnitude': magnitude,
            'frequency': frequency,
            'phase': phase
        })

    def update(self,model):
        if type(model) == list:
            for i, m in enumerate(model):
                signal = m.get_signal()
                #self.plot_signal(signal, m.get_color())
                self.plot_signal(m)
        else:
            signal = model.get_signal()
            self.plot_signal(model)
        self.grid(6, 4)

    def get_panel_control_index(self):
        return self.panelControl.index('current')

    def get_canvas(self):
        return self.canvas

    def get_panel_control_page(self):
        return self.panel_control_page

    def get_magnitude(self, index):
        return self.panel_control_page[index]['magnitude']

    def get_frequency(self, index):
        return self.panel_control_page[index]['frequency']

    def get_phase(self, index):
        return self.panel_control_page[index]['phase']
        
    def get_checkbox_signalX(self):
        return self.checkbox_signalX

    def get_checkbox_signalY(self):
        return self.checkbox_signalY
    
    def get_checkbox_XY(self):
        return self.checkbox_XY

    def plot_signal(self,model):
        w,h=self.canvas.winfo_width(),self.canvas.winfo_height()
        width,height=int(w),int(h)

        signal = model.get_signal()
        name = model.get_name()
        color = model.get_color()

        if self.canvas.find_withtag("signal"+name) :
            self.canvas.delete("signal"+name)

        if signal and len(signal) > 1:
            plot = [(x*width, height/2.0*(y+1)) for (x, y) in signal]
            signal_id = self.canvas.create_line(plot, fill=color, smooth=1, width=3,tags="signal"+name)
        return signal_id

    def grid(self, row, col):
        w,h=self.canvas.winfo_width(),self.canvas.winfo_height()
        width,height=int(w),int(h)

        if self.canvas.find_withtag("grid") :
            self.canvas.delete("grid")

        # dessin des axes X et Y
        self.canvas.create_line(5, height/2, width, height/2, arrow="last", tags=('grid', 'axe-x'))
        self.canvas.create_line(width/2, height-5, width/2, 5, arrow="last", tags=('grid', 'axe-y'))

        # dessin des lignes verticales
        for c in range(1,int(row/2)+1): 
            stepW=width/row
            xd=width/2+c*stepW 
            xg=width/2-c*stepW 
            #Creation des lignes verticales
            self.canvas.create_line(xd, height-5, xd, 5, dash=1, tags=('grid', 'vertical-line'), fill='grey') #cote droit
            self.canvas.create_line(xg, height-5, xg, 5, dash=1, tags=('grid', 'vertical-line'), fill='grey') #cote gauche
            #Creation des tirets sur x
            self.canvas.create_line(xd, height/2-4, xd, height/2+4, tags=('grid', 'horizontal-line'), fill='grey')
            self.canvas.create_line(xg, height/2-4, xg, height/2+4, tags=('grid', 'horizontal-line'), fill='grey')

        # dessin des lignes horizontales
        for r in range(1,int(col/2)+1): 
            stepH=height/col
            yB=height/2+r*stepH
            yH=height/2-r*stepH
            #Creation des lignes horizontales
            self.canvas.create_line(5, yB, width, yB, dash=1, tags=('grid', 'horizontal-line'), fill='grey')
            self.canvas.create_line(5, yH, width, yH, dash=1, tags=('grid', 'horizontal-line'), fill='grey')
            #Creation des tirets sur y
            self.canvas.create_line(width/2-4, yB, width/2+4, yB, tags=('grid', 'vertical-line'), fill='grey')
            self.canvas.create_line(width/2-4, yH, width/2+4, yH, tags=('grid', 'vertical-line'), fill='grey')

    def packing(self) :
        self.menu_bar.pack(fill='x')
        self.canvas.pack(side=LEFT,expand=1,fill="both",padx=6,pady=6)
        self.panelControl.pack(side=RIGHT,expand=1,fill="both",pady=6)
        self.frameLabelSignals.pack(expand=1,fill="both")
        self.frameLabelMode.pack(expand=1,fill="both")
        self.checkbox_signalX.pack(side=LEFT)
        self.checkbox_signalY.pack(side=LEFT)
        self.checkbox_XY.pack(side=RIGHT)
        self.frameControl.pack(side=RIGHT,expand=1,fill="both",pady=6)

