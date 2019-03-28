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
        self.font = self.font()
        self.__scene_changed = False
        self.begin,self.end,self.offset=QtCore.QPoint(0,0),QtCore.QPoint(0,0),QtCore.QPoint(0,0)
        self.item_maintained = None
        self.item_shape = None
        self.mouse_pressed = False
        self.ctrl_key_pressed = False
        self.shift_key_pressed = False

        self.poly_painter_shape_points = []
        self.poly_painter = None
        self.poly_shape = False

        # pen init
        self.pen = QtGui.QPen()
        self.pen.setColor(QtCore.Qt.red)
        self.pen.setWidth(2)
        ## brush init
        self.brush = QtGui.QBrush(QtCore.Qt.blue)

        self.pen_shape = QtGui.QPen(QtGui.QColor(0, 0, 0, 150))
        self.pen_shape.setWidth(2)
        self.pen_shape.setStyle(QtCore.Qt.DashLine)

        self.brush_shape = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        
    def sceneChanged(self):
        return self.__scene_changed

    def setSceneChanged(self, s):
        self.__scene_changed = s

    def set_tool(self,tool) :
        self.tool=tool
        self.item_maintained = None
        if isinstance(self.item_shape, QtWidgets.QGraphicsPathItem):
            self.removeItem(self.item_shape)
        self.item_shape = None

    def set_pen_color(self,color) :
        self.pen.setColor(color)

    def set_pen_line_style(self, style):
        self.pen.setStyle(style)

    def get_pen_width(self):
        return self.pen.width()

    def set_pen_width(self, width):
        self.pen.setWidth(width)

    def set_font(self, font):
        self.font = font

    def get_font(self):
        return self.font

    def set_brush_color(self,color) :
       self.brush.setColor(color)
 
    def set_brush_style(self, style):
        self.brush.setStyle(style)
    
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
        self.parent.menu_style.exec(QtGui.QCursor.pos())

    def mousePressEvent(self, event):
        self.begin = self.end = event.scenePos()
        self.item_maintained = self.itemAt(self.begin,QtGui.QTransform())

        if self.tool == 'pointer' and self.item_maintained:
            self.offset = self.begin - self.item_maintained.pos()
        elif self.tool == 'eraser' and self.item_maintained:
            self.removeItem(self.item_maintained)
        elif self.tool == "line":
            if not self.item_shape:
                self.item_shape = self.addLine(self.begin.x(), self.begin.y(), self.end.x(), self.end.y(), self.pen_shape)
        elif self.tool == "rect":
            x, y = self.begin.x(), self.begin.y()
            if not self.item_shape:
                self.item_shape = self.addRect(x, y, 0, 0, self.pen_shape, self.brush_shape)
        elif self.tool == "elli":
            x, y = self.begin.x(), self.begin.y()
            if not self.item_shape:
                self.item_shape = self.addEllipse(x, y, 0, 0, self.pen_shape, self.brush_shape)
        elif self.tool == "text":
            pass
        self.mouse_pressed = True
        
    
    def mouseMoveEvent(self, event):
        self.end = event.scenePos()

        if self.tool == "pointer" and self.item_maintained:
            self.item_maintained.setPos(event.scenePos() - self.offset)

        elif self.tool == "line" and self.mouse_pressed:
            if self.item_shape:
                self.item_shape.setLine(self.begin.x(), self.begin.y(), self.end.x(), self.end.y())

        elif self.tool == "rect" and self.mouse_pressed:
            x, y = self.begin.x(), self.begin.y()
            w = self.end.x()-self.begin.x()
            h = self.end.y()-self.begin.y()
            
            if self.shift_key_pressed:
                h = w if (bool(w > 0) == bool(h > 0)) else -w

            if self.item_shape:
                self.item_shape.setRect(x, y, w, h)

        elif self.tool == "elli" and self.mouse_pressed:
            x, y = self.begin.x(), self.begin.y()
            w = self.end.x()-self.begin.x()
            h = self.end.y()-self.begin.y()

            if self.shift_key_pressed:
                h = w if (bool(w > 0) == bool(h > 0)) else -w

            if self.item_shape:
                self.item_shape.setRect(x, y, w, h)

        elif self.tool == "poly":
            if self.poly_shape and self.item_shape:
                self.poly_painter.setElementPositionAt(self.poly_painter.elementCount()-1, self.end.x(), self.end.y())
                self.item_shape.setPath(self.poly_painter)
                
        self.update()
        

    def mouseReleaseEvent(self, event):
        self.end = event.scenePos()
        self.mouse_pressed = False
        if self.tool == "pointer":
            if self.item_maintained :
                self.item_maintained.setPos(event.scenePos() - self.offset)
                self.item_maintained = None
                self.__scene_changed = True
        
        elif self.tool == 'line' :
            self.item_shape.setPen(self.pen)
            self.item_shape = None
            self.__scene_changed = True

        elif self.tool == 'rect' or self.tool == 'elli' :
            self.item_shape.setPen(self.pen)
            self.item_shape.setBrush(self.brush)
            self.item_shape = None
            self.__scene_changed = True

        elif self.tool == 'poly':
            if not self.item_shape:
                self.poly_shape = True
                self.poly_painter = QtGui.QPainterPath(QtCore.QPointF(self.end.x(), self.end.y()))
                self.item_shape = self.addPath(self.poly_painter, self.pen_shape, self.brush_shape)

            if self.poly_painter.elementCount() > 2:
                x0  = self.poly_painter.elementAt(0).x
                y0  = self.poly_painter.elementAt(0).y
                x   = self.poly_painter.elementAt(self.poly_painter.elementCount()-1).x
                y   = self.poly_painter.elementAt(self.poly_painter.elementCount()-1).y
                #if self.poly_painter.contains(QtCore.QPointF(x,y)):
                if (x0 > (x-10) and x0 < (x+10) and y0 > (y-10) and y < (y+10)):
                    self.poly_shape = False
                    self.poly_painter.setElementPositionAt(self.poly_painter.elementCount()-1, x0, y0)
                    self.item_shape.setPath(self.poly_painter)

                    points = []
                    for i in range(self.poly_painter.elementCount()):
                        point = self.poly_painter.elementAt(i)
                        points.append(QtCore.QPointF(point.x, point.y))
                    polygon = QtGui.QPolygonF(points)
                    self.removeItem(self.item_shape)
                    self.addPolygon(polygon, self.pen, self.brush)
                    self.item_shape = None
                    self.__scene_changed = True
                else:
                    self.poly_painter.lineTo(self.end.x()+1, self.end.y()+1)
                    self.item_shape.setPath(self.poly_painter)
            else:
                self.poly_painter.lineTo(self.end.x()+1, self.end.y()+1)
                self.item_shape.setPath(self.poly_painter)
           
        elif self.tool == "text":
            text, ok = QtWidgets.QInputDialog.getText(QtWidgets.QWidget(), "Insert text", "text", flags=QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
            if ok:
                text = QtWidgets.QGraphicsTextItem(text)
                text.setPos(self.end.x(), self.end.y())
                text.setFont(self.font)
                self.addItem(text)
        
        else :
            print("no item_maintained selected and nothing to draw !")
        self.update()