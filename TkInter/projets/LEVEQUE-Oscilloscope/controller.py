class Controller :
    def __init__(self, parent, view):
        self.parent=parent
        self.view=view
        
        # attribution des comportements
        for pageControl in self.view.get_panel_control_page():
            pageControl['magnitude'].bind("<B1-Motion>",self.update_magnitude)
            pageControl['frequency'].bind("<B1-Motion>",self.update_frequency)
            pageControl['phase'].bind("<B1-Motion>",self.update_phase)

        self.view.get_canvas().bind("<Configure>", self.resize)
        self.view.get_checkbox_signalX().bind("<B1>", )
        
        
        # initialisation de la vue par le modele
        self.update_controls()


    def update_controls(self):
        models = self.parent.get_models()
        for index, model in enumerate(models):
            self.view.get_magnitude(index).set(model.get_magnitude())
            self.view.get_frequency(index).set(model.get_frequency())
            self.view.get_phase(index).set(model.get_phase())


    def update_magnitude(self,event):
        print("update_magnitude")
        x=int(event.widget.get())
        pageIndex = self.view.get_panel_control_index()
        model = self.parent.get_model(pageIndex)
        model.set_magnitude(x)
        model.generate_signal()

    def update_frequency(self, event):
        print("update_frequency")
        x=int(event.widget.get())
        pageIndex = self.view.get_panel_control_index()
        model = self.parent.get_model(pageIndex)
        model.set_frequency(x)
        model.generate_signal()

    def update_phase(self, event):
        print("update_phase")
        x=int(event.widget.get())
        pageIndex = self.view.get_panel_control_index()
        model = self.parent.get_model(pageIndex)
        model.set_phase(x)
        model.generate_signal()
         
    def resize(self, event):
        """
        En cas de reconfiguration de fenetre
        """
        models = self.parent.get_models()
        self.view.update(models)