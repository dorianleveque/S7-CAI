from PyQt4 import QtCore,QtCore,QtGui, QtSvg

class Foo(QtCore.QObject):

    signal = QtCore.pyqtSignal()

    def connectSignal():        
        self.signal.connect(self.myAction)

    @QtCore.pyqtSlot()
    def myAction():
        print("signal triggered")


f=Foo()

class Dialog(QDialog):
    def __init__(self):
        super(Dialog, self).__init__()
        button=QPushButton("Click")
        button.clicked.connect(self.slot_method)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(button)
        self.setLayout(mainLayout)
        self.setWindowTitle("Button Example - pythonspot.com")

    def slot_method(self):
        print('slot method called.')
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())
