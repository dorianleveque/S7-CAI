import sys
from PyQt5 import QtCore,QtCore,QtGui,QtWidgets,QtSvg

class Mapper(QtCore.QObject):
    def __init__(self,parent) :
        super(Mapper, self).__init__()
        layout = QtGui.QVBoxLayout(parent)
        signalMapper = QtCore.QSignalMapper(self)
        self.buttons=[]
        for i in range(5) :
            self.buttons.append(QtGui.QPushButton(str(i)))

        for i, button in enumerate(self.buttons) :
            signalMapper.setMapping(button, i)
            button.clicked.connect(signalMapper.map)
            signalMapper.mapped.connect(self.my_slot)
            layout.addWidget(button)

    def my_slot(self, index):
        print("button:", index)

# https://stackoverflow.com/questions/35819538/using-lambda-expression-to-connect-slots-in-pyqt
class Keypad(QtWidgets.QWidget):
    def __init__(self,parent=None) :
        super(Keypad, self).__init__()
        layout = QtWidgets.QVBoxLayout(self)
        self.buttons=[]
        for i in range(5) :
            self.buttons.append(QtWidgets.QPushButton(str(i),self))
        for i, button in enumerate(self.buttons) :
            layout.addWidget(button)
            button.clicked.connect(lambda state,x=i: self.on_selected(state,x))
    def on_selected(self,  state, index):
        print('state', state)
        print('index', index)

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(QtGui.QWidget, self).__init__()

        main_layout = QtWidgets.QVBoxLayout(self)

        # Works:
        self.button_1 = QtWidgets.QPushButton('Button 1 manual', self)
        self.button_2 = QtWidgets.QPushButton('Button 2 manual', self)
        main_layout.addWidget(self.button_1)
        main_layout.addWidget(self.button_2)

        self.button_1.clicked.connect(lambda x:self.button_pushed(1))
        self.button_2.clicked.connect(lambda x:self.button_pushed(2))

        # Doesn't work:
        self.buttons = []
        for idx in [3, 4]:
            button = QtWidgets.QPushButton('Button {} auto'.format(idx), self)
            button.clicked.connect(lambda x=idx: self.button_pushed(x))
            self.buttons.append(button)
            main_layout.addWidget(button)
    def button_pushed(self, num):
        print('Pushed button {}'.format(num))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #mw=QtGui.QWidget()
    #mapper = Mapper(mw)
    keypad = Keypad()
 #   mw.show()
    keypad.show()
    sys.exit(app.exec_())
