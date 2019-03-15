#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import QT_VERSION_STR, QObject

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

        #self.parentWidget().installTranslator(translate)
        #QtWidgets.QApplication.instance().installTranslator(translate)
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
        # ------- FILE -------------
        # action NEW
        self.action_new = QtWidgets.QAction(QtGui.QIcon('icons/new.png'), self.tr('New'), self)
        self.action_new.setShortcut('Ctrl+N')
        self.action_new.setStatusTip('New file')
      
        # action OPEN
        self.action_open = QtWidgets.QAction(QtGui.QIcon('icons/open.png'), self.tr('Open'), self)
        self.action_open.setShortcut('Ctrl+O')
        self.action_open.setStatusTip('Open file')
        
        # action SAVE
        self.action_save = QtWidgets.QAction(QtGui.QIcon('icons/save.png'), self.tr('Save'), self)
        self.action_save.setShortcut('Ctrl+S')
        self.action_save.setStatusTip('Save to file')
        
        # action SAVE AS
        self.action_save_as = QtWidgets.QAction(QtGui.QIcon('icons/saveas.png'), self.tr('Save as'), self)
        self.action_save_as.setShortcut('Ctrl+S')
        self.action_save_as.setStatusTip('Save to file')  
        
        # action EXIT
        self.action_exit = QtWidgets.QAction(QtGui.QIcon('icons/exit.png'), self.tr('Exit'), self)
        self.action_exit.setShortcut('Ctrl+Q')
        self.action_exit.setStatusTip('Exit application')
        self.group_action_tools = QtWidgets.QActionGroup(self)
        
        
        # -------- TOOLS ------------
        # action LINE
        self.action_line = QtWidgets.QAction(QtGui.QIcon('icons/line.png'), self.tr("&Line"), self)
        self.action_line.setCheckable(True)
        self.action_line.setChecked(True)
        self.group_action_tools.addAction(self.action_line)
        
        # action RECTANGLE
        self.action_rect = QtWidgets.QAction(QtGui.QIcon('icons/rectangle.png'), self.tr("&Rectangle"), self)
        self.action_rect.setCheckable(True)
        self.group_action_tools.addAction(self.action_rect)
        
        # action ELLIPSE
        self.action_elli = QtWidgets.QAction(QtGui.QIcon('icons/ellipse.png'), self.tr("&Ellipse"), self)
        self.action_elli.setCheckable(True)
        self.group_action_tools.addAction(self.action_elli)
       
        # action POLYGON
        self.action_poly = QtWidgets.QAction(QtGui.QIcon('icons/polygon.png'), self.tr("&Polygon"), self)
        self.action_poly.setCheckable(True)
        self.group_action_tools.addAction(self.action_poly)
        
        # action TEXT
        self.action_text = QtWidgets.QAction(QtGui.QIcon('icons/text.png'), self.tr("&Text"), self)
        self.action_text.setCheckable(True)
        self.group_action_tools.addAction(self.action_text)
        
        # -------- STYLE ------------
        self.action_pen_color = QtWidgets.QAction(QtGui.QIcon('icons/select_color.png'), self.tr("Color"), self)
        self.action_pen_line  = QtWidgets.QAction(QtGui.QIcon('icons/line.png'), self.tr("Line"), self)
        self.action_pen_width = QtWidgets.QAction(QtGui.QIcon('icons/width.png'), self.tr("Width"), self)
        
        self.action_brush_color = QtWidgets.QAction(QtGui.QIcon('icons/color.png'), self.tr("Color"), self)
        self.action_brush_fill  = QtWidgets.QAction(QtGui.QIcon('icons/fill.png'), self.tr("Fill"), self)
        
        self.action_font = QtWidgets.QAction(self.tr("Font"), self)
        
        # -------- OPTIONS ---------
        self.action_select_lang = QtWidgets.QAction(QtGui.QIcon('icons/select_lang.png'), self.tr("Select lang"), self)

        # ------- HELP -----------
        self.action_about_us  = QtWidgets.QAction(QtGui.QIcon('icons/info.png'), self.tr("About Us"), self)
        self.action_about_qt  = QtWidgets.QAction(QtGui.QIcon('icons/about_qt.png'), self.tr("About Qt"), self)
        self.action_about_app = QtWidgets.QAction(QtGui.QIcon('icons/info_app.png'), self.tr("About this Application"), self)


    def create_menus(self) :
 #       statusbar=self.statusBar()
        #menubar = self.menuBar()
        menubar = QtWidgets.QMenuBar(self)
        self.setMenuBar(menubar)
        # ------- FILE -------------
        menu_file = menubar.addMenu(self.tr('&File'))
        menu_file.addAction(self.action_new)
        menu_file.addAction(self.action_open)
        menu_file.addAction(self.action_save)
        menu_file.addAction(self.action_save_as)
        menu_file.addAction(self.action_exit)

        # -------- TOOLS ------------
        menu_tools = menubar.addMenu(self.tr('&Tools'))
        menu_tools.addAction(self.action_line)
        menu_tools.addAction(self.action_rect)
        menu_tools.addAction(self.action_elli)
        menu_tools.addAction(self.action_poly)
        menu_tools.addAction(self.action_text)

        # -------- STYLE ------------
        menu_style = menubar.addMenu(self.tr('&Style'))
        menu_style_pen = menu_style.addMenu(self.tr('Pen'))
        menu_style_pen.addAction(self.action_pen_color)
        menu_style_pen.addAction(self.action_pen_line)
        menu_style_pen.addAction(self.action_pen_width)
        
        menu_style_brush = menu_style.addMenu(self.tr('Brush'))
        menu_style_brush.addAction(self.action_brush_color)
        menu_style_brush.addAction(self.action_brush_fill)
        
        menu_style.addAction(self.action_font)
       
        # -------- OPTIONS ---------
        menu_options = menubar.addMenu(self.tr('&Options'))
        menu_options.addAction(self.action_select_lang)

        # -------- HELP ------------
        menu_help = menubar.addMenu(self.tr("&Help"))
        menu_help.addAction(self.action_about_us)
        menu_help.addAction(self.action_about_qt)
        menu_help.addAction(self.action_about_app)


        # -------- TOOLBAR ------------
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(self.action_exit)

        
    def connect_actions(self) :
        self.action_new.triggered.connect(self.file_new)
        self.action_open.triggered.connect(self.file_open)
        self.action_save.triggered.connect(self.file_save)
        self.action_save_as.triggered.connect(self.file_save_as)
        self.action_exit.triggered.connect(self.file_exit)
        
        self.action_line.triggered.connect(lambda checked, tool="line": self.set_action_tool(checked,tool))
        self.action_rect.triggered.connect(lambda checked, tool="rect": self.set_action_tool(checked,tool))
        self.action_elli.triggered.connect(lambda checked, tool="elli": self.set_action_tool(checked,tool))
        self.action_poly.triggered.connect(lambda checked, tool="poly": self.set_action_tool(checked,tool))
        self.action_text.triggered.connect(lambda checked, tool="text": self.set_action_tool(checked,tool))
        
        self.action_pen_color.triggered.connect(self.pen_color_selection)
        self.action_pen_line.triggered.connect(self.pen_line_selection)
        self.action_pen_width.triggered.connect(self.pen_width_selection)
        
        self.action_brush_color.triggered.connect(self.brush_color_selection)
        self.action_brush_fill.triggered.connect(self.brush_fill_selection)
        self.action_font.triggered.connect(self.font_selection)
        
        self.action_select_lang.triggered.connect(self.change_lang)

        self.action_about_us.triggered.connect(self.help_about_us)
        self.action_about_qt.triggered.connect(self.help_about_qt)
        self.action_about_app.triggered.connect(self.help_about_app)
        
        
    ### CALLBACK FUNCTIONS ##################################
    
    def changeEvent(self, event):
        if (event.type() == QtCore.QEvent.LanguageChange):
            self.create_actions()
            self.create_menus()
            self.connect_actions()

    def change_lang(self):
        app = QtWidgets.QApplication.instance()
        translate = QtCore.QTranslator(app)
        translate.load('lang/en.qm')
        app.installTranslator(translate)

    ## FILE ------------------------------------------------
    def file_new(self):
        print("Create new file")
   
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
        filesave = QtCore.QFile(filename)
        if filesave.open(QtCore.QIODevice.WriteOnly) == None :
            print("filesave.open(QtCore.QIODevice.WriteOnly)==None")
            return -1
        else :
            print(filename + " ready to save !")
            
    def file_save_as(self):
        print("Sauvegarder sous")

    def file_exit(self):
        buttonReply = QtWidgets.QMessageBox.question(self, self.tr('Quit ?'), self.tr("Do you want to quit without saving ?"), QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            print('Yes clicked.')
            exit(0)
        else:
            print('No clicked.')
        


    ## TOOLS ------------------------------------------------
    def set_action_tool(self,checked, tool) :
        print("lamda checked, tool : ",checked, tool)
        self.scene.set_tool(tool)



    ## STYLE ------------------------------------------------
    # PEN 
    def pen_color_selection(self):
        color = QtWidgets.QColorDialog.getColor(QtCore.Qt.yellow, self )
        if color.isValid() :
            self.scene.set_pen_color(color)
            print("Color Choosen : ",color.name())
        else :
            print("color is not a valid one !")
            
    def pen_line_selection(self):
        print("pen_line_selection")
    
    def pen_width_selection(self):
        print("pen_width_selection")


    # BRUSH
    def brush_color_selection(self):
        color = QtWidgets.QColorDialog.getColor(QtCore.Qt.yellow, self )
        if color.isValid() :
            self.scene.set_brush_color(color)
            print("Color Choosen : ",color.name())
        else :
            print("color is not a valid one !")
        
    def brush_fill_selection(self):
        print("brush_fill_selection")
    
    
    # FONT
    def font_selection(self):
        print("font_selection")
       
    
    
    ## HELP ------------------------------------------------
    def help_about_us(self):
        QtWidgets.QMessageBox.information(self, self.tr("About Me"), self.tr("Application created by LEVEQUE Dorian\ncopyright © LEVEQUE Dorian 2019"))
        
    def help_about_qt(self):
        QtWidgets.QMessageBox.information(self, self.tr("About Qt"), self.tr("This application is developed with PyQt5.\nFor more information, please visit\nthe following site https://www.qt.io\n\nVersion de PyQt5: 5.12"))
        
    def help_about_app(self):
        QtWidgets.QMessageBox.information(self, self.tr("About App"), self.tr("Version Alpha 0.1"))


    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

if __name__ == "__main__" :  
    print(QT_VERSION_STR)
    app = QtWidgets.QApplication(sys.argv)
    
    locale = QtCore.QLocale().system().name().split('_')
    print(locale)

    translate = QtCore.QTranslator(app)
    translate.load('lang/'+locale[0]+'.qm')
    app.installTranslator(translate)

    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
