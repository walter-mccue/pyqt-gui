
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# Imports "Color" from file "layout_colorwidget.py"
from layout_colorwidget import Color

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    widget = Color("red")
    self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
