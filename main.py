import sys
from mainWindowLogic import *
import mainWindowLogic
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
