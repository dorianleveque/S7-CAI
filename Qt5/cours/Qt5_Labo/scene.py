#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore,QtCore,QtGui,QtWidgets
from PyQt5.QtCore import QT_VERSION_STR

class Scene (QtWidgets.QGraphicsScene) :
    def __init__(self,parent=None) :
        QtWidgets.QGraphicsScene.__init__(self)
        self.tool='line'
        self.begin,self.end,self.offset=QtCore.QPoint(0,0),QtCore.QPoint(0,0),QtCore.QPoint(0,0)
        self.item=None
        self.pen=QtGui.QPen()
        self.pen.setColor(QtCore.Qt.red)
        self.pen.setWidth(3)
        self.brush=QtGui.QBrush(QtCore.Qt.green)
    #    self.brush.setColor(QtCore.Qt.green)
        rect=QtWidgets.QGraphicsRectItem(0,0,100,100)
        rect.setPen(self.pen)
        rect.setBrush(self.brush)
        self.addItem(rect)
        
    def set_tool(self,tool) :
        print("set_tool(self,tool)",tool)
        self.tool=tool

    def set_pen_color(self,color) :
        self.pen.setColor(color)

    def set_brush_color(self,color) :
       print("set_brush_color(self,color)",color)
       self.color_brush=color
 
    def mousePressEvent(self, event):
        print("Scene.mousePressEvent()")
        self.begin = self.end = event.scenePos()
        self.item=self.itemAt(self.begin,QtGui.QTransform())
        if self. item :
            self.offset =self.begin-self.item.pos()
                
    def mouseMoveEvent(self, event):
        # print("Scene.mouseMoveEvent()")
        if self.item :
            self.item.setPos(event.scenePos() - self.offset)
        self.end = event.scenePos()
 
    def mouseReleaseEvent(self, event):
        print("Scene.mouseReleaseEvent()",self.tool)
        self.end = event.scenePos()
        if self.item :
            print(" item ")
            self.item.setPos(event.scenePos() - self.offset)
#            self.item.ungrabMouse()
            self.item=None
        elif self.tool=='line' :
            self.addLine(self.begin.x(), self.begin.y(),self.end.x(), self.end.y(),self.pen)
        else :
            print("no item selected and nothing to draw !")
