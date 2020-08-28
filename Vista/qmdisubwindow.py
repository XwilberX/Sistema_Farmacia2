import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiSubWindow, QMdiArea, QTextEdit, QWidget
from subwindow import SubWindow

import sys
sys.path.append('../Modelo/')
from farm import Clave

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('mysql+pymysql://root:wil99@localhost/prueba')
Session = sessionmaker(bind=engine)
session = Session()

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("MDI demo")
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        self.ui = SubWindow()
        self.ui.createSubWindow()
        self.mdi.addSubWindow(self.ui)

        self.ui.show()

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()