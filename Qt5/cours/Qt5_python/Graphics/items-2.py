import sys
from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import QApplication,QWidget,QGraphicsScene,QGraphicsView,QGraphicsItem

# http://www.gchagnon.fr/cours/python/pyqt.html

app=QApplication(sys.argv)
scene=QGraphicsScene()
rect=scene.addRect(QtCore.QRectF(0, 0, 100, 100))
rect.setFlag(QGraphicsItem.ItemIsMovable)
view=QGraphicsView(scene)
view.resize(500,300)
view.move(500, 500)
view.show()
sys.exit(app.exec_())
