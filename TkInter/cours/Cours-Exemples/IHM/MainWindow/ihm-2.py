from Tkinter import Tk,Frame,Canvas,Label

class MainWindow(Frame):
    def __init__(self, parent=None, width=100,height=100,bg="red"):
        Frame.__init__(self,parent, relief="sunken", bd=5)
        self.canvas =Canvas(self,width=width-20,height=height-20, bg=bg)
        self.libelle =Label(text ="Serious Game", font="Helvetica 14 bold")
        print(self.canvas.cget("height"))
        print(self.canvas.cget("width"))
        print(self.canvas.winfo_height())
        print(self.canvas.winfo_width())

    def packing(self) :
        self.pack()
        self.canvas.pack(fill="both",expand=True)
        self.libelle.pack()

if __name__ =="__main__":
    root = Tk()
    root.title("Editeur Graphique")
    root.geometry("400x300+1200+300")
    mw = MainWindow(root)
    mw.packing()
    root.mainloop()

