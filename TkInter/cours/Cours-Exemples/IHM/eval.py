#-------- 1) Initialisation ---------------------------
from Tkinter import Tk,Entry,Label
from math import *
#-------- 2) Composants graphiques --------------------
mw = Tk()
mw.title("Eval")
entry = Entry(mw)
label = Label(mw)
#-------- 3) Positionnement des composants ------------
entry.pack()
label.pack()
#-------- 4) Definition des interactions --------------
def evaluer(event):
    label.configure(text = "Resultat = " + str(eval(entry.get())))
#-------- 5) Gestion des evenements  ------------------
entry.bind("<Return>", evaluer)
mw.mainloop()
exit(0)
