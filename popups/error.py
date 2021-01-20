from PyQt5 import QtWidgets


# error shown when something is wrong during file import
class Error:

    @classmethod
    def show_error(cls, file_type):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)

        msg.setText('   Files read error   ')
        msg.setInformativeText('Please check tables you want to import')
        msg.setWindowTitle(f'Error in {file_type}')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        msg.exec()
