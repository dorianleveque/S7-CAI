import sys
if sys.version_info[0]< 3 :
    from Tkinter import Tk,Frame,Canvas,Label,Menu,Menubutton,Scrollbar
    import tkFileDialog
else :
    from tkinter import Tk,Frame,Canvas,Label,Menu,Menubutton,Scrollbar,filedialog

from random import randrange
class ScrolledCanvas(Frame):
    def __init__(self,parent,
               width=100,height=100,bg="white",bd=2,
               scrollregion =(0,0,300,300)):
        Frame.__init__(self,parent)
        self.canvas=Canvas(self,width=width-20,
                        height=height-20,bg=bg,bd=bd,
                        scrollregion=scrollregion)
        self.canvas.grid(row=0,column=0)
        scv=Scrollbar(self,orient="vertical",
                    command =self.canvas.yview)
        sch=Scrollbar(self,orient="horizontal",
                    command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=sch.set,
                            yscrollcommand=scv.set)
        scv.grid(row=0,column=1,sticky="ns")
        sch.grid(row=1,column=0,sticky="ew")
        self.bind("<Configure>", self.resize)
        self.started =False

    def resize(self,event):
        """
        print("cget",event.widget.cget("width"))
        print("winfo",self.winfo_width()-20)
        
        if self.started:
            w=self.winfo_width()-20,
            h=self.winfo_height()-20
            self.canvas.configure(width=w,height=h)
        else :
            self.started=True
        """
        pass
    def get_canvas(self) :
        return self.canvas

class MenuBar(Frame):
  def __init__(self,parent=None):
    Frame.__init__(self, bg='green',borderwidth=2)
    file_button = Menubutton(self, text="File")
    file_button.pack(side="left")
    file_menu = Menu(file_button)
    file_button.configure(menu=file_menu)
 
    file_menu.add_command(label='Save', underline=0,
                          command=parent.file_save)
    # file_menu.add_command(label='Quit', underline=0,
    #                     command=parent.destroy)
    file_menu.add_command(label='Quit', underline=0,
                          command=parent.file_quit)
   
 
    edit_button = Menubutton(self, text="Edit")
    edit_button.pack(side="left")
    edit_menu = Menu(edit_button)
    edit_button.configure(menu=edit_menu)

    edit_menu.add_command(label='Hide', underline=0,
                        command=parent.delete_circle)
    edit_menu.add_command(label='Show', underline=0,
                        command=parent.create_circle)
  
    help_button = Menubutton(self, text="Help")
    help_button.pack(side="right")
    help_menu = Menu(help_button)
    help_button.configure(menu=help_menu)
 
    help_menu.add_command(label='About Us', underline=0,
                        command=parent.help_us)
    help_menu.add_command(label='About TkInter', underline=0,
                        command=parent.help_tkinter)
  

class MainWindow(Frame):
    def __init__(self, parent=None,bg="red"):
        Frame.__init__(self,parent, relief="sunken", bd=5)
        self.parent=parent
        self.menubar = MenuBar(self)
#        self.canvas =Canvas(self, bg=bg)
        self.area=ScrolledCanvas(self,
                         width=500,height=300,
                         scrollregion=(-600,-600,600,600))
        self.libelle =Label(text ="Serious Game", font="Helvetica 14 bold")
        print(self.area.cget("height"))
        print(self.area.cget("width"))
        print(self.area.winfo_height())
        print(self.area.winfo_width())
        self.x,self.y=100,100
        self.circle_bb=20
        self.circle=self.create_circle()
        self.animation_id=None

    def create_circle(self):
        print("create_circle(self)")
        canvas=self.area.get_canvas()
        id_circle=canvas.create_oval(self.x,self.y,
                                self.x+self.circle_bb,
                                self.y+self.circle_bb,
                                fill="yellow",
                                outline="black")
        return id_circle

    def animation(self):
        self.x += randrange(-60, 61)
        self.y += randrange(-60, 61)
        canvas=self.area.get_canvas()
        canvas.coords(self.circle,
                    self.x,
                    self.y,
                    self.x+self.circle_bb,
                    self.y+self.circle_bb)
        self.libelle.config(text="Cherchez en %s %s" \
                                % (self.x, self.y))
        self.animation_id=self.after(250, self.animation)

    def packing(self) :
        self.menubar.pack(fill="x")
        self.area.pack(fill="both",expand=True)
        self.libelle.pack()
        self.pack()

    def file_save(self) :
        formats=[('Texte','*.py'),
                ('Portable Network Graphics','*.png')]
        if sys.version_info[0]< 3 :
            filename= tkFileDialog.asksaveasfilename(parent=self.parent,
                                        filetypes=formats,
                                        title="Save...")
        else :
            filename= filedialog.asksaveasfilename(parent=self.parent,
                                        filetypes=formats,
                                        title="Save...")
        if len(nfilename) > 0:
            print("Sauvegarde en cours dans %s" % filename)

    def file_quit(self) :
        exit(0)
    def delete_circle(self) :
        pass
    def help_us(self) :
        self.animation()
    def help_tkinter(self) :
        self.after_cancel(self.animation_id)

if __name__ =="__main__":
    print(sys.version_info)
    root = Tk()
    root.title("Editeur Graphique")
    root.geometry("400x300+1200+300")
    mw = MainWindow(root)
    mw.packing()
    root.mainloop()

