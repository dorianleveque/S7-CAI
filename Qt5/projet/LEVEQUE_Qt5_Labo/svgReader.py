from PyQt5 import QtCore, QtXml

class SvgReader():

    def __getRectangles(self, filename):
        pass

    def getElements(self, fileopen):
        graphicsList = []
        
        doc = QtXml.QDomDocument()
        if not doc.setContent(fileopen):
            return -1
        
        gList = doc.elementsByTagName("g")
        print(gList)
        
            
if __name__ == "__main__":
    print("\n\n")
    s = SvgReader()
    fileopen = QtCore.QFile('data/test.svg')
    s.getElements(fileopen)
