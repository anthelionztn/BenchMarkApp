import sys
from mainWindowLogic import *
import mainWindowLogic
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # mainWindow = MainWindow()
    # mainWindow.show()
    # sys.exit(app.exec())


    # app = QApplication(sys.argv)
    # MainWindow = QMainWindow()
    # ui = mainWindowLogic.Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec())

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
