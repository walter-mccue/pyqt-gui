# QComboBox

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QComboBox, QMainWindow
import sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    widget = QComboBox()
    widget.addItems(["One", "Two", "Three"])

    # To allow users to insert options:
      # widget.setEditable(True)
    # To control how those added options are inserted:
      # widget.setInsertPolicy(***Insert a flag from below***)
        # QComboBox.NoInsert = No insert
        # QComboBox.InsertAtTop = Insert as first item
        # QComboBox.InsertAtCurrent = Replace currently selected item
        # QComboBox.InsertAtBottom = Insert after last item
        # QComboBox.InsertAfterCurrent = Insert after current item
        # QComboBox.InsertBeforeCurrent = Insert before current item
        # QComboBox.InsertAlphabetically = Insert in alphabetical order
    # To control the max number of inserts:
      # widget.setMaxCount(10)

    widget.currentIndexChanged.connect(self.index_changed)
    widget.currentTextChanged.connect(self.text_changed)
    self.setCentralWidget(widget)

  def index_changed(self, i): # i is an int
    print(i)

  def text_changed(self, s): # s is a str
    print(s)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
