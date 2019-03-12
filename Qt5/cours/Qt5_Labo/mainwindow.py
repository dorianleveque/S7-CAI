#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import QT_VERSION_STR

from scene import Scene

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.resize(500, 300)
        self.setWindowTitle("Editeur v0.1")
        self.create_scene()
        self.create_actions()
        self.create_menus()
        self.connect_actions()
##        textEdit = QtGui.QTextEdit()
##        self.setCentralWidget(textEdit)
    def create_scene(self) :
        view=QtWidgets.QGraphicsView()
        self.scene=Scene(self)
        text= self.scene.addText("Hello World !")
    #    text.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        text.setPos(100,200)
    #    text.setVisible(True)
        view.setScene(self.scene)
        self.setCentralWidget(view)

    def create_actions(self) :
        self.action_save = QtWidgets.QAction(QtGui.QIcon('icons/save.png'), 'Save', self)
        self.action_save.setShortcut('Ctrl+S')
        self.action_save.setStatusTip('Save to file')
        self.action_open = QtWidgets.QAction(
            QtGui.QIcon('icons/open.png'), 'Open', self)
        self.action_open.setShortcut('Ctrl+O')
        self.action_open.setStatusTip('Open file')
        self.action_exit = QtWidgets.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        self.action_exit.setShortcut('Ctrl+Q')
        self.action_exit.setStatusTip('Exit application')
        self.group_action_tools = QtWidgets.QActionGroup(self)
        self.action_line = QtWidgets.QAction(self.tr("&Line"), self)
        self.action_line.setCheckable(True)
        self.action_line.setChecked(True)
        self.group_action_tools.addAction(self.action_line)
        self.action_pen_color = QtWidgets.QAction(self.tr("Color"), self)
        self.action_brush_color = QtWidgets.QAction(self.tr("Color"), self)

    def create_menus(self) :
 #       statusbar=self.statusBar()
        menubar = self.menuBar()
        menu_file = menubar.addMenu('&File')
        menu_file.addAction(self.action_open)
        menu_file.addAction(self.action_save)
        menu_file.addAction(self.action_exit)

        menu_tools = menubar.addMenu('&Tools')
        menu_tools.addAction(self.action_line)

        menu_style=menubar.addMenu('&Style')
        menu_style_pen=menu_style.addMenu('Pen')
        menu_style_pen.addAction(self.action_pen_color)
        menu_style_brush=menu_style.addMenu('Brush')
        menu_style_brush.addAction(self.action_brush_color)

        menu_help=self.menuBar().addMenu(self.tr("&Help"))

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(self.action_exit)

        self.action_about = menu_help.addAction(self.tr("& About this Editor"))

    def connect_actions(self) :
        self.action_open.triggered.connect(self.file_open)
        self.action_save.triggered.connect(self.file_save)
        self.action_exit.triggered.connect(self.file_exit)
        self.action_about.triggered.connect(self.help_about)
        self.action_pen_color.triggered.connect(self.pen_color_selection)
        self.action_brush_color.triggered.connect(self.brush_color_selection)
        self.action_line.triggered.connect(lambda checked, tool="line": self.set_action_tool(checked,tool))

    def set_action_tool(self,checked, tool) :
        print("lamda checked, tool : ",checked, tool)
        self.scene.set_tool(tool)
    
    def file_exit(self):
        exit(0)
   
    def file_open(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', os.getcwd())
        fileopen=QtCore.QFile(filename)
        if fileopen.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)==None :
            print("fileopen.open(QtCore.QIODevice.WriteOnly)==None")
            return -1
        else :
            print(filename + " opened !")

    def file_save(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', os.getcwd())
        filesave=QtCore.QFile(filename)
        if filesave.open(QtCore.QIODevice.WriteOnly)==None :
            print("filesave.open(QtCore.QIODevice.WriteOnly)==None")
            return -1
        else :
            print(filename + " ready to save !")

    def pen_color_selection(self):
        color = QtWidgets.QColorDialog.getColor(QtCore.Qt.yellow, self )
        if color.isValid() :
            print("Color Choosen : ",color.name())
        else :
            print("color is not a valid one !")

    def brush_color_selection(self):
        color = QtWidgets.QColorDialog.getColor(QtCore.Qt.yellow, self )
        if color.isValid() :
            print("Color Choosen : ",color.name())
        else :
            print("color is not a valid one !")
        
    def help_about(self):
        QtWidgets.QMessageBox.information(self, self.tr("About Me"),
                                self.tr("Jean Dupond\n copyright ENIB 2019"))
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

if __name__ == "__main__" :  
    print(QT_VERSION_STR)
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
