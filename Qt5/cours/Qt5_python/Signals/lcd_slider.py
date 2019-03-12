#!/usr/bin/python

# sigslot.py

import sys
from PyQt5 import QtCore,QtGui, QtWidgets


class SigSlot(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setWindowTitle('signal & slot')

        lcd = QtWidgets.QLCDNumber(self)
        slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)
        # self.connect(slider,  QtCore.SIGNAL('valueChanged(int)'), lcd, 
		# QtCore.SLOT('display(int)') )
        slider.valueChanged.connect(lcd.display)
  
        self.resize(250, 150)

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    qb = SigSlot()
    qb.show()
    sys.exit(app.exec_())
