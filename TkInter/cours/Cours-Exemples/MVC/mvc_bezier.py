# -*- coding: utf-8 -*-
from Tkinter import Tk,Canvas
from copy import copy
import time

##def draw_line(p1,p2) :
##    up()
##    x,y=p1
##    goto(x,y)
##    down()
##    x,y=p2
##    goto(x,y)
##
##def draw_circle(center,radius=10) :
##    x,y=center
##    up()
##    goto(x,y-radius/2.0)
##    down()
##    circle(radius/2.0)
##
##def plot_point(p,size=2,color="red") :
##    x,y=p
##    up()
##    goto(x,y)
##    down()
##    dot(size,color)

##def bezier_draw_curve(points) :
##    for point in points :
##        plot_point(point)
##    return points


class Subject(object):
    def __init__(self):
        self.observers=[]
    def notify(self):
        for obs in self.observers:
            obs.update(self)
    def attach(self, obs):
        if not hasattr(obs,"update"):
            raise ValueError("Observer must have an update() method")
        self.observers.append(obs)
    def detach(self, obs):
        if obs in self.observers :
            self.observers.remove(obs)

class Bezier(Subject):
    def __init__(self,points=[]):
        Subject.__init__(self)
        self.control_points=copy(points)
        print(self.control_points)
        self.curve=[]

    def set_control_points(self,points) :
        self.control_points=copy(points)
        self.notify()
    def get_control_points(self) :
        return self.control_points
    def set_curve(self,curve) :
        self.curve=copy(curve)
        self.notify()
    def get_curve(self) :
        return self.curve

    def compute_point(self,points,t):
        if len(points)==1:
            return points[0]
        else:
            casteljau_points=[]
            for i in range(0,len(points)-1):
                x=(1-t)*points[i][0]+t*points[i+1][0]
                y=(1-t)*points[i][1]+t*points[i+1][1]
                casteljau_points.append((x, y))
            return self.compute_point(casteljau_points,t)

    def compute_curve(self,step=0.01) :
        t=0
        del self.curve[:]
        while (t<=1):
            self.curve.append(self.compute_point(self.control_points,t))
            t+=step
        self.notify()
        return self.curve

# observers  :  update (state of the Model has  changed)
class Observer:
    def update(self, subject):
        raise NotImplementedError

class Screen(Observer) :
    def __init__(self,parent,model):
        self.parent=parent
        self.model=model
        self.canvas=Canvas(parent)
        self.curve_id=-1
        self.control_points_id=[]
        self.control_point_index=-1
    def set_canvas(self,canvas) :
        self.canvas=canvas
    def get_canvas(self) :
        return self.canvas
    
# View : update() the Bezier curve
    def update(self, subject):
        curve=subject.get_curve()
        self.canvas.delete(self.curve_id)
        self.curve_id=self.canvas.create_line(curve,width=3,fill='gray40')

# View : control points visualisation 
    def update_control_points(self, model):
        control_points=model.get_control_points()
#        self.canvas.delete('ctrl_pts')
        del self.control_points_id[:]
        i=0
        while i < len(control_points):
            x,y=control_points[i]
            self.control_points_id.append(self.canvas.create_oval(x,y, x+10,y+10, outline='black', fill='green'))
            i=i+1

# Controler :  control point interaction to update the Bezier curve
    def select_point(self,event,model) :
        control_points=model.get_control_points()
        # selection of a control point
        i=0
        while i < len(control_points) :
                x,y=control_points[i]
                if x-10< event.x < x+10 and  y-10 < event.y < y+10:
                    self.control_point_index=i
                    self.canvas.itemconfigure(self.control_points_id[self.control_point_index],fill='red')
                    break
                i=i+1
        # insertion of a control point
        if self.control_point_index==-1 :
            i=0
            while i < len(control_points)-1 :
                x1,y1=control_points[i]
                x2,y2=control_points[i+1]
                print(event.x,event.y)
                if (x1 < event.x < x2  or x2 < event.x < x1) and  (y1 < event.y < y2  or y2 < event.y < y1):
                    control_points.insert(i,(event.x,event.y))
                    model.set_control_points(control_points)
                    self.update_control_points(model)
                    break
                i=i+1
            self.update_control_points(model)
            
    def move_point(self,event,model) :
        if 0 <= self.control_point_index < len(self.control_points_id):
                coords=self.canvas.coords(self.control_points_id[self.control_point_index])
                x1,y1=coords[0],coords[1]
                x1,y1=event.x-x1,event.y-y1
                control_points=model.get_control_points()
                control_points[self.control_point_index]=event.x,event.y
                model.set_control_points(control_points)
                self.canvas.move(self.control_points_id[self.control_point_index], x1, y1)
                model.compute_curve()
    def release_point(self,event) :
            self.canvas.itemconfigure(self.control_points_id[self.control_point_index],fill='green')
            self.control_point_index=-1

    def packing(self) :
        self.canvas.pack(fill='both', expand=True)

if __name__ == "__main__" :
    root=Tk()
    root.title("Courbes de Bézier")
##    control_points=[(50,200),(100,100),(150,50),(200,100),(250,200)]
    control_points=[(50,200),(100,100),(150,300),(200,100),(250,200)]
##    control_points=[(-400,-300),(-400,100),(-50,400),(350,250),(450,-100)]
    bezier=Bezier(control_points)
    bezier.compute_curve()
    screen=Screen(root,bezier)
    bezier.attach(screen)
    bezier.notify()    
    screen.update_control_points(bezier)
    screen.packing()
    canvas=screen.get_canvas()
    canvas.configure(bg="white")

##    canvas.bind("<Button-1>", screen.select_point)
##    canvas.bind("<Motion>",screen.move_point)
##    canvas.bind("<ButtonRelease>",screen.release_point)
    canvas.bind("<Button-1>",lambda event,model=bezier :
                screen.select_point(event,model))
    canvas.bind("<Motion>",lambda event,model=bezier : screen.move_point(event,model))
    canvas.bind("<ButtonRelease>",screen.release_point)

##    scr=Screen(root,bezier)
##    scr.packing()
##    bezier.attach(scr)
##    scr.update_control_points(bezier)
##    bezier.notify()    

    root.mainloop()
