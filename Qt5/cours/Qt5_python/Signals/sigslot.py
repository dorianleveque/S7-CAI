from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal,pyqtSlot
class SigSlot (QtCore.QObject) :
  value_changed = pyqtSignal(int)
  def __init__(self):
    QtCore.QObject.__init__(self)
    self.value=0
  def get_value(self) :
    return self.value
  def set_value(self,v) :
   if (v!=self.value) :
    self.value=v
    self.value_changed.emit(v)

if __name__ == "__main__" :
  a,b=SigSlot(),SigSlot()
  # QtCore.QObject.connect(a, QtCore.SIGNAL('value_changed(int)'),
  #                 b, QtCore.SLOT('set_value(int)'))
  a.value_changed.connect(b.set_value)   
#  QObject::connect(&b,SIGNAL(valueChanged(int)),
#                   &a,SLOT(setValue(int)));
  b.set_value(10)
  print(a.get_value()) # 0 or 10 ?
  a.set_value(100)
  print(b.get_value()) # 10 or 100  ?

