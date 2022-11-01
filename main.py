from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
  def __init__(self):
    super(MyWindow. self).__init__()
    self.initUI()

  def initUI(self):
    pass

class PlayerRow():
  pass

def create_app():
  app = QApplication(sys.argv)
  win = QMainWindow()
  win.show()
  sys.exit(app.exec_())

if __name__ == "__main__":
  create_app()