# http://www.gchagnon.fr/cours/python/pyqt.html

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsScene

app=QApplication(sys.argv)
scene=QGraphicsScene(app)

window=QWidget()
window.resize(500,300)
window.move(500, 500)
window.setWindowTitle("Application : version 0.1")
window.show()
sys.exit(app.exec_())
