
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
  QApplication,
  QLabel,
  QMainWindow,
  QPushButton,
  QTabWidget,
  QWidget,
)
import sys

from layout_colorwidget import Color

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")

    tabs = QTabWidget()
    tabs.setTabPosition(QTabWidget.West) # Use cardinal directions to set tab position
    tabs.setMovable(True) # Allows user to reorder tabs

    for n, color in enumerate(["red", "green", "blue", "yellow"]):
      tabs.addTab(Color(color), color) # associates the string as the tab name and the layout as the color

    self.setCentralWidget(tabs)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
