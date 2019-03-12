import sys
from PyQt5 import QtCore,QtGui,QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = QtWidgets.QGraphicsView()
    view.setGeometry(QtCore.QRect(0, 0, 600, 500))
    scene=QtWidgets.QGraphicsScene()
    scene.setSceneRect(-150, -150, 300, 300)

    top_line = QtCore.QLineF(scene.sceneRect().topLeft(),scene.sceneRect().topRight())
    left_line = QtCore.QLineF(scene.sceneRect().topLeft(),scene.sceneRect().bottomLeft())
    right_line=QtCore.QLineF(scene.sceneRect().topRight(), scene.sceneRect().bottomRight())
    bottom_line=QtCore.QLineF(scene.sceneRect().bottomLeft(), scene.sceneRect().bottomRight())

    pen = QtGui.QPen(QtCore.Qt.red)
    
    scene.addLine(top_line, pen)
    scene.addLine(left_line, pen)
    scene.addLine(right_line, pen)
    scene.addLine(bottom_line, pen)

    #   scene.setSceneRect(QtCore.QRectF())
    #   scene.setSceneRect(QtCore.QRectF(0, 0, 300, 300))
    #   setSceneRect(self.sceneRect())
    view.setScene(scene)
    item = QtWidgets.QGraphicsEllipseItem(0,0, 50, 50)
    scene.addItem(item)
    item = QtWidgets.QGraphicsRectItem(-100,-100, 50, 50)
    scene.addItem(item)

    # for i in range(5):
    #     item = QtWidgets.QGraphicsEllipseItem(i*75, 100, 60, 40)
    #     scene.addItem(item)
    view.show()
    sys.exit(app.exec_())