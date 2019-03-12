class Controller :
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.view.get_magnitude().bind("<B2-Motion>",self.update_magnitude)
    def update_magnitude(self,event):
        print("update_magnitude")
        x=int(event.widget.get())
        self.model.set_magnitude(x)
        self.model.generate_signal()
