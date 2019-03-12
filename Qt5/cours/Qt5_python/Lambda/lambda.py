from PyQt5 import  QtCore, QtGui, QtWidgets

#https://stackoverflow.com/questions/33304203/pyqt-a-correct-way-to-connect-multiple-signals-to-the-same-function-in-pyqt-qs

class Widget(QtWidgets.QWidget):
    def __init__(self):
        super(Widget, self).__init__()

        # create and set the layout
        lay_main = QtWidgets.QHBoxLayout()
        self.setLayout(lay_main)

        # create two comboboxes and connect them to a single handler with lambda

        combobox = QtWidgets.QComboBox()
        combobox.addItems('Nol Adyn Dwa Tri'.split())
        combobox.currentIndexChanged.connect(lambda ind: self.on_selected('1', ind))
        lay_main.addWidget(combobox)

        combobox = QtWidgets.QComboBox()
        combobox.addItems('Nol Adyn Dwa Tri'.split())
        combobox.currentIndexChanged.connect(lambda ind: self.on_selected('2', ind))
        lay_main.addWidget(combobox)

    # let the handler show which combobox was selected with which value
    def on_selected(self, cb, index):
        print('! combobox ', cb, ' index ', index)

    def __del__(self):
        print('deleted')

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)

    wdg = Widget()
    wdg.show()
    #wdg.deleteLater()
    print('wdg.deleteLater called')

    #del wdg
    print('del widget executed')

    wd2 = Widget()
    wd2.move(300,100)
    wd2.show()

    print('starting event-loop')
    app.exec_()
    