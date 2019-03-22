import os,sys
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtCore import QT_VERSION_STR

if __name__ == "__main__" :
    print(QT_VERSION_STR)
    app=QtWidgets.QApplication(sys.argv)
    view=QtWidgets.QGraphicsView()
    scene=QtWidgets.QGraphicsScene()
#    view.setGeometry(500,200,1000,600)
    print(view.width()) 
    print(view.rect())
    print(view.size())
    print(view.sceneRect())
    w=view.width() 
    h=view.height()
    text=QtWidgets.QGraphicsTextItem("Translation en haut a gauche")
    transform=QtGui.QTransform()
    transform.translate(-w/2.0,-h/2.0)
    text.setTransform(transform)
    scene.addItem(text)
    pen=QtGui.QPen()
    pen.setColor(QtCore.Qt.green)
    pen.setWidth(5)
    line=QtWidgets.QGraphicsLineItem(-w/2.0,0,w/2.0,0)
    line.setPen(pen)
    scene.addItem(line)
    text=QtWidgets.QGraphicsTextItem("Rotation a + 45 degres autour de l'axe 0z")
#    text.setDefaultTextColor(pen.color())
    transform=QtGui.QTransform()
    transform.rotate(45)
    text.setTransform(transform)
    scene.addItem(text)
    pen.setColor(QtCore.Qt.red)
    pen.setWidth(5)
    line=QtWidgets.QGraphicsLineItem(0,-h/2.0,0,h/2.0)
    line.setPen(pen)
    scene.addItem(line)
    text=QtWidgets.QGraphicsTextItem("Rotation a -45 degres autour de l'axe 0z")
#    text.setDefaultTextColor(pen.color())
    transform=QtGui.QTransform()
    transform.rotate(-45)
    text.setTransform(transform)
    scene.addItem(text)
    view.setScene(scene)
    view.show()
    sys.exit(app.exec_())
