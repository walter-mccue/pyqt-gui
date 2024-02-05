# QCheckbox

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QCheckBox, QMainWindow
import sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    widget = QCheckBox("This is a checkbox")
    widget.setCheckState(Qt.Checked)
    # For unchecked: widget.setCheckState(Qt.Unchecked)
    # For tristate: widget.setCheckState(Qt.PartiallyChecked)
    # Or: widget.setTriState(True)
    widget.stateChanged.connect(self.show_state)
    self.setCentralWidget(widget)

  def show_state(self, s):
    print(s == Qt.Checked)
    print(s)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
