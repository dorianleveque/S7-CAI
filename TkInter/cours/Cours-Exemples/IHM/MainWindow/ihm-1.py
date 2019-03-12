from Tkinter import Tk,Canvas,Label

class MainWindow(Tk):
  def __init__(self, width=100,height=100,bg="red"):
    Tk.__init__(self)
    self.title("Editeur Graphique")
    self.geometry("400x300+1200+300")
    self.canvas =Canvas(self,width=width-20,
                        height=height-20, bg=bg)
    self.libelle =Label(text ="Serious Game",
                        font="Helvetica 14 bold")
    self.canvas.pack()
    self.libelle.pack()
    print(self.canvas.cget("height"))
    print(self.canvas.cget("width"))
    print(self.canvas.winfo_height())
    print(self.canvas.winfo_width())
if __name__ =="__main__":
    MainWindow().mainloop()
