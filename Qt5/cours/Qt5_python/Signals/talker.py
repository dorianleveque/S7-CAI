from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

class TalkAndListen(QObject):
  signal_talk = pyqtSignal(str)
  def __init__(self):
    QObject.__init__(self)
  def listen_to_me(self,text):
    self.signal_talk.emit(text)
  @pyqtSlot(str)
  def slot_listen(self,text):
    print("You say : " + text)

if __name__ == "__main__" :
  talker = TalkAndListen()
  listener=TalkAndListen()
  talker.signal_talk.connect(listener.slot_listen)
  talker.listen_to_me("Did you hear what I say !")
  listener.signal_talk.connect(talker.slot_listen)
  listener.listen_to_me("I am not deaf !")
