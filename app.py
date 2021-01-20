import sys

from INTMA import INTMAApp
from PyQt5 import QtWidgets


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = INTMAApp.INTMAApp()
    window.setWindowTitle('INTMA')
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
