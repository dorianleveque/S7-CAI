import sys
from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QGraphicsProxyWidget
from PyQt5.QtWidgets import QGraphicsScene,QGraphicsView,QGraphicsItem

app=QApplication(sys.argv)
scene=QGraphicsScene()
rect=scene.addRect(QtCore.QRectF(0, 0, 100, 100))
rect.setFlag(QGraphicsItem.ItemIsMovable)
button = QPushButton("Un bouton")
proxy = QGraphicsProxyWidget()
proxy.setWidget(button)
scene.addItem(proxy)
scene.setSceneRect(0, 0, 300, 300);

matrix=QtGui.QTransform()
matrix.rotate(45)
matrix.translate(100, 0)
matrix.scale(1,2);
proxy.setTransform(matrix)

# print("proxy->x() : ",proxy->x())
# print("proxy->y() : ",proxy->y())
# proxy.setTransform(matrix);


view=QGraphicsView(scene)
#view.resize(500,300)
#view.move(500, 500)
view.show()
sys.exit(app.exec_())
