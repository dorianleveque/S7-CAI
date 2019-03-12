from Tkinter import Tk, Frame, Canvas, Scrollbar, Label, Button, Scale, Menu, Menubutton
from random import randrange

class ScrolledCanvas(Frame):
    """Zone Client"""
    def __init__(self,parent=None,bg="white",bd=2,
                 scrollregion=(0, 0, 300, 300),relief="sunken"):
        Frame.__init__(self,parent,bd=bd,relief=relief)
        self.parent=parent
        self.canvas=Canvas(self,bg=bg,bd=1,scrollregion=scrollregion)
        scv = Scrollbar(self, orient="vertical", command=self.canvas.yview, bd=1)
        sch = Scrollbar(self, orient="horizontal", command=self.canvas.xview, bd=1)
        self.canvas.configure(xscrollcommand=sch.set, yscrollcommand=scv.set)
        self.canvas.grid(row=0, column=0)
        scv.grid(row=0, column=1, sticky="ns")
        sch.grid(row=1, column=0, sticky="ew")
        self.config = False
        self.bind("<Configure>", self.resize)
 
    def get_canvas(self):
        return self.canvas

    def resize(self, event):
        if self.config:
            self.width,self.height=self.winfo_width(), self.winfo_height()
            self.canvas.config(width=self.width-20, height=self.height-20)
        else :
            self.config=True

class MenuBar(Frame):
    """Barre de menus"""
    def __init__(self,master=None):
        Frame.__init__(self, borderwidth=2)
        self.master=master
        button_file=Menubutton(self,text="Fichier",bg="white")
        button_file.pack(side="left")
        menu_file=Menu(button_file)
        menu_file.add_command(label='Effacer', underline=0,
                        command=self.master.delete_circle)
        menu_file.add_command(label='Afficher', underline=0,
                        command=self.master.create_circle)
        menu_file.add_command(label='Terminer', underline=0,
                        command=self.master.quit)
        button_file.configure(menu=menu_file)

class MainWindow(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.parent=parent
        menubar=MenuBar(self)
        self.area=self.create_area()
        self.button_start,self.scale_circle=self.create_controls()
        self.libelle=Label(text="Serious Game", font="Helvetica 14 bold",bg="white",fg="red")
        menubar.pack()
        self.area.pack()
        self.libelle.pack(pady=3)
        
        self.x,self.y=100,100
        self.circle_bb=100
        self.circle=None
        self.animation_id=None

    def create_area(self) :
        canvas=ScrolledCanvas(self,relief="solid",scrollregion=(-600, -600, 600, 600), bd=3)
        return canvas

    def create_controls(self) :
        canvas=self.area.get_canvas()
        start = Button(self, text="Start", command=self.start)
        scale = Scale(self, length=250, orient="horizontal",
                                 label='Rayon :', troughcolor='dark grey', sliderlength=20,
                                 showvalue=0, from_=0, to=100, tickinterval=25,
                                 command=self.update_circle)
        scale.set(50)
        canvas.create_window(50, 200, window=start)
        canvas.create_window(250,200,window=scale)
        return start,scale
       
    def create_circle(self):
        canvas=self.area.get_canvas()
        if self.circle != None :
            canvas.delete(self.circle)
        self.circle=canvas.create_oval(self.x, self.y,
                                  self.x+self.circle_bb, self.y+self.circle_bb,
                                  fill='yellow', outline='black')
        return self.circle
        
    def delete_circle(self):
        if self.circle != None :
            canvas=self.area.get_canvas()
            canvas.delete(self.circle)
  
    def update_circle(self, size):
        canvas=self.area.get_canvas()
        canvas.delete(self.circle)
        self.circle_bb=2*int(size)
        self.circle=self.create_circle()

    def animation(self):
        self.x += randrange(-60, 61)
        self.y += randrange(-60, 61)
        canvas=self.area.get_canvas()
        canvas.coords(self.circle, self.x, self.y, self.x+self.circle_bb, self.y+self.circle_bb)
        self.libelle.config(text='Cherchez en %s %s' % (self.x, self.y))
        self.animation_id = self.after(250, self.animation)

    def stop(self):
        self.after_cancel(self.animation_id)
        self.button_start.configure(text="Start", command=self.start)

    def start(self):
        self.button_start.configure(text="Stop", command=self.stop)
        self.animation()

    def stop(self):
        self.parent.destroy()

if __name__ == "__main__":
    root = Tk()
    root.title("Editeur Graphique")
    mw = MainWindow(root)
    mw.pack(expand=1,fill="both",padx=3,pady=6)
    root.mainloop()
