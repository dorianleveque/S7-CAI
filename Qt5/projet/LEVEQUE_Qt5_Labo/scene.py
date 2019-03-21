#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore,QtCore,QtGui,QtWidgets
from PyQt5.QtCore import QT_VERSION_STR

class Scene (QtWidgets.QGraphicsScene) :
    def __init__(self,parent=None) :
        QtWidgets.QGraphicsScene.__init__(self)
        self.parent = parent
        self.tool = 'pointer'
        self.begin,self.end,self.offset=QtCore.QPoint(0,0),QtCore.QPoint(0,0),QtCore.QPoint(0,0)
        self.item_maintained = None
        self.item_shape = None
        self.mouse_pressed = False
        self.ctrl_key_pressed = False
        self.shift_key_pressed = False

        # pen init
        self.pen = QtGui.QPen()
        self.pen.setColor(QtCore.Qt.red)
        self.pen.setWidth(3)
        # brush init
        self.brush = QtGui.QBrush(QtCore.Qt.green)
        self.brush.setColor(QtCore.Qt.blue)
        #rect = QtWidgets.QGraphicsRectItem(0,0,100,100)
        #rect.setPen(self.pen)
        #rect.setBrush(self.brush)
        #self.setBackgroundBrush(QtGui.QColor(255, 255, 50, 127))
        #self.addItem(rect)
        
    def set_tool(self,tool) :
        print("set_tool(self,tool)",tool)
        self.tool=tool
        self.item_maintained = None

    def set_pen_color(self,color) :
        self.pen.setColor(color)

    def set_brush_color(self,color) :
       print("set_brush_color(self,color)",color)
       self.color_brush=color
 
    
    
    # ------ EVENTS -----------------------------

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Shift:
            self.shift_key_pressed = True
        elif event.key() == QtCore.Qt.Key_Control:
            self.ctrl_key_pressed = True

    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Shift:
            self.shift_key_pressed = False
        elif event.key() == QtCore.Qt.Key_Control:
            self.ctrl_key_pressed = False

    def contextMenuEvent(self, event):
        self.parent.menu_style_pen.exec(QtGui.QCursor.pos())

    def mousePressEvent(self, event):
        print("Scene.mousePressEvent()")
        self.begin = self.end = event.scenePos()
        self.item_maintained = self.itemAt(self.begin,QtGui.QTransform())
        if self.item_maintained :
            if self.tool == 'pointer':
                self.offset = self.begin - self.item_maintained.pos()
            elif self.tool == 'eraser':
                self.removeItem(self.item_maintained)


        self.mouse_pressed = True
        self.item_shape = None
                
    def mouseMoveEvent(self, event):
        pen_shape = QtGui.QPen()
        pen_shape.setColor(QtGui.QColor(0, 0, 0, 150))
        pen_shape.setWidth(2)
        pen_shape.setStyle(QtCore.Qt.DashLine)

        brush_shape = QtGui.QBrush()
        brush_shape.setColor(QtGui.QColor(0, 0, 0, 120))

        self.end = event.scenePos()

        if self.tool == "pointer":
            if self.item_maintained:
                self.item_maintained.setPos(event.scenePos() - self.offset)

        elif self.tool == "line" and self.mouse_pressed:
            if not self.item_shape:
                self.item_shape = self.addLine(self.begin.x(), self.begin.y(), self.end.x(), self.end.y(), pen_shape)
            self.item_shape.setLine(self.begin.x(), self.begin.y(), self.end.x(), self.end.y())

        elif self.tool == "rect" and self.mouse_pressed:
            x, y = self.begin.x(), self.begin.y()
            w = self.end.x()-self.begin.x()
            h = self.end.y()-self.begin.y()
            
            if self.shift_key_pressed:
                h = w if (bool(w > 0) == bool(h > 0)) else -w

            if not self.item_shape:
                self.item_shape = self.addRect(x, y, w, h, pen_shape, brush_shape)
            self.item_shape.setRect(x, y, w, h)

        elif self.tool == "elli" and self.mouse_pressed:
            x, y = self.begin.x(), self.begin.y()
            w = self.end.x()-self.begin.x()
            h = self.end.y()-self.begin.y()

            if self.shift_key_pressed:
                h = w if (bool(w > 0) == bool(h > 0)) else -w

            if not self.item_shape:
                self.item_shape = self.addEllipse(x, y, w, h, pen_shape, brush_shape)
            self.item_shape.setRect(x, y, w, h)

        self.update()

    def mouseReleaseEvent(self, event):
        print("Scene.mouseReleaseEvent()",self.tool)
        self.end = event.scenePos()
        self.mouse_pressed = False
        if self.tool == "pointer":
            print(" item_maintained ")
            if self.item_maintained :
                self.item_maintained.setPos(event.scenePos() - self.offset)
                self.item_maintained=None
        
        elif self.tool == 'line' :
            self.item_shape.setPen(self.pen)
            self.item_shape = None
        elif self.tool == 'rect' or self.tool == 'elli' :
            self.item_shape.setPen(self.pen)
            self.item_shape.setBrush(self.brush)
            self.item_shape = None
        else :
            print("no item_maintained selected and nothing to draw !")
        