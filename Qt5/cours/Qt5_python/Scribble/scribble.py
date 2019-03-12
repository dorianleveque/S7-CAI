import sys
from PyQt5 import QtCore,QtGui,QtWidgets,QtSvg

class Scribble(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.polygon= QtGui.QPolygon()
        self.start,self.end=QtCore.QPoint(0,0),QtCore.QPoint(0,0)
        self.pen_color=QtCore.Qt.blue;
        self.pen_width=3;
    def mousePressEvent(self,event) :
        print("ScribbleArea.mousePressEvent(event)")
        if event.button() == QtCore.Qt.LeftButton :
            self.start = self.end = event.pos();

    def mouseMoveEvent(self,event) :
        print("ScribbleArea.mouseMoveEvent(event)")
        if event.buttons() & QtCore.Qt.LeftButton :
            self.end = event.pos();
        self.update()
   
    def mouseReleaseEvent(self,event) :
        print("ScribbleArea.mouseReleaseEvent(event)")
        if  event.button()== QtCore.Qt.LeftButton :
            self.update()

    def paintEvent(self,event) :
    #    print("ScribbleArea.paintEvent(event)")
        painter=QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(self.pen_color,self.pen_width,
                        QtCore.Qt.SolidLine, QtCore.Qt.RoundCap,QtCore.Qt.RoundJoin))
        painter.drawLine(self.start,self.end);
        self.update()

    def resizeEvent(self,event) :
        print("ScribbleArea.resizeEvent(event)")
        print(self.width(),self.height())
  
    #  def paintEvent(self, event):
    #     painter = QtGui.QPainter(self)
    #     pen = QtGui.QPen(QtCore.Qt.red)
    #     pen.setWidth(5)
    #     painter.setPen(pen)
    #     brush = QtGui.QBrush(QtCore.Qt.lightGray)
    #     painter.setBrush(brush)
    #     painter.drawRect(5,5,120,40)
    #     return


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = Scribble()
    # mw = QtWidgets.QMainWindow()
    # mw.setCentralWidget(Scribble())
    mw.resize(300,200)
    mw.show()
    app.exec_()

