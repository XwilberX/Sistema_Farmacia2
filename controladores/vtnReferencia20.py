# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnReferencia2.0.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHeaderView, QWidget
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from sqlalchemy import create_engine
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker, relationship
import sys
sys.path.append('../Modelo/')
from farm import Clave, Farmaco, Entrada, Historial
import pandas as pd

engine = create_engine('mysql+pymysql://root:wil99@localhost/farmaciaDB')
Session = sessionmaker(bind=engine)
session = Session()

class Ui_VtnES(QWidget):
    def setupUi(self, VtnES):
        VtnES.setObjectName("VtnES")
        VtnES.resize(670, 635)
        # VtnES.setMinimumSize(QtCore.QSize(500, 635))
        # VtnES.setMaximumSize(QtCore.QSize(1012, 635))
        VtnES.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size: 12px;\n"
"}\n"
"#VtnES{\n"
"background: #b8f4f0;\n"
"}\n"
"QLineEdit{\n"
"    border:none;\n"
"    border-bottom: 1px solid black;\n"
"}\n"
"")
        self.radioButtonTodas = QtWidgets.QRadioButton(VtnES)
        self.radioButtonTodas.setGeometry(QtCore.QRect(600, 10, 61, 17))
        self.radioButtonTodas.setObjectName("radioButtonTodas")
        self.radioButtonMes = QtWidgets.QRadioButton(VtnES)
        self.radioButtonMes.setGeometry(QtCore.QRect(600, 40, 51, 17))
        self.radioButtonMes.setObjectName("radioButtonMes")
        self.frame = QtWidgets.QFrame(VtnES)
        self.frame.setGeometry(QtCore.QRect(10, 560, 571, 61))
        self.frame.setStyleSheet("\n"
"QFrame{\n"
"border-radius: 25px;\n"
" background:#fefefe;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.radioButtonReferencia = QtWidgets.QRadioButton(self.frame)
        self.radioButtonReferencia.setGeometry(QtCore.QRect(220, 10, 111, 20))
        self.radioButtonReferencia.setObjectName("radioButtonReferencia")
        self.radioButtonProveedor = QtWidgets.QRadioButton(self.frame)
        self.radioButtonProveedor.setGeometry(QtCore.QRect(350, 10, 111, 17))
        self.radioButtonProveedor.setObjectName("radioButtonProveedor")
        self.radioButtonPedido = QtWidgets.QRadioButton(self.frame)
        self.radioButtonPedido.setGeometry(QtCore.QRect(90, 10, 101, 21))
        self.radioButtonPedido.setStyleSheet("")
        self.radioButtonPedido.setObjectName("radioButtonPedido")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(90, 30, 371, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.dateEdit = QtWidgets.QDateEdit(VtnES)
        self.dateEdit.setGeometry(QtCore.QRect(1130, 70, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.spinBox = QtWidgets.QSpinBox(VtnES)
        self.spinBox.setGeometry(QtCore.QRect(1270, 70, 42, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10000)
        self.spinBox.setObjectName("spinBox")
        self.tableViewReferencia = QtWidgets.QTableView(VtnES)
        self.tableViewReferencia.setGeometry(QtCore.QRect(0, 0, 591, 551))
        self.tableViewReferencia.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableViewReferencia.setObjectName("tableViewReferencia")
        self.tableWidgetReferencia = QtWidgets.QTableWidget(VtnES)
        self.tableWidgetReferencia.setGeometry(QtCore.QRect(0, 0, 1011, 311))
        self.tableWidgetReferencia.setObjectName("tableWidgetReferencia")
        self.tableWidgetReferencia.setColumnCount(0)
        self.tableWidgetReferencia.setRowCount(0)
        self.btnActualizarReferencia = QtWidgets.QPushButton(VtnES)
        self.btnActualizarReferencia.setGeometry(QtCore.QRect(10, 330, 131, 31))
        self.btnActualizarReferencia.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background:#ffc001;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background:#dea806;\n"
"}\n"
"")
        self.btnActualizarReferencia.setObjectName("btnActualizarReferencia")
        self.btnPDF = QtWidgets.QPushButton(VtnES)
        self.btnPDF.setGeometry(QtCore.QRect(150, 320, 51, 51))
        self.btnPDF.setStyleSheet("QPushButton{\n"
"border-radius:5px;\n"
"background:#ffc001;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background:#dea806;\n"
"}\n"
"")
        self.btnPDF.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagenes/pdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPDF.setIcon(icon)
        self.btnPDF.setIconSize(QtCore.QSize(45, 45))
        self.btnPDF.setObjectName("btnPDF")

        self.retranslateUi(VtnES)
        QtCore.QMetaObject.connectSlotsByName(VtnES)
        VtnES.setTabOrder(self.radioButtonPedido, self.radioButtonReferencia)
        VtnES.setTabOrder(self.radioButtonReferencia, self.radioButtonProveedor)
        VtnES.setTabOrder(self.radioButtonProveedor, self.lineEdit)
        VtnES.setTabOrder(self.lineEdit, self.tableViewReferencia)
        VtnES.setTabOrder(self.tableViewReferencia, self.tableWidgetReferencia)
        VtnES.setTabOrder(self.tableWidgetReferencia, self.btnActualizarReferencia)
        VtnES.setTabOrder(self.btnActualizarReferencia, self.btnPDF)
        VtnES.setTabOrder(self.btnPDF, self.spinBox)
        VtnES.setTabOrder(self.spinBox, self.dateEdit)
        VtnES.setTabOrder(self.dateEdit, self.radioButtonMes)
        VtnES.setTabOrder(self.radioButtonMes, self.radioButtonTodas)
        self.btnPDF.hide()
        self.btnActualizarReferencia.hide()
        self.tableWidgetReferencia.hide()

        self.radioButtonTodas.setChecked(True)
        self.radioButtonPedido.setChecked(True)
        self.radioButtonPedido.toggled.connect(self.fillTableView)
        self.radioButtonReferencia.toggled.connect(self.fillTableView)
        self.radioButtonProveedor.toggled.connect(self.fillTableView)
        self.fillTableView()

        self.tableViewReferencia.doubleClicked.connect(self.showTableW)

    def fillTableView(self):
        if self.radioButtonTodas.isChecked() == True:
            self.query = pd.read_sql('SELECT * FROM entrada', engine)
            self.model = QStandardItemModel(self.query.shape[0], self.query.shape[1])
            self.model.setHorizontalHeaderLabels(['NumEntrada', 'NumReferencia', 'Fe-Referencia', 'Fe-Entrada', 'Proveedor'])
            self.tableViewReferencia.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            for z in range(self.query.shape[0]):
                for m in range(self.query.shape[1]):
                    item = QStandardItem(str(self.query.iloc[z, m]))
                    self.model.setItem(z, m, item)
            self.buscador = QSortFilterProxyModel()
            self.buscador.setFilterCaseSensitivity(Qt.CaseInsensitive)
            self.buscador.setSourceModel(self.model)

            if self.radioButtonPedido.isChecked():
                self.buscador.setFilterKeyColumn(0)
                self.lineEdit.textChanged.connect(self.buscador.setFilterRegExp)
            if self.radioButtonReferencia.isChecked():
                self.buscador.setFilterKeyColumn(1)
                self.lineEdit.textChanged.connect(self.buscador.setFilterRegExp)
            if self.radioButtonProveedor.isChecked():
                self.buscador.setFilterKeyColumn(4)
                self.lineEdit.textChanged.connect(self.buscador.setFilterRegExp)
            self.tableViewReferencia.setModel(self.buscador)

    def showTableW(self):
        indexTableview = self.tableViewReferencia.currentIndex().row()
        NReferencia = self.tableViewReferencia.model().index(indexTableview,0).data()
        print(NReferencia)
        self.tableViewReferencia.hide()

    def retranslateUi(self, VtnES):
        _translate = QtCore.QCoreApplication.translate
        VtnES.setWindowTitle(_translate("VtnES", "Form"))
        self.radioButtonTodas.setText(_translate("VtnES", "Todas"))
        self.radioButtonMes.setText(_translate("VtnES", "Mes"))
        self.radioButtonReferencia.setText(_translate("VtnES", "Por referencia"))
        self.radioButtonProveedor.setText(_translate("VtnES", "Por Proveedor"))
        self.radioButtonPedido.setText(_translate("VtnES", "Por pedido"))
        self.btnActualizarReferencia.setText(_translate("VtnES", "Actualizar"))
        self.btnActualizarReferencia.setShortcut(_translate("VtnES", "Ctrl+A"))
        self.btnPDF.setShortcut(_translate("VtnES", "Ctrl+P"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VtnES = QtWidgets.QWidget()
    ui = Ui_VtnES()
    ui.setupUi(VtnES)
    VtnES.show()
    sys.exit(app.exec_())
