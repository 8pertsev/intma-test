import design

from PyQt5 import QtWidgets
from threading import Thread
from db_utils.sql_manager import sql_manager
from db_utils.db_io import db_io
from popups.error import Error


class INTMAApp(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.xls_path.setText("filepath to xlsx:")
        self.csv_path.setText("filepath to csv: ")
        self.choose_xls.clicked.connect(lambda: self.set_filepath('xls'))
        self.choose_csv.clicked.connect(lambda: self.set_filepath('csv'))
        self.import_to_db.clicked.connect(self.write_to_db)
        self.export_from_db.clicked.connect(self.export_db)
        self.e = None

    # set filepaths for files
    def set_filepath(self, file_type):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'OpenFile')
        if file_type == 'xls':
            self.xls_path.setText(file_path)

        elif file_type == 'csv':
            self.csv_path.setText(file_path)

    # fastest solution, that I came up with to handle errors. Didn't find any easy way to pass exceptions into main
    # thread, and its quite tricky to work with interface from notmain thread, so I made a flag.
    def exc_check(self, e):
        self.e = e
        return self.e

    def write_to_db(self):

        with sql_manager() as connection:

            thread_xlsx = Thread(target=db_io.write_from_xlsx, args=(connection, self.xls_path.text(), self.exc_check))
            thread_csv = Thread(target=db_io.write_from_csv, args=(connection, self.csv_path.text(), self.exc_check))

            thread_xlsx.start()
            thread_csv.start()

            thread_xlsx.join()
            thread_csv.join()

            if self.e:
                Error.show_error(self.e)
                self.e = None

    def export_db(self):
        with sql_manager() as connection:
            thread_to_xls = Thread(target=db_io.export_to_xlsx, args=(connection,))
            thread_to_csv = Thread(target=db_io.export_to_csv, args=(connection,))

            thread_to_xls.start()
            thread_to_csv.start()

            thread_to_xls.join()
            thread_to_csv.join()