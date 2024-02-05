# QLabel

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
import sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    widget = QLabel("Hello")
    font = widget.font()
    font.setPointSize(30)
    widget.setFont(font)
    widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    # Horizontal: Qt.AlignLeft, Qt.AlignRight, Qt.AlignHCenter, Qt.AlignJustify, Qt.AlignHCenter
    # Vertical: Qt.AlignTop , Qt.AlignBottom, Qt.AlignVCenter, Qt.AlignVCenter
    # Centered on both axises: Qt.AlignCenter
    self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
