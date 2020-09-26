# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnReferencia2.0.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHeaderView, QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from sqlalchemy import create_engine
from sqlalchemy.sql import func
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker, relationship
import sys
sys.path.append('../Modelo/')
from farm import Clave, Farmaco, Entrada, Historial
import pandas as pd
from functools import partial

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
        self.btnAtras = QtWidgets.QPushButton(VtnES)
        self.btnAtras.setGeometry(QtCore.QRect(860, 330, 131, 31))
        self.btnAtras.setText("Regresar")
        self.btnAtras.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background:#ffc001;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background:#dea806;\n"
"}\n"
"")
        self.btnAtras.setToolTip("Regresa a la ventana anterior")
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
        VtnES.setTabOrder(self.radioButtonMes, self.radioButtonTodas)
        # Ocultando cosas que tiene que ver cuando aun no se da doble click en el tableview
        self.btnAtras.hide()
        self.btnPDF.hide()
        self.btnActualizarReferencia.hide()
        self.tableWidgetReferencia.hide()
        # indicamos que cuando de click en una celda se selecione toda su fila
        self.tableViewReferencia.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

        self.radioButtonTodas.setChecked(True)
        self.radioButtonPedido.setChecked(True)
        # enviamos un señal de cuando algun radiobutton este selecionado ala funcion fillTableView
        self.radioButtonMes.toggled.connect(self.fillTableView)
        self.radioButtonPedido.toggled.connect(self.fillTableView)
        self.radioButtonReferencia.toggled.connect(self.fillTableView)
        self.radioButtonProveedor.toggled.connect(self.fillTableView)
        self.fillTableView()

        # guardando en una variable el un objeto de tipo widgget
        vtn = VtnES

        # preparamos un variable que sirve para enviar argumentos a un funcion
        change = partial(self.showTableW, vtn)
        back = partial(self.back, vtn).

        # aqui en el evento dobleclick del tablewidget enviamos una de esas variables
        self.tableViewReferencia.doubleClicked.connect(change)

        # si ya esta en la consulta de los farmacos y da click oculta y muestra
        self.btnAtras.clicked.connect(back)

        # al dar click en actualizar si algo se a modificado o borrado
        self.btnActualizarReferencia.clicked.connect(self.send)

# Funciones.
    # Funcion de llenado de tableview y actualiza segun el tipo de busqueda
    def fillTableView(self):
        # checando si el radiobuttontodas esta seleccionada
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

            # cambio el tipo de busqueda que indique el radio button
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

    # funcion que entra cuando ya se dio dobleclick en el tableview y muestra el tablewidget
    def showTableW(self, VtnES):
        indexTableview = self.tableViewReferencia.currentIndex().row()
        NEntrada = self.tableViewReferencia.model().index(indexTableview, 0).data()
        # ocultando algunos widgets
        if self.tableViewReferencia.isVisible():
            self.radioButtonTodas.hide()
            self.radioButtonMes.hide()
            self.frame.hide()
            self.tableViewReferencia.hide()
        # Cambiando tamaño de la ventana
        VtnES.resize(1011, 380)
        # Consulta
        self.query = session.query(Historial.clave_corta, Clave.descripcion, Clave.presentacion, Historial.cantidad,
                                   Historial.lote,
                                   Historial.area, Historial.idFarmaco).join(Clave).filter(and_(Historial.clave_corta == Clave.corta, Historial.Entrada_NoEntrada == NEntrada))

        self.tableWidgetReferencia.setColumnCount(8)
        self.tableWidgetReferencia.setHorizontalHeaderLabels(['Eliminar','Clave', 'Descripción', 'Presentación', 'Cantidad', 'Lote', 'Resguardo', 'id'])
        self.tableWidgetReferencia.setColumnHidden(7, True)
        self.tableWidgetReferencia.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidgetReferencia.setRowCount(self.query.count())

        # ciclos para llenar la tabla segun lo que corresponda
        for row, i in enumerate(self.query):
            for col, j in enumerate(i):
                #Agregando el boton para eliminar fila
                if col == 0:
                    self.BtnDelete(VtnES)
                    self.tableWidgetReferencia.setCellWidget(row, col, self.btnDelete)
                    self.btnDelete.clicked.connect(self.deleteRowWi)
                    self.tableWidgetReferencia.setItem(row, col + 1, QTableWidgetItem(str(j)))
                # Agregando un spinbox en la columna de cnatidades
                if col == 3:
                    self.createSpinBox(int(j), VtnES)
                    self.tableWidgetReferencia.setCellWidget(row, col + 1, self.spinBox)
                if col != 0 and col != 3 :
                    item = QTableWidgetItem(str(j))
                    if col == 1:
                        item.setToolTip(str(j))
                    if col == 2:
                        item.setToolTip(str(j))
                    self.tableWidgetReferencia.setItem(row, col + 1, item)
        self.ids = list()
        # llenando lista con ids que entrar de la consulta
        for i in range(self.tableWidgetReferencia.rowCount()):
            self.ids.append(int(self.tableWidgetReferencia.item(i,7).text()))
        if not self.tableViewReferencia.isVisible():
            self.tableWidgetReferencia.show()
            self.btnAtras.show()
            self.btnPDF.show()
            self.btnActualizarReferencia.show()
            self.tableWidgetReferencia.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    # funcion para eliminar una fila
    def deleteRowWi(self):
        rowC = self.tableWidgetReferencia.currentRow()
        self.tableWidgetReferencia.removeRow(rowC)

    # funcion de creacion de boton delete y ser agregado con un widget
    def BtnDelete(self, VtnES):
        self.btnDelete = QtWidgets.QPushButton(VtnES)
        self.btnDelete.setGeometry(QtCore.QRect(320, 20, 21, 21))
        ################################################################################ SE CREO MANUAL
        IconoDelete = QtGui.QIcon()
        IconoDelete.addPixmap(QtGui.QPixmap("../imagenes/ic_delete_128_28267.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDelete.setIcon(IconoDelete)
        self.btnDelete.setStyleSheet("QPushButton{\n"
                                     "border-radius:15px;\n"
                                     "background:#fefefe;\n"
                                     "\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background:#dea806;\n"
                                     "}\n"
                                     "")

    # funcion de creacion de un spinbox y ser agregado con un widget
    def createSpinBox(self, j, VtnES):
        self.spinBox = QtWidgets.QSpinBox(VtnES)
        self.spinBox.setGeometry(QtCore.QRect(1270, 70, 42, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10000)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setValue(j)

    # culta los elementos que aparecen despues del dobleclick
    def back(self, VtnES):
        self.btnAtras.hide()
        self.btnPDF.hide()
        self.btnActualizarReferencia.hide()
        self.tableWidgetReferencia.hide()
        VtnES.resize(670, 635)
        self.radioButtonTodas.show()
        self.radioButtonMes.show()
        self.frame.show()
        self.tableViewReferencia.show()

    def send(self):
        rows = self.tableWidgetReferencia.rowCount()
        self.idsNow = list()
        # llenando una lista con los ids de los farmacos que sigan estando en la tabla
        for i in range(rows):
            self.idsNow.append(int(self.tableWidgetReferencia.item(i,7).text()))
        # lista que contiene los ids de los farmacos que se an eliminado en caso de no a ver eliminado nada
        # estara vacio
        self.idsRes =  list(set(self.ids) - set(self.idsNow))
        # for para eliminaciones si asi se a hecho, para tabla farmaco e historial de la base de datos
        for inx, value in enumerate(self.idsRes):
            session.query(Historial).filter(Historial.idFarmaco == value).delete()
            session.query(Farmaco).filter(Farmaco.idFarmaco == value).delete()
            session.commit()
        # for para actualizar cantidades de farmacos si es que se han y aun que no xd
        for i in range(self.tableWidgetReferencia.rowCount()):
            value = int(self.tableWidgetReferencia.cellWidget(i, 4).value())
            queryUpdate = session.query(Historial).get(self.idsNow[i])
            queryUpdate2 = session.query(Farmaco).get(self.idsNow[i])
            queryUpdate2.cantidad = value
            queryUpdate.cantidad = value
            session.commit()

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
    ui.showTableW(VtnES)
    VtnES.show()
    sys.exit(app.exec_())
