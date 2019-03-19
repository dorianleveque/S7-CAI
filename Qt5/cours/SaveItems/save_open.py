#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,sys
from PyQt5 import QtCore,QtGui,QtWidgets

from PyQt5.QtCore import QT_VERSION_STR

def file_open(filename):
    fileopen=QtCore.QFile(filename)
    if fileopen.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)==None :
        print("fileopen.open(QtCore.QIODevice.WriteOnly)==None")
        return -1
    xmlReader=QtCore.QXmlStreamReader(fileopen)
    xmlReader.setDevice(fileopen)
    while not xmlReader.atEnd() :
        if xmlReader.name() != "" :
            print("name",xmlReader.name() )
            if xmlReader.isStartElement() :
                if xmlReader.name()== "GraphicsItem" :
                    print("GraphicsItem start")
                    if xmlReader.attributes().value("type") == "rect" :
                        rect=None
                        print("rect")
                        while  xmlReader.readNextStartElement() :
                            print("xmlReader.readNextStartElement()")
                            if xmlReader.name()== "shape" :
                                x=float(xmlReader.attributes().value("x"))
                                y=float(xmlReader.attributes().value("y"))
                                w=float(xmlReader.attributes().value("w"))
                                h=float(xmlReader.attributes().value("h"))
                                print("shape",x,y,w,h)
    #                            rect=QtWidgets.QGraphicsRectItem(x,y,w,h)
                            xmlReader.readNext()
                    print("GraphicsItem end")            
        xmlReader.readNext()                       

def file_save(filename):
    filesave=QtCore.QFile(filename)
    if filesave.open(QtCore.QIODevice.WriteOnly)==None :
        print("filesave.open(QtCore.QIODevice.WriteOnly)==None")
        return -1
    xmlWriter=QtCore.QXmlStreamWriter(filesave)
    xmlWriter.setAutoFormatting(True)

    xmlWriter.writeStartDocument()
    xmlWriter.writeStartElement("Scene")                # Start Scene Root Element
    xmlWriter.writeAttribute("version", "v1.0")
    xmlWriter.writeStartElement("GraphicsItemList")     # Star GraphicsItemList Element
##    items=self.scene.items()
##    for i  in range(len(items)) :
##        xmlWriter.writeStartElement("GraphicsItem")
##       num=items[i].type()
##       if num==3 :
##           xmlWriter.writeAttribute("type","rect")
##           ...
    xmlWriter.writeStartElement("GraphicsItem")         # Star GraphicsItem Element
    xmlWriter.writeAttribute("type","rect")
    xmlWriter.writeStartElement("shape")                # Star GraphicsItem Element
    xmlWriter.writeAttribute("x", str(10))
    xmlWriter.writeAttribute("y", str(40))
    xmlWriter.writeAttribute("w", str(200))
    xmlWriter.writeAttribute("h", str(300))
    xmlWriter.writeEndElement()                         # End shape Element
    xmlWriter.writeEndElement()                         # End GraphicsItem Element
    xmlWriter.writeEndElement()                         # End GraphicsItemList Element
    xmlWriter.writeEndElement()                         # End Scene Root Element
    filesave.close()

if __name__ == "__main__" :  
    print(QT_VERSION_STR)
    file_save("save_open.xml")
    file_open("save_open.xml")
