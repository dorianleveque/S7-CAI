## python 2.7
from Tkinter import Tk,Label,Canvas,Frame,Menu,Menubutton,Button,Scale,Scrollbar
import tkFileDialog

## python 3
##from tkinter import Tk,Label,Canvas,Frame,Menu,Menubutton,Button,Scale,Scrollbar,
##import filedialog


class MenuBar(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,borderwidth=2)
        button_file = Menubutton(self,text="File")
        menu_file=Menu(button_file)
        menu_file.add_command(label="New",command=parent.new)
        menu_file.add_command(label ="Save",command = parent.save)
        menu_file.add_command(label ="Exit",command = parent.exit)
        button_file.configure(menu=menu_file)
        button_file.pack()

class ScrolledCanvas(Frame):
    def __init__(self,parent,width=100,height=100,
                 bg="white",scrollregion =(0,0,300,300)):
        Frame.__init__(self,parent)
        self.canvas=Canvas(self,width=width-20,height=height-20,
                           bg=bg,scrollregion=scrollregion)
        self.canvas.grid(row=0,column=0)
        scv=Scrollbar(self,orient="vertical",command =self.canvas.yview)
        sch=Scrollbar(self,orient="horizontal",command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=sch.set,yscrollcommand=scv.set)
        scv.grid(row=0,column=1,sticky="ns")
        sch.grid(row=1,column=0,sticky="ew")
        self.bind("<Configure>", self.resize)
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
      
class MainWindow(Frame):
    def __init__(self,parent=None,width=200,height=100,bg="red"):
        Frame.__init__(self)
        self.parent=parent
        self.x,self.y=0,0
        menubar = MenuBar(self)
        self.canvas_game=ScrolledCanvas(self,width=width-20,height=height-20, bg=bg)
        self.libelle =Label(text ="Serious Game",
                            font="Helvetica 14 bold")
        menubar.pack()
        self.libelle.pack()
#        self.canvas_game.pack()
        self.canvas_game.pack(expand=1,fill="both",padx=6,pady=6)
        
    def new(self):
        pass
    def save(self):
        formats = [('Texte','*.py'),('Portable Network Graphics','*.png')]
        filename = tkFileDialog.asksaveasfilename(parent=self.parent,filetypes=formats,title="Sauvez l'image sous...")
#        filename = filedialog.asksaveasfilename(parent=self.parent,filetypes=formats,title="Sauvez l'image sous...")
        if len(filename) > 0:
          print("Sauvegarde en cours dans %s" % filename)

    def exit(self):
        self.parent.destroy()

if __name__ =="__main__":
    root = Tk()
    root.option_add('*tearOff', False)
    root.title("Editeur Graphique")
    mw = MainWindow(root)
#    mw.pack()
    mw.pack(expand=1,fill="both",padx=6,pady=6)
    root.mainloop()
