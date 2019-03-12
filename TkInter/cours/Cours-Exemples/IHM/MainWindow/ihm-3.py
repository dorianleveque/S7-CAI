import sys
if sys.version_info[0]< 3 :
    from Tkinter import Tk,Frame,Canvas,Label,Menu,Menubutton,Scrollbar
    import tkFileDialog
else :
    from tkinter import Tk,Frame,Canvas,Label,Menu,Menubutton,Scrollbar,filedialog

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
        self.canvas =Canvas(self, bg=bg)
        self.libelle =Label(text ="Serious Game", font="Helvetica 14 bold")
        print(self.canvas.cget("height"))
        print(self.canvas.cget("width"))
        print(self.canvas.winfo_height())
        print(self.canvas.winfo_width())

    def packing(self) :
        self.menubar.pack(fill="x")
        self.canvas.pack(fill="both",expand=True)
        self.libelle.pack()
        self.pack()

    def file_save(self) :
        formats=[('Texte','*.py'),
                ('Portable Network Graphics','*.png')]
        if sys.version_info[0]<3 :
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
    def create_circle(self) :
        pass
    def delete_circle(self) :
        pass
    def help_us(self) :
       pass
    def help_tkinter(self) :
        pass

if __name__ =="__main__":
    print(sys.version_info)
    root = Tk()
    root.title("Editeur Graphique")
    root.geometry("400x300+1200+300")
    mw = MainWindow(root)
    mw.packing()
    root.mainloop()

