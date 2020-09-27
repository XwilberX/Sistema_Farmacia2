

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QCompleter, QApplication, QTableView,QHeaderView
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append('../Modelo/')
from farm import Clave
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import pandas as pd
import pymysql


engine = create_engine('mysql+pymysql://root:@localhost/farmaciaDB')
Session = sessionmaker(bind=engine)
session = Session()
class Ui_BDP(object):
    def __init__(self, x):
        print('el mensaje es :' + x)
        self.x2 = x
    def setupUi(self, BDP):
        BDP.setObjectName("BDP")
        BDP.resize(919, 405)
        BDP.setMinimumSize(QtCore.QSize(919, 405))
        BDP.setMaximumSize(QtCore.QSize(919, 405))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagenes/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BDP.setWindowIcon(icon)
        BDP.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size: 15px;\n"
"}\n"
"QMainWindow{\n"
"background: #b8f4f0;\n"
"}\n"
"QLabel{\n"
"    background:transparent;\n"
"}\n"
"QLineEdit{\n"
"    border:none;\n"
"    border-bottom: 1px solid black;\n"
"    background: transparent;\n"
"}\n"
"QPushButton{\n"
"border-radius:15px;\n"
"background:#ffc001;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background:#dea806;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(BDP)
        self.centralwidget.setObjectName("centralwidget")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 20, 111, 21))
        self.label_9.setObjectName("label_9")
        self.LineClaveBusqueda = QtWidgets.QLineEdit(self.centralwidget)
        self.LineClaveBusqueda.setGeometry(QtCore.QRect(130, 10, 751, 31))
        self.LineClaveBusqueda.setObjectName("LineClaveBusqueda")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 60, 881, 291))
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setObjectName("tableView")
        BDP.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BDP)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 919, 26))
        self.menubar.setObjectName("menubar")
        BDP.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BDP)
        self.statusbar.setObjectName("statusbar")
        BDP.setStatusBar(self.statusbar)

        self.retranslateUi(BDP)
        QtCore.QMetaObject.connectSlotsByName(BDP)


        self.TableViewInsert()

        self.tableView.doubleClicked.connect(self.VentanaClose)

        
    def VentanaClose(self):
        QtWidgets.qApp.activeWindow().close()

    def TableViewInsert(self):
        # INGRESA LOS DATOS A LA TABLA Y HACE BUSQUEDA EN DESCRIPCION
        self.q = pd.read_sql('SELECT corta, descripcion FROM clave WHERE tipo = %s' %self.x2, engine)
        print(self.q)
        self.numero  = session.query(Clave.corta).filter_by(tipo=self.x2).count()
        #aqui se le indica el numero de comlumnas que tendra la tabla
        self.model = QStandardItemModel(self.numero, 2)
        #se le da un encabezado a la tabla
        self.model.setHorizontalHeaderLabels(['Clave', 'Descripcion'])
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #se meten los datos a la talba
        for z in range(self.numero):
            for m in range(2):
                item = QStandardItem(self.q.iloc[z, m])
                self.model.setItem(z, m, item)
        #se instancia la clase , esa clase nos ayuda que al escribir busque algo
        buscador = QSortFilterProxyModel()
        #este sirve para que puedan buscar alguna cosa no importa si es en mayusculas o minusculas
        buscador.setFilterCaseSensitivity(Qt.CaseInsensitive)
        buscador.setSourceModel(self.model)
        #aqui le indicamos en que columba de la tabla va a filter cosas segun lo que se escriba
        buscador.setFilterKeyColumn(1)
        #aqui envia la señal que si cambia el texto vaya buscando
        self.LineClaveBusqueda.textChanged.connect(buscador.setFilterRegExp)
        self.tableView.setModel(buscador)





    def retranslateUi(self, BDP):
        _translate = QtCore.QCoreApplication.translate
        BDP.setWindowTitle(_translate("BDP", "Busqueda por descripción"))
        self.label_9.setText(_translate("BDP", "Descripción:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BDP = QtWidgets.QMainWindow()
    ui = Ui_BDP()
    ui.setupUi(BDP)
    BDP.show()
    sys.exit(app.exec_())
