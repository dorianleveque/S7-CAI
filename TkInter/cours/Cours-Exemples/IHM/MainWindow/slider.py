from Tkinter import Tk,Scale,IntVar,DoubleVar

def update_magnitude(event):
    global data
    x=int(event.widget.get())   
    print(x,type(x))
    print(data.get(),data.get())

if __name__ == "__main__" :
    root = Tk()
    root.title("Oscilloscope v.1")
    data=DoubleVar()
    magnitude=Scale(root,variable=data,
                    length=250,orient="horizontal",
                    label="Magnitude",sliderlength=20,
                    showvalue=0,from_=0,to=5,tickinterval=25)
    magnitude.pack()
    magnitude.bind("<B2-Motion>",update_magnitude)
    root.mainloop()

