from Tkinter import Tk,Label,Button
root=Tk()
root.option_readfile('hello.txt')
labelHello=Label(root, text="Hello World !")
labelBonjour=Label(root,name="labelBonjour")
labelHello.pack()
labelBonjour.pack()
buttonQuit=Button(root, text="Goodbye World", fg="red",command=root.destroy)
buttonQuit.pack()
root.mainloop()
exit(0)
