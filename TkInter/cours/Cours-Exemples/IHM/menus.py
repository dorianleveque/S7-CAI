from Tkinter import Tk,Menu,Frame
def hello():
    print "hello!"
root = Tk()
menubar = Menu(root)
menubar.add_command(label="Hello!", command=hello)
menubar.add_command(label="Quit!", command=root.quit)
root.config(menu=menubar)
root.mainloop()

##menubar = Menu(root)
##
### create a pulldown menu, and add it to the menu bar
##filemenu = Menu(menubar, tearoff=0)
##filemenu.add_command(label="Open", command=hello)
##filemenu.add_command(label="Save", command=hello)
##filemenu.add_separator()
##filemenu.add_command(label="Exit", command=root.quit)
##menubar.add_cascade(label="File", menu=filemenu)
##
### create more pulldown menus
##editmenu = Menu(menubar, tearoff=0)
##editmenu.add_command(label="Cut", command=hello)
##editmenu.add_command(label="Copy", command=hello)
##editmenu.add_command(label="Paste", command=hello)
##menubar.add_cascade(label="Edit", menu=editmenu)
##
##helpmenu = Menu(menubar, tearoff=0)
##helpmenu.add_command(label="About", command=hello)
##menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
##menu = Menu(root, tearoff=0)
##menu.add_command(label="Undo", command=hello)
##menu.add_command(label="Redo", command=hello)
##frame = Frame(root, width=512, height=512)
##frame.pack()
####
##def popup(event):
##    menu.post(event.x_root, event.y_root)
##frame.bind("<Button-3>", popup)
