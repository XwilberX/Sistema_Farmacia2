from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHeaderView, QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from sqlalchemy import create_engine
from sqlalchemy.sql import func
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import extract  
from datetime import datetime
import sys
sys.path.append('../Modelo/')
from farm import Clave, Farmaco, Entrada, Historial, Salida
import pandas as pd
from functools import partial

engine = create_engine('mysql+pymysql://root:@localhost/farmaciaDB')
Session = sessionmaker(bind=engine)
session = Session()

class Ui_VtnES(object):
    def __init__(self, EnOsal):
        print('el mensaje es :' + str(EnOsal))
        self.EnOsal = EnOsal
    def setupUi(self, VtnES):
        VtnES.setObjectName("VtnES")
        VtnES.resize(670, 635)
        #VtnES.setMinimumSize(QtCore.QSize(1012, 635))
        #VtnES.setMaximumSize(QtCore.QSize(1012, 635))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagenes/referencias.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VtnES.setWindowIcon(icon)
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
        self.tableViewReferencia.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableViewReferencia.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableViewReferencia.setObjectName("tableViewReferencia")
        self.tableWidgetReferencia = QtWidgets.QTableWidget(VtnES)
        self.tableWidgetReferencia.setGeometry(QtCore.QRect(0, 0, 1011, 311))
        self.tableWidgetReferencia.setObjectName("tableWidgetReferencia")
        self.tableWidgetReferencia.setColumnCount(0)
        self.tableWidgetReferencia.setRowCount(0)
        self.btnActualizarReferencia = QtWidgets.QPushButton(VtnES)
        self.btnActualizarReferencia.setGeometry(QtCore.QRect(160, 320, 51, 51))
        self.btnActualizarReferencia.setStyleSheet("QPushButton{\n"
"border-radius:5px;\n"
"background:#ffc001;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background:#dea806;\n"
"}\n"
"")
        self.btnActualizarReferencia.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagenes/actualizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnActualizarReferencia.setIcon(icon)
        self.btnActualizarReferencia.setIconSize(QtCore.QSize(45, 45))
        self.btnActualizarReferencia.setObjectName("btnActualizarReferencia")
        self.btnPDF = QtWidgets.QPushButton(VtnES)
        self.btnPDF.setGeometry(QtCore.QRect(90, 320, 51, 51))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagenes/pdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPDF.setIcon(icon1)
        self.btnPDF.setIconSize(QtCore.QSize(45, 45))
        self.btnPDF.setObjectName("btnPDF")
        self.btnAtras = QtWidgets.QPushButton(VtnES)
        self.btnAtras.setGeometry(QtCore.QRect(20, 320, 51, 51))
        self.btnAtras.setStyleSheet("QPushButton{\n"
"border-radius:5px;\n"
"background:#ffc001;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background:#dea806;\n"
"}\n"
"")
        self.btnAtras.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../imagenes/atras.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAtras.setIcon(icon2)
        self.btnAtras.setIconSize(QtCore.QSize(45, 45))
        self.btnAtras.setObjectName("btnAtras")
        self.btnBorrarItemView = QtWidgets.QPushButton(VtnES)
        self.btnBorrarItemView.setGeometry(QtCore.QRect(600, 70, 51, 51))
        self.btnBorrarItemView.setStyleSheet("QPushButton{\n"
"border-radius:5px;\n"
"background:#ffc001;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background:#dea806;\n"
"}\n"
"")
        self.btnBorrarItemView.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../imagenes/ic_delete_128_28267.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBorrarItemView.setIcon(icon3)
        self.btnBorrarItemView.setIconSize(QtCore.QSize(45, 45))
        self.btnBorrarItemView.setObjectName("btnBorrarItemView")

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

        ##
        self.btnBorrarItemView.clicked.connect(self.borrarEntrada)
        ##
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

        self.change = partial(self.showTableW, vtn)
        back = partial(self.back, vtn)

        # aqui en el evento dobleclick del tablewidget enviamos una de esas variables
        self.tableViewReferencia.doubleClicked.connect(self.change)

        # si ya esta en la consulta de los farmacos y da click oculta y muestra
        self.btnAtras.clicked.connect(back)
        
        if self.tableWidgetReferencia.isVisible():
            VtnES.resize(900,500)

        
        # al dar click en actualizar si algo se a modificado o borrado
        self.btnActualizarReferencia.clicked.connect(self.send)
        self.btnActualizarReferencia.clicked.connect(back)

        if self.EnOsal == 0:
            self.radioButtonProveedor.setText("Por Destino")
            self.radioButtonPedido.setText("por N.salida")
            self.radioButtonReferencia.hide()

        self.cantidadQuedaron= list()

    ######################
    def borrarEntrada(self):
        confirmacion = QtWidgets.QMessageBox()
        confirmacion.setIcon(QtWidgets.QMessageBox.Information)
        if self.EnOsal == 1:
            confirmacion.setText("Esta seguro que desea eliminar esta entrada?")
        else:
            confirmacion.setText("Esta seguro que desea eliminar esta salida? De esta manera las salidas eliminadas no seran agregadas nuevamente al inventario")
        confirmacion.setWindowTitle("Aviso")
        confirmacion.setStandardButtons(QtWidgets.QMessageBox.Yes| QtWidgets.QMessageBox.No)
        decision = confirmacion.exec()
        if decision == QtWidgets.QMessageBox.Yes:
            filaAzul = self.tableViewReferencia.currentIndex().row()
            numeroE = int(self.tableViewReferencia.model().index(filaAzul,0).data())
            #obtenemos la entrada seleccionada y lo eliminamos
            if self.EnOsal == 1:
                bdFilaEntrada = session.query(Entrada).get(numeroE)
                #obtenemos el ID de historial de todas aquellos que tengan el mismo numero de entrada o salida
                bdFilaEntrada2 = session.query(Historial.idFarmaco).filter(Historial.Entrada_NoEntrada == numeroE).all()
                #eliminamos los ID que tenian el mismo numero de entrada (se eliminan de farmaco) bdFilaEntrada2 con tiene esos id , cuando se agrega un item tinen el mismo ID
                for a in bdFilaEntrada2:
                    for i in a:
                        bdFilaEntrada4 = session.query(Farmaco).filter(Farmaco.idFarmaco == i).delete()
                #se eliminar los datos que tienen el mismo numero de entrada de HISTORIAL
                bdFilaEntrada3 = session.query(Historial).filter(Historial.Entrada_NoEntrada == numeroE).delete()
                #aqui se elimina lo de bdFilaEntrada
                session.delete(bdFilaEntrada)
                session.commit()
            else:
                bdFilaSalida = session.query(Salida).filter(Salida.numero_pedido== numeroE).delete()
                


        


    def fillTableView(self):
        # checando si el radiobuttontodas esta seleccionada
        if self.radioButtonTodas.isChecked() == True:
            #self.query = pd.read_sql('SELECT * FROM entrada', engine)
            if self.EnOsal==1:
                self.query = session.query(Entrada.NoEntrada,Entrada.NoReferencia,Entrada.FeReferencia,Entrada.FeEntrada,Entrada.origen).all()
            else:
                self.query = session.query(Salida.numero_pedido,Salida.FechaPedido,Salida.fechaEntrega,Salida.area).group_by(Salida.numero_pedido).all()
                   
        if self.radioButtonMes.isChecked() == True:
            mesActual = datetime.today().month
            if self.EnOsal==1:            
                self.query = session.query(Entrada.NoEntrada,Entrada.NoReferencia,Entrada.FeReferencia,Entrada.FeEntrada,Entrada.origen).filter(extract('month', Entrada.FeEntrada)==mesActual).all()
            else:
                
                self.query = session.query(Salida.numero_pedido,Salida.FechaPedido,Salida.fechaEntrega,Salida.area).group_by(Salida.numero_pedido).filter(extract('month', Salida.FechaPedido)==mesActual).all()        
                print(self.query)
        if self.EnOsal==1: 
            self.model = QStandardItemModel(len(self.query), 5)
            self.model.setHorizontalHeaderLabels(['NumEntrada', 'NumReferencia', 'Fe-Referencia', 'Fe-Entrada', 'Proveedor'])
        else:
            self.model = QStandardItemModel(len(self.query), 4)
            self.model.setHorizontalHeaderLabels(['NumSalida', 'Fe-Pedido', 'Fe-Entrega', 'Destino'])
            

        self.tableViewReferencia.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for row,z in enumerate(self.query):
            for col,m in enumerate(z):
                item = QStandardItem(str(m))
                self.model.setItem(row, col, item)
                
        self.buscador = QSortFilterProxyModel()
        self.buscador.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.buscador.setSourceModel(self.model)
        # cambio el tipo de busqueda que indique el radio button

        if self.EnOsal==1: 
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
        else:
            if self.radioButtonPedido.isChecked():
                self.buscador.setFilterKeyColumn(0)
                self.lineEdit.textChanged.connect(self.buscador.setFilterRegExp)
            if self.radioButtonProveedor.isChecked():
                self.buscador.setFilterKeyColumn(3)
                self.lineEdit.textChanged.connect(self.buscador.setFilterRegExp)
            self.tableViewReferencia.setModel(self.buscador)


    def showTableW(self, VtnES):

        # ocultando algunos widgets
        if self.tableViewReferencia.isVisible():
            self.radioButtonTodas.hide()
            self.radioButtonMes.hide()
            self.frame.hide()
            self.tableViewReferencia.hide()
            self.btnBorrarItemView.hide()
        # Cambiando tamaño de la ventana
        VtnES.resize(1011, 380)
        if self.EnOsal==1:
            indexTableview = self.tableViewReferencia.currentIndex().row()
            NEntrada = self.tableViewReferencia.model().index(indexTableview, 0).data()
        # Consulta
            self.query = session.query(Historial.clave_corta, Clave.descripcion, Clave.presentacion, Historial.cantidad,
                                   Historial.lote,
                                   Historial.area, Historial.idFarmaco).join(Clave).filter(and_(Historial.clave_corta == Clave.corta, Historial.Entrada_NoEntrada == NEntrada))
            self.tableWidgetReferencia.setColumnCount(8)
            self.tableWidgetReferencia.setHorizontalHeaderLabels(['Eliminar','Clave', 'Descripción', 'Presentación', 'Cantidad', 'Lote', 'Resguardo', 'id'])
            self.tableWidgetReferencia.setColumnHidden(7, True)
        else:
            indexTableview = self.tableViewReferencia.currentIndex().row()
            NSalida = self.tableViewReferencia.model().index(indexTableview, 0).data()
        # Consulta
            self.query = session.query(Salida.clave_corta,Clave.descripcion,Clave.presentacion,Salida.cantidadSal,
                                    Salida.lote,
                                    Salida.area,Salida.idSalida).join(Clave).filter(and_(Salida.clave_corta == Clave.corta, Salida.numero_pedido == NSalida))
            self.tableWidgetReferencia.setColumnCount(8)
            self.tableWidgetReferencia.setHorizontalHeaderLabels(['Eliminar','Clave', 'Descripción', 'Presentación', 'Cantidad', 'Lote', 'Destino', 'id'])
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
        self.cantidads=list()
        # llenando lista con ids que entrar de la consulta
        for i in range(self.tableWidgetReferencia.rowCount()):
            self.ids.append(int(self.tableWidgetReferencia.item(i,7).text()))
            self.cantidads.append(int(self.tableWidgetReferencia.cellWidget(i,4).value()))
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
        self.cantidadQuedaron.append(self.cantidads[rowC])
        self.cantidads.pop(rowC)
        



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
        self.btnBorrarItemView.show()
        self.fillTableView()


    def send(self):

        rows = self.tableWidgetReferencia.rowCount()
        self.idsNow = list()
        self.cantidadNow = list()
        # llenando una lista con los ids de los farmacos que sigan estando en la tabla
        for i in range(rows):
            self.idsNow.append(int(self.tableWidgetReferencia.item(i,7).text()))
            self.cantidadNow.append(int(self.tableWidgetReferencia.cellWidget(i,4).value()))
        # lista que contiene los ids de los farmacos que se an eliminado en caso de no a ver eliminado nada
        # estara vacio
        self.idsRes =  list(set(self.ids) - set(self.idsNow))
        self.cantidadRes = list(set(self.cantidads)-set(self.cantidadNow))
        # for para eliminaciones si asi se a hecho, para tabla farmaco e historial de la base de datos
        for inx, value in enumerate(self.idsRes):

            if self.EnOsal==1:
                session.query(Historial).filter(Historial.idFarmaco == value).delete()
                session.query(Farmaco).filter(Farmaco.idFarmaco == value).delete()               
            else:
                #si el articulo ya no existe de la bd
                a = session.query(Salida).filter(Salida.idSalida == value).scalar()
                b = session.query(Historial).filter(Historial.idFarmaco == a.idFarmaco).scalar()
                if session.query(Farmaco).filter(Farmaco.idFarmaco == a.idFarmaco).scalar() == None:
                    d = Farmaco(idFarmaco=b.idFarmaco,lote=b.lote,cantidad=a.cantidadSal,caducidad=b.caducidad,area=b.area,origen=b.origen,fechaIngreso=b.fechaIngreso,clave_corta=b.clave_corta)
                    session.add(d)
                    session.flush()
                if session.query(Farmaco).filter(Farmaco.idFarmaco == a.idFarmaco).scalar():
                    c = session.query(Farmaco).filter(Farmaco.idFarmaco == a.idFarmaco).scalar()
                    c.cantidad = c.cantidad + self.cantidadQuedaron[inx]
                    session.commit()
                a = session.query(Salida).filter(Salida.idSalida == value).delete()

            
                


        session.commit()
        # for para actualizar cantidades de farmacos si es que se han y aun que no xd
        for i in range(self.tableWidgetReferencia.rowCount()):
            if self.EnOsal==1:
                value = int(self.tableWidgetReferencia.cellWidget(i, 4).value())
                queryUpdate = session.query(Historial).get(self.idsNow[i])
                queryUpdate2 = session.query(Farmaco).get(self.idsNow[i])
                if queryUpdate2.cantidad < 0 or queryUpdate.cantidad  < 0:
                    confirmacion = QtWidgets.QMessageBox()
                    confirmacion.setIcon(QtWidgets.QMessageBox.Information)
                    confirmacion.setText("Una cantidad supera su total:"+str(value)+" Solo se realizaron los cambios de los articulos  arriba de esta")
                    confirmacion.setWindowTitle("Aviso")
                    decision = confirmacion.exec()
                    break
                queryUpdate2.cantidad = value
                queryUpdate.cantidad = value
                session.commit()
            else:
                value = int(self.tableWidgetReferencia.cellWidget(i, 4).value())
                print(value)
                queryUpdate = session.query(Salida).get(self.idsNow[i])
                
                session.commit()
                ##########
                queryUpdate2 = session.query(Farmaco).filter(Farmaco.idFarmaco==queryUpdate.idFarmaco).scalar()
                print(self.cantidadNow)
                cantidad_nueva = value - self.cantidads[i]
                if cantidad_nueva > 0:
                    queryUpdate2.cantidad = queryUpdate2.cantidad - cantidad_nueva
                    loquequedo = queryUpdate2.cantidad
                    if loquequedo < 0:
                        confirmacion = QtWidgets.QMessageBox()
                        confirmacion.setIcon(QtWidgets.QMessageBox.Information)
                        confirmacion.setText("Una cantidad supera su total:"+str(value)+" Solo se realizaron los cambios de los articulos  arriba de esta")
                        confirmacion.setWindowTitle("Aviso")
                        decision = confirmacion.exec()
                        break
                    if loquequedo == 0 :
                        session.delete(queryUpdate2)
                    queryUpdate.cantidadSal = value
                    session.commit()
                else:
                    queryUpdate2.cantidad = queryUpdate2.cantidad + abs(cantidad_nueva)
                    session.commit()
        self.ids[:] = []
        self.idsNow[:] = []
        self.idsRes[:] = []
        self.cantidads[:] = []
        self.cantidadNow[:] = []
        self.cantidadRes[:] = []
        self.cantidadQuedaron[:] = []
                    

               



    def retranslateUi(self, VtnES):
        _translate = QtCore.QCoreApplication.translate
        VtnES.setWindowTitle(_translate("VtnES", "Referencias"))
        self.radioButtonTodas.setText(_translate("VtnES", "Todas"))
        self.radioButtonMes.setText(_translate("VtnES", "Mes"))
        self.radioButtonReferencia.setText(_translate("VtnES", "Por referencia"))
        self.radioButtonProveedor.setText(_translate("VtnES", "Por Proveedor"))
        self.radioButtonPedido.setText(_translate("VtnES", "Por N.Entrada"))
        self.btnActualizarReferencia.setToolTip(_translate("VtnES", "Actualizar"))
        self.btnActualizarReferencia.setShortcut(_translate("VtnES", "Ctrl+A"))
        self.btnPDF.setToolTip(_translate("VtnES", "Generar PDF"))
        self.btnPDF.setShortcut(_translate("VtnES", "Ctrl+P"))
        self.btnAtras.setToolTip(_translate("VtnES", "Regresar"))
        self.btnBorrarItemView.setToolTip(_translate("VtnES", "Borrar una entrada completa"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VtnES = QtWidgets.QWidget()
    ui = Ui_VtnES()
    ui.setupUi(VtnES)
    VtnES.show()
    sys.exit(app.exec_())
