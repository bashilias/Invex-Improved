import sys
from PyQt6.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,300,450)
        self.setWindowTitle("Invex-Improved")

        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())