#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import QT_VERSION_STR, QObject

from scene import Scene
from settings import Settings

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.settings = Settings("MySoft", "Simply Paint")
        self.srcfile = None    # Current file for save option
        self.resize(600, 450)
        self.setWindowTitle("Simply Paint v0.1")
        self.setWindowIcon(QtGui.QIcon("./icons/simplyPaint.ico"))
        self.create_scene()
        self.create_actions()
        self.create_menus()
        self.connect_actions()
        self.create_toolbar()

        # init language 
        lang = self.settings.get_selected_language()
        locale = lang if (lang) else 'en'
        self.set_selected_language(True, locale)

##        textEdit = QtGui.QTextEdit()
##        self.setCentralWidget(textEdit)

    def create_scene(self) :
        view = QtWidgets.QGraphicsView()
        self.scene = Scene(self)
        text = self.scene.addText("Hello World !")
        text.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        text.setPos(100,200)
        text.setVisible(True)
        view.setScene(self.scene)
        self.setCentralWidget(view)

    def create_actions(self) :
        # ------- FILE -------------
        # action NEW
        self.action_new = QtWidgets.QAction(QtGui.QIcon('icons/new.png'), self.tr('New'), self)
        self.action_new.setShortcut('Ctrl+N')
        self.action_new.setStatusTip(self.tr('New file'))
        self.action_new.setToolTip(self.tr('New file'))
      
        # action OPEN
        self.action_open = QtWidgets.QAction(QtGui.QIcon('icons/open.png'), self.tr('Open'), self)
        self.action_open.setShortcut('Ctrl+O')
        self.action_open.setStatusTip(self.tr('Open a file'))
        self.action_open.setToolTip(self.tr('Open a file'))
        
        # action SAVE
        self.action_save = QtWidgets.QAction(QtGui.QIcon('icons/save.png'), self.tr('Save'), self)
        self.action_save.setShortcut('Ctrl+S')
        self.action_save.setStatusTip(self.tr('Save to file'))
        self.action_save.setToolTip(self.tr('Save to file'))
        
        # action SAVE AS
        self.action_save_as = QtWidgets.QAction(QtGui.QIcon('icons/saveas.png'), self.tr('Save as'), self)
        self.action_save_as.setShortcut('Ctrl+Shift+S')
        self.action_save_as.setStatusTip(self.tr('Save to file in a chosen directory'))
        self.action_save_as.setToolTip(self.tr('Save to file in a chosen directory')) 
        
        # action EXIT
        self.action_exit = QtWidgets.QAction(QtGui.QIcon('icons/exit.png'), self.tr('Exit'), self)
        self.action_exit.setShortcut('Ctrl+Q')
        self.action_exit.setStatusTip(self.tr('Exit Application'))
        self.action_exit.setToolTip(self.tr('Exit Application'))
        
        
        # -------- TOOLS ------------
        # action LINE
        self.group_action_tools = QtWidgets.QActionGroup(self)

        self.action_line = QtWidgets.QAction(QtGui.QIcon('icons/line.png'), self.tr("&Line"), self)
        self.action_line.setStatusTip(self.tr('Draw a line'))
        self.action_line.setToolTip(self.tr('Draw a line'))
        self.action_line.setCheckable(True)
        self.action_line.setChecked(True)
        self.group_action_tools.addAction(self.action_line)
        
        # action RECTANGLE
        self.action_rect = QtWidgets.QAction(QtGui.QIcon('icons/rectangle.png'), self.tr("&Rectangle"), self)
        self.action_rect.setStatusTip(self.tr('Draw a rectangle'))
        self.action_rect.setToolTip(self.tr('Draw a rectangle'))
        self.action_rect.setCheckable(True)
        self.group_action_tools.addAction(self.action_rect)
        
        # action ELLIPSE
        self.action_elli = QtWidgets.QAction(QtGui.QIcon('icons/ellipse.png'), self.tr("&Ellipse"), self)
        self.action_elli.setStatusTip(self.tr('Draw an ellipse'))
        self.action_elli.setToolTip(self.tr('Draw an ellipse'))
        self.action_elli.setCheckable(True)
        self.group_action_tools.addAction(self.action_elli)
       
        # action POLYGON
        self.action_poly = QtWidgets.QAction(QtGui.QIcon('icons/polygon.png'), self.tr("&Polygon"), self)
        self.action_poly.setStatusTip(self.tr('Draw a polygon'))
        self.action_poly.setToolTip(self.tr('Draw a polygon'))
        self.action_poly.setCheckable(True)
        self.group_action_tools.addAction(self.action_poly)
        
        # action TEXT
        self.action_text = QtWidgets.QAction(QtGui.QIcon('icons/text.png'), self.tr("&Text"), self)
        self.action_text.setStatusTip(self.tr('Place a text'))
        self.action_text.setToolTip(self.tr('Place a text'))
        self.action_text.setCheckable(True)
        self.group_action_tools.addAction(self.action_text)
        
        # -------- STYLE ------------
        self.action_pen_color = QtWidgets.QAction(QtGui.QIcon('icons/select_color.png'), self.tr("Color"), self)
        self.action_pen_line  = QtWidgets.QAction(QtGui.QIcon('icons/texture.png'), self.tr("Line"), self)
        self.action_pen_width = QtWidgets.QAction(QtGui.QIcon('icons/width.png'), self.tr("Width"), self)
        
        self.action_brush_color = QtWidgets.QAction(QtGui.QIcon('icons/color.png'), self.tr("Color"), self)
        self.action_brush_fill  = QtWidgets.QAction(QtGui.QIcon('icons/fill.png'), self.tr("Fill"), self)
        
        self.action_font = QtWidgets.QAction(QtGui.QIcon('icons/font.png'), self.tr("Font"), self)
        
        # -------- OPTIONS ---------
        self.group_options_lang = QtWidgets.QActionGroup(self)

        self.action_options_lang_fr = QtWidgets.QAction(self.tr("French"), self)
        self.action_options_lang_fr.setCheckable(True)
        self.group_options_lang.addAction(self.action_options_lang_fr)
        
        self.action_options_lang_en = QtWidgets.QAction(self.tr("English"), self)
        self.action_options_lang_en.setCheckable(True)
        self.group_options_lang.addAction(self.action_options_lang_en)

        default_lang = self.settings.get_selected_language()
        exec("self.action_options_lang_%s.setChecked(%d)" % (default_lang, True))

        # ------- HELP -----------
        self.action_about_us  = QtWidgets.QAction(QtGui.QIcon('icons/info.png'), self.tr("About Us"), self)
        self.action_about_qt  = QtWidgets.QAction(QtGui.QIcon('icons/about_qt.png'), self.tr("About Qt"), self)
        self.action_about_app = QtWidgets.QAction(QtGui.QIcon('icons/info_app.png'), self.tr("About this Application"), self)


    def create_menus(self) :
        statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(statusbar)
        # menubar = self.menuBar()
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
        menu_style_pen.setIcon(QtGui.QIcon('icons/pen.png'))
        menu_style_pen.addAction(self.action_pen_color)
        menu_style_pen.addAction(self.action_pen_line)
        menu_style_pen.addAction(self.action_pen_width)
        
        menu_style_brush = menu_style.addMenu(self.tr('Brush'))
        menu_style_brush.setIcon(QtGui.QIcon('icons/brush.png'))
        menu_style_brush.addAction(self.action_brush_color)
        menu_style_brush.addAction(self.action_brush_fill)
        
        menu_style.addAction(self.action_font)
       
        # -------- OPTIONS ---------
        menu_options = menubar.addMenu(self.tr('&Options'))
        menu_options_lang = menu_options.addMenu(self.tr("Select lang"))
        menu_options_lang.setIcon(QtGui.QIcon('icons/select_lang.png'))
        menu_options_lang.addAction(self.action_options_lang_en)
        menu_options_lang.addAction(self.action_options_lang_fr)

        # -------- HELP ------------
        menu_help = menubar.addMenu(self.tr("&Help"))
        menu_help.addAction(self.action_about_us)
        menu_help.addAction(self.action_about_qt)
        menu_help.addAction(self.action_about_app)


    def create_toolbar(self):
        # -------- TOOLBAR ------------
        file_toolbar = QtWidgets.QToolBar(self)
        self.addToolBar(file_toolbar)
        file_toolbar.addAction(self.action_new)
        file_toolbar.addAction(self.action_open)
        file_toolbar.addAction(self.action_save)

        tool_toolbar = QtWidgets.QToolBar(self)
        self.addToolBar(tool_toolbar)
        tool_toolbar.addAction(self.action_line)
        tool_toolbar.addAction(self.action_rect)
        tool_toolbar.addAction(self.action_elli)
        tool_toolbar.addAction(self.action_poly)
        tool_toolbar.addAction(self.action_text)

        #toolbar = self.addToolBar('Exit')
        #toolbar.addAction(self.action_exit)

        
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
        
        self.action_options_lang_en.triggered.connect(lambda checked, lang="en": self.set_selected_language(checked,lang))
        self.action_options_lang_fr.triggered.connect(lambda checked, lang="fr": self.set_selected_language(checked,lang))

        self.action_about_us.triggered.connect(self.help_about_us)
        self.action_about_qt.triggered.connect(self.help_about_qt)
        self.action_about_app.triggered.connect(self.help_about_app)
        
        
    ### EVENTS FUNCTIONS ##################################
    
    def closeEvent(self, event):
        if (event.type() == QtCore.QEvent.Close):
            self.file_exit()
        event.ignore()

    def changeEvent(self, event):
        if (event.type() == QtCore.QEvent.LanguageChange):
            self.create_menus()
        event.ignore()

    ## FILE ------------------------------------------------
    def file_new(self):
        print("Create new file")
   
    def file_open(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', os.getcwd())
        fileopen = QtCore.QFile(filename[0])
        if fileopen.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)==None :
            print("fileopen.open(QtCore.QIODevice.WriteOnly)==None")
            return -1
        else :
            print(filename[0] + " opened !")

    def file_save(self):
        if (self.srcfile):
            print("save")
        else:
            self.file_save_as()
            
    def file_save_as(self):
        print("Sauvegarder sous")
        filename = QtWidgets.QFileDialog.getSaveFileName(self, self.tr('Save File'), os.getcwd())
        filesave = QtCore.QFile(filename[0])
        if filesave.open(QtCore.QIODevice.WriteOnly) == None :
            print("filesave.open(QtCore.QIODevice.WriteOnly)==None")
            return -1
        else :
            print(filename[0] + " ready to save !")

    def file_exit(self):
        title = self.tr('Quit ?')
        text  = self.tr("Do you want to quit without saving ?")
        msgbox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, title, text)
        msgbox.setWindowIcon(self.windowIcon())
        no_button = msgbox.addButton(self.tr('No'), QtWidgets.QMessageBox.NoRole)
        yes_button= msgbox.addButton(self.tr('Yes'), QtWidgets.QMessageBox.YesRole)
        msgbox.setDefaultButton(no_button)
        msgbox.exec()

        if (msgbox.clickedButton() == yes_button):
            exit(0)


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
       
    
    ## OPTIONS ---------------------------------------------
    def set_selected_language(self, checked, lang):
        app = QtWidgets.QApplication.instance()
        translate = QtCore.QTranslator(app)
        translate.load("qt_fr")
        translate.load("qtbase_fr")
        translate.load('lang/{}.qm'.format(lang))
        self.settings.set_selected_language(lang)
        app.installTranslator(translate)
        print("new lang " + lang)
        
    ## HELP ------------------------------------------------
    def help_about_us(self):
        QtWidgets.QMessageBox.information(self, self.tr("About Me"), self.tr("Application created by LEVEQUE Dorian\ncopyright © LEVEQUE Dorian 2019"))
        
    def help_about_qt(self):
        QtWidgets.QMessageBox.information(self, self.tr("About Qt"), self.tr("This application is developed with PyQt5.\nFor more information, please visit\nthe following site https://www.qt.io"))
        
    def help_about_app(self):
        title = self.tr("About App")
        text = self.tr("Version: {}\nVersion de PyQt5: {}\nVersion de Python: {}".format("0.1 (alpha)",QT_VERSION_STR, sys.version[0:5]))
        msgbox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,title,text)
        msgbox.setWindowIcon(self.windowIcon())
        ok_button    = msgbox.addButton(self.tr('Ok'), QtWidgets.QMessageBox.AcceptRole)
        copie_button = msgbox.addButton(self.tr("Copie"), QtWidgets.QMessageBox.RejectRole)
        msgbox.setDefaultButton(ok_button)
        msgbox.exec()

        if (msgbox.clickedButton() == copie_button):
            app = QtWidgets.QApplication.instance()
            app.clipboard().setText(text)

    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
