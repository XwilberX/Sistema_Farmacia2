from PyQt5.QtWidgets import QMdiSubWindow, QMainWindow, QWidget, QPushButton,QTableView,QHeaderView,QTableWidgetItem
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIntValidator, QPainter, QColor, QPen
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func
from vtnCantidad import Ui_vtnCantidad
from vtnReferencia import Ui_VtnES
from vtnObservaciones import Ui_Observaciones
import sys
sys.path.append('../Modelo/')
from farm import Salida
from farm import Clave
from farm import Farmaco
import pandas as pd
from reports import Report as reportes
import pymysql

engine = create_engine('mysql+pymysql://root:wil99@localhost/farmaciaDB')
Session = sessionmaker(bind=engine)
session = Session()


class SubWindow(QWidget):
    def createSubWindow(self):
        parent = None
        super(SubWindow, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setObjectName("InterFazSalida")
        self.resize(1051, 721)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagenes/medicina.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size: 12px;\n"
"}\n"
"#Frame2{\n"
"border-radius:30;\n"
"}\n"
"QLineEdit{\n"
"    border:none;\n"
"    border-bottom: 1px solid black;\n"
"}\n"
"QFrame{\n"
"border-radius: 60px;\n"
" background:#fefefe;\n"
"}\n"
"QLabel{\n"
"    background:transparent;\n"
"}\n"
"QCalendarWidget QAbstractItemView\n"
"{ \n"
"selection-background-color: #042944; \n"
"selection-color: white;\n"
"selection-border:10px solid red;\n"
"\n"
"}\n"
"QCalendarWidget QWidget \n"
"{\n"
"  color:grey;\n"
"}\n"
"QCalendarWidget QTableView{\n"
"border-width:0px;\n"
"background-color:lightgrey;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:#dea806;\n"
"}")
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setGeometry(QtCore.QRect(40, 110, 961, 560))
        self.frame_2.setStyleSheet("\n"
" background:#fefefe;\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 81, 21))
        self.label_8.setObjectName("label_8")
        self.LineClaveSalida = QtWidgets.QLineEdit(self.frame_2)
        self.LineClaveSalida.setGeometry(QtCore.QRect(80, 20, 191, 31))
        self.LineClaveSalida.setObjectName("LineClaveSalida")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(290, 20, 91, 21))
        self.label_9.setObjectName("label_9")
        self.btnFinalizarSalida = QtWidgets.QPushButton(self.frame_2)
        self.btnFinalizarSalida.setGeometry(QtCore.QRect(780, 520, 141, 31))
        self.btnFinalizarSalida.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background:#ffc001;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background:#dea806;\n"
"}\n"
"")
        self.btnFinalizarSalida.setObjectName("btnFinalizarSalida")
        self.TableSalida = QtWidgets.QTableWidget(self.frame_2)
        self.TableSalida.setGeometry(QtCore.QRect(10, 280, 941, 230))
        self.TableSalida.setObjectName("TableSalida")
        self.TableSalida.setColumnCount(9)
        self.TableSalida.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagenes/ic_delete_128_28267.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.TableSalida.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
        self.TableSalida.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
        self.TableSalida.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
        self.TableSalida.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
        self.TableSalida.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
        self.TableSalida.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
        self.TableSalida.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
        self.TableSalida.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
        self.TableSalida.setHorizontalHeaderItem(8, item)


        #
        # #que la tabla no pueda ser editada
        self.TableSalida.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        #
        #

        self.tableViewSalida = QtWidgets.QTableView(self.frame_2)
        self.tableViewSalida.setGeometry(QtCore.QRect(10, 70, 941, 200))
        self.tableViewSalida.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableViewSalida.setObjectName("tableViewSalida")
        self.LineDescripSalida = QtWidgets.QLineEdit(self.frame_2)
        self.LineDescripSalida.setGeometry(QtCore.QRect(370, 20, 541, 31))
        self.LineDescripSalida.setObjectName("LineDescripSalida")
        self.btnTotalEntradasEntra = QtWidgets.QPushButton(self.frame_2)
        self.btnTotalEntradasEntra.setGeometry(QtCore.QRect(710, 520, 51, 31))
        self.btnTotalEntradasEntra.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background:#ffc001;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background:#dea806;\n"
"}\n"
"")
        self.btnTotalEntradasEntra.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../imagenes/papeleo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnTotalEntradasEntra.setIcon(icon2)
        self.btnTotalEntradasEntra.setIconSize(QtCore.QSize(30, 30))
        self.btnTotalEntradasEntra.setObjectName("btnTotalEntradasEntra")
        self.Frame2 = QtWidgets.QFrame(self)
        self.Frame2.setGeometry(QtCore.QRect(80, 20, 881, 71))
        self.Frame2.setStyleSheet("\n"
" background:#fefefe;\n"
"\n"
"")
        self.Frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame2.setObjectName("Frame2")
        self.label_16 = QtWidgets.QLabel(self.Frame2)
        self.label_16.setGeometry(QtCore.QRect(30, 10, 61, 20))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.Frame2)
        self.label_17.setGeometry(QtCore.QRect(550, 10, 91, 21))
        self.label_17.setObjectName("label_17")
        self.LineControlSalida = QtWidgets.QLineEdit(self.Frame2)
        self.LineControlSalida.setEnabled(False)
        self.LineControlSalida.setGeometry(QtCore.QRect(90, 10, 121, 21))
        self.LineControlSalida.setObjectName("LineControlSalida")
        self.DateFechaPSalida = QtWidgets.QDateEdit(self.Frame2)
        self.DateFechaPSalida.setGeometry(QtCore.QRect(640, 10, 121, 22))
        self.DateFechaPSalida.setAccelerated(False)
        self.DateFechaPSalida.setProperty("showGroupSeparator", False)
        self.DateFechaPSalida.setCalendarPopup(True)
        self.DateFechaPSalida.setTimeSpec(QtCore.Qt.UTC)
        self.DateFechaPSalida.setDate(QtCore.QDate(2020, 1, 1))
        self.DateFechaPSalida.setObjectName("DateFechaPSalida")
        self.label_18 = QtWidgets.QLabel(self.Frame2)
        self.label_18.setGeometry(QtCore.QRect(30, 40, 51, 20))
        self.label_18.setObjectName("label_18")
        self.LineAreaSalida = QtWidgets.QLineEdit(self.Frame2)
        self.LineAreaSalida.setGeometry(QtCore.QRect(90, 40, 121, 21))
        self.LineAreaSalida.setObjectName("LineAreaSalida")
        self.label_19 = QtWidgets.QLabel(self.Frame2)
        self.label_19.setGeometry(QtCore.QRect(550, 40, 91, 21))
        self.label_19.setObjectName("label_19")
        self.DateFechaESalida = QtWidgets.QDateEdit(self.Frame2)
        self.DateFechaESalida.setGeometry(QtCore.QRect(640, 40, 121, 22))
        self.DateFechaESalida.setAccelerated(False)
        self.DateFechaESalida.setProperty("showGroupSeparator", False)
        self.DateFechaESalida.setCalendarPopup(True)
        self.DateFechaESalida.setTimeSpec(QtCore.Qt.UTC)
        self.DateFechaESalida.setDate(QtCore.QDate(2020, 1, 1))
        self.DateFechaESalida.setObjectName("DateFechaESalida")
        self.comboboxSalida = QtWidgets.QComboBox(self.Frame2)
        self.comboboxSalida.setGeometry(QtCore.QRect(350, 20, 151, 22))
        self.comboboxSalida.setObjectName("comboboxSalida")
        self.comboboxSalida.addItem("")
        self.comboboxSalida.addItem("")
        self.label_20 = QtWidgets.QLabel(self.Frame2)
        self.label_20.setGeometry(QtCore.QRect(310, 20, 31, 20))
        self.label_20.setObjectName("label_20")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.LineAreaSalida, self.comboboxSalida)
        self.setTabOrder(self.comboboxSalida, self.DateFechaPSalida)
        self.setTabOrder(self.DateFechaPSalida, self.DateFechaESalida)
        self.setTabOrder(self.DateFechaESalida, self.LineClaveSalida)
        self.setTabOrder(self.LineClaveSalida, self.btnTotalEntradasEntra)
        self.setTabOrder(self.btnTotalEntradasEntra, self.btnFinalizarSalida)
        self.setTabOrder(self.btnFinalizarSalida, self.tableViewSalida)
        self.setTabOrder(self.tableViewSalida, self.TableSalida)
        self.setTabOrder(self.TableSalida, self.LineControlSalida)
        self.setTabOrder(self.LineControlSalida, self.LineDescripSalida)
        self.LineControlSalida.setToolTip('Numero automatico de la salida')
        self.LineAreaSalida.setToolTip('Destino de la salida de los medicamentos o materiales de curación')
        self.comboboxSalida.setToolTip('Eligir medicamento o material de curación')
        self.DateFechaPSalida.setToolTip('Introducir fecha del pedido')
        self.DateFechaESalida.setToolTip('Introducir fecha de la entrada')
        self.LineClaveSalida.setToolTip('Clave del medicamento o matarial de curación')
        self.LineDescripSalida.setToolTip('Descripción del medicamento o material de curación')
        self.btnFinalizarSalida.setToolTip('Se envian los datos para generar reporte y se guardan al bd')

                # self.setTabOrder(self.LineClaveSalida, self.LineDescripSalida)
        # self.setTabOrder(self.LineDescripSalida, self.btnFinalizarSalida)


        #INICIO DEL CODIGO
        now = datetime.now()
        self.DateFechaESalida.setDate(now)
        self.DateFechaPSalida.setDate(now)

        self.NcontrolS()
        self.TableViewInsertSalida()
        self.comboboxSalida.currentIndexChanged.connect(self.TableViewInsertSalida)

        #cuando se le da el click a esto , le otorga los permisos de busqueda

        self.LineDescripSalida.mousePressEvent = self.click
        self.LineClaveSalida.mousePressEvent = self.click
        

        #funcion para enviar los datos a la base de datos y crear el archivo.
        self.btnFinalizarSalida.clicked.connect(self.bdFinalizarSalida)
        self.tableViewSalida.doubleClicked.connect(self.insertDatosTablaWid)
        self.listaId=[]
        self.listaCantidad=[]
        self.listaLote=[]

        self.btnTotalEntradasEntra.clicked.connect(self.openRef)
        self.EnOsal=0



    #mete los datos de la tabla a la base de datos
    def bdFinalizarSalida(self):
        try:
            DfSalida = pd.DataFrame()
            self.DfReport = pd.DataFrame()
            #el func.max es la funcion SELECT MAX de sql (obtiene el dato con mayor valor)
            Npedido = session.query(func.max(Salida.numero_pedido)).scalar()
            if Npedido is None:
                Npedido = 0
            self.Npedidoup = int(Npedido + 1)
            rows = self.TableSalida.rowCount()
            Column = self.TableSalida.columnCount()
            #TUVIMOS QUE ARREGLAR EL ORDEN DE LOS HEADERS PARA QUE JALE LA CONSULTA JUSTO CON LA TABLA DE BD Y EL DATAFRAME
            headers = ['clave_corta', 'cantidadSal', 'Caducidad','FechaPedido','fechaEntrega','area','lote','numero_pedido','idFarmaco']
            for i in range(rows):
                for j in range(Column + 4):
                    # Este If es por que no necesitamos las columnas de descripcion y presentacion en el ingreso al DATAFRAME ya que al ingresar el dataframe a la BD no estan esos campos
                    if j != 3 and j != 4 and j != 0 and j != 9 and j != 10 and j != 11 and j!=1 and j!=12:
                        DfSalida.loc[i, j] = self.TableSalida.item(i, j).text()
                    if j == 9:
                        DfSalida.loc[i, j] = self.LineAreaSalida.text()
                    if j == 10:
                        DfSalida.loc[i, j] = self.listaLote[i]
                    if j == 11:
                        DfSalida.loc[i, j] = self.Npedidoup
                    if j == 12:
                        DfSalida.loc[i, j] = self.listaId[i]

            DfSalida.columns = headers
            #print(DfSalida)
            #Ingreso DEl dataframe a la bd tipo ingreso pandas(NO SQLALCHEMY)
            DfSalida.to_sql('salida', engine, index= False, if_exists="append")
            #ciclo para que vaya ejecutando el update de cada uno de ellos 
            self.listaCantidad
            rango = len(self.listaId)
            for i in range(rango):
                idd = self.listaId[i]
                #obtengo todos los datos de ese ID y actualizo el de cantidad - la cantidad que se resta
                QueryUpdate = session.query(Farmaco).get(idd)
                QueryUpdate.cantidad = QueryUpdate.cantidad - int(self.listaCantidad[i])
                loquequedo = QueryUpdate.cantidad
                if loquequedo == 0 :
                    session.delete(QueryUpdate)

                #para que se realice el cambio
                session.commit()
                session.close()
                
            #aqui abrimos la ventana de observaciones
            self.vtnObserv = QtWidgets.QWidget()
            self.uiObser = Ui_Observaciones()
            self.uiObser.setupUi(self.vtnObserv)
            self.vtnObserv.show()
            self.uiObser.btnAceptarObservaciones.clicked.connect(self.observaciones)

            
            #receteamos el numero de control para que no exista problemas
            self.NcontrolS()
            #limpiamos la lista para que no contenga un ID y acepte todos nuevamente
            self.listaId[:] = [] 
            self.listaCantidad[:] = [] 
            # self.listaLote[:] =[]
            self.TableViewInsertSalida()
        except Exception as e:
            print(e)
            self.LineAreaSalida.setFocus()
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
            error_dialog.setText("No hay datos en la tabla")
            error_dialog.setWindowTitle("Error")
            error_dialog.exec()


    def EnvioReport(self):
        # mandando datos para generar reportes
        datarow = ['Clave', 'Descripción', 'Presentación', 'Cantidad', 'Caducidad', 'Lote']
        dataall = list()
        dataall.append(datarow)
        for row in range(self.TableSalida.rowCount()):
            datarow = []
            for column in range(self.TableSalida.columnCount()):
                if column > 1 and column < 7:
                    datarow.append(str(self.TableSalida.item(row, column).text()))
            datarow.append(self.listaLote[row])
            dataall.append(datarow)

        print(dataall)
        # borramos los datos de la tablaWidget
        for i in reversed(range(self.TableSalida.rowCount())):
            self.TableSalida.removeRow(i)

        Date = self.DateFechaESalida.date()
        FechaEsalida = Date.toPyDate()
        Date = self.DateFechaPSalida.date()
        FechaPsalida = Date.toPyDate()
        idSalidaU = int(self.LineControlSalida.text()) - 1

        tipo = 1
        reportes(dataall, self.LineAreaSalida.text(), self.Npedidoup, str(FechaEsalida),
                 str(FechaPsalida), self.vObserva, tipo)
    def observaciones(self):
        self.vObserva = self.uiObser.textObservaciones.toPlainText()
        self.EnvioReport()
        self.closeVtn()

    #mete los datos al TableWidget
    def insertDatosTablaWid(self):
        indexTableview = self.tableViewSalida.currentIndex().row()
        #saca id ID de la tableView
        self.claveid = self.tableViewSalida.model().index(indexTableview,0).data()
        self.Lote = self.tableViewSalida.model().index(indexTableview,4).data()
        self.listaLote.append(self.Lote)
        print(self.claveid)
        #pregunta si el id de farmaco se repite en la tablaview, si no ... entra y si si... no puede
        if not self.claveid in self.listaId:
            #consulta para sacar los campos  y luego meterlos al tableWidget
            self.Query = session.query(Clave.descripcion,Clave.presentacion, Farmaco.cantidad,Farmaco.caducidad).join(Clave).filter(Farmaco.idFarmaco == self.claveid).one()
            #print(self.Query)
            #aqui quiero preguntar la cantidad
            self.ventanaCanti = QtWidgets.QDialog()
            self.vtncanti = Ui_vtnCantidad()
            self.vtncanti.setupUi(self.ventanaCanti)
            self.ventanaCanti.show()
            self.vtncanti.btnAceptardialogSalida.clicked.connect(self.inserDatosBtn)
            self.vtncanti.btnCancelardialogSalida.clicked.connect(self.closeVtn)
            #hace que el LineEdit solo puedan introducir numeros
            intonly = QIntValidator()
            self.vtncanti.LineCantidaddialogSalida.setValidator(intonly)
        else:
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
            error_dialog.setText("Este Farmaco ya esta agregado")
            error_dialog.setWindowTitle("Error")
            error_dialog.exec()

    #cierra la ventana de vtnCantidad
    def closeVtn(self):
        QtWidgets.qApp.activeWindow().close()

    def inserDatosBtn(self):
        try:
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
            cantidadPuesta = int(self.vtncanti.LineCantidaddialogSalida.text())
            self.CantixId = cantidadPuesta
            if cantidadPuesta <= self.Query[2] and cantidadPuesta != 0:
                #####################################
                #cambio el formato de fecha
                Date =  self.DateFechaESalida.date()
                FechaEsalida = Date.toPyDate()
                Date =  self.DateFechaPSalida.date()
                FechaPsalida = Date.toPyDate()
                it = self.tableViewSalida.currentIndex().row()
                self.Clavecorta = self.tableViewSalida.model().index(it,1).data()
                Nrow = self.TableSalida.rowCount()
                self.TableSalida.insertRow(Nrow)
                #campos para el boton de eliminar
                self.btnDeleteSalida = QtWidgets.QPushButton(self)
                self.btnDeleteSalida.setGeometry(QtCore.QRect(320, 20, 21, 21))
                IconoDelete2 = QtGui.QIcon()
                IconoDelete2.addPixmap(QtGui.QPixmap("../imagenes/ic_delete_128_28267.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.btnDeleteSalida.setIcon(IconoDelete2)
                self.btnDeleteSalida.setStyleSheet("QPushButton{\n"
                    "border-radius:15px;\n"
                    "background:#fefefe;\n"
                    "\n"
                    "}\n"
                    "QPushButton:hover{\n"
                    "background:#dea806;\n"
                    "}\n"
                    "")
                
                #agrega al tableWidget
                self.TableSalida.setCellWidget(Nrow,0,self.btnDeleteSalida) 
                self.TableSalida.setItem(Nrow,1,QTableWidgetItem(str(self.LineControlSalida.text()))) 
                self.TableSalida.setItem(Nrow,2,QTableWidgetItem(str(self.Clavecorta)))
                self.TableSalida.setItem(Nrow,3,QTableWidgetItem(str(self.Query[0])))
                self.TableSalida.item(Nrow, 3).setToolTip(str(self.Query[0]))
                self.TableSalida.setItem(Nrow,4,QTableWidgetItem(str(self.Query[1])))
                self.TableSalida.item(Nrow, 4).setToolTip(str(self.Query[1]))
                self.TableSalida.setItem(Nrow,5,QTableWidgetItem(str(cantidadPuesta)))
                self.TableSalida.setItem(Nrow,6,QTableWidgetItem(str(self.Query[3])))
                self.TableSalida.setItem(Nrow,7,QTableWidgetItem(str(FechaEsalida)))
                self.TableSalida.setItem(Nrow,8,QTableWidgetItem(str(FechaPsalida)))

                self.btnDeleteSalida.clicked.connect(self.contadorSalida)
                #aumenta el numero en el control de salida
                self.NcontrolS()
                #Agrega el id a una lsita para que no pueda repetir
                self.listaId.append(self.claveid)
                self.listaCantidad.append(self.CantixId)
                #cierra la ventana
                self.closeVtn()
            else:
                #el dato puesto no sea 0
                if cantidadPuesta ==0:
                    error_dialog.setText("Ingresa una cantidad mayor")
                    error_dialog.setWindowTitle("Error")
                    error_dialog.exec()
                else:
                    #si el dato puesto es mayor a la existencia
                    error_dialog.setText("Ingresa una cantidad Menor")
                    error_dialog.setWindowTitle("Error")
                    error_dialog.exec()
        except:
            error_dialog.setText("Cantidad Vacia")
            error_dialog.setWindowTitle("Error")
            error_dialog.exec()


    #funcion con la cual controlamos el control de salida
    def NcontrolS(self):  
        #self.Ncontrol = session.query(func.max(Salida.numero_pedido)).scalar()
        self.Ncontrol = session.execute("""
    SELECT AUTO_INCREMENT
    FROM information_schema.TABLES
    WHERE TABLE_SCHEMA = "farmaciadb"
    AND TABLE_NAME = "salida"
""").scalar()
        # if self.Ncontrol  is None:
        #     self.Ncontrol = 0

        self.LineControlSalida.setText(str(self.Ncontrol))
        session.close()
    #Elimina filas den tableWidget y resta a al control de salida
    def contadorSalida(self):
        rowC = self.TableSalida.currentRow()
        print(rowC)
        #aqui elimina el ID de la lista de los ID
        self.listaId.pop(rowC)
        self.listaCantidad.pop(rowC)
        self.listaLote.pop(rowC)
        self.TableSalida.removeRow(rowC)
        row2 = self.TableSalida.rowCount()

 

    #le pasa el parametro de busqueda al lineDescribe
    def click(self,event):
        if event.buttons() and QtCore.Qt.LeftButton:
            self.TableViewInsertSalida()
    #Rellena el TableView Atravez de un QstandarItem
    def TableViewInsertSalida(self):
        #poner otra columna del ID-FARMACO
        
        self.x = str(self.comboboxSalida.currentIndex())
        self.q = session.query(Farmaco.idFarmaco,Farmaco.clave_corta, Clave.descripcion, Farmaco.caducidad, Farmaco.lote, Farmaco.cantidad,Farmaco.area,Farmaco.fechaIngreso).join(Clave).filter(Clave.tipo == self.x).all()
        #print(self.q)
        self.numero  = session.query(Farmaco.clave_corta).join(Clave).filter(Clave.tipo == self.x).count()
        self.model = QStandardItemModel(0,8)
        self.model.setHorizontalHeaderLabels(['Id farmaco','Clave', 'Descripción','Caducidad', 'Lote', 'Cantidad', 'Area Almacen','Fecha Ingreso'])
        self.tableViewSalida.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        print('cambio realizado')
        #aqui se necesita convertir a str por que el datatime hacia problemas
        for i, row in enumerate(self.q):
            for j, item in enumerate(row):
                add = QStandardItem(str(item))
                if j == 2:
                    add.setToolTip(str(item))
                if j == 6:
                    add.setToolTip(str(item))
                self.model.setItem(i, j, add)
        #se instancia la clase , esa clase nos ayuda que al escribir busque algo
        buscador = QSortFilterProxyModel()
        #este sirve para que puedan buscar alguna cosa no importa si es en mayusculas o minusculas
        buscador.setFilterCaseSensitivity(Qt.CaseInsensitive)
        buscador.setSourceModel(self.model)
        #aqui le indicamos en que columba de la tabla va a filter cosas segun lo que se escriba
        buscador.setFilterKeyColumn(1)
        self.LineClaveSalida.textChanged.connect(buscador.setFilterRegExp)
        #condicion para que pueda buscar en descripcion
        if self.LineDescripSalida.hasFocus():
            buscador.setFilterKeyColumn(2)
            self.LineDescripSalida.textChanged.connect(buscador.setFilterRegExp)
        self.tableViewSalida.setModel(buscador)
        #sirve para darle color a las celdas de cantidad las que tienen menor a 10 o 10
        for h in range(self.numero):
            cantiRojo = int(self.tableViewSalida.model().index(h,5).data())
            #print(cantiRojo)
            if cantiRojo <=10: 
                self.model.setData(self.model.index(h,5), QtGui.QBrush(QtCore.Qt.white), QtCore.Qt.ForegroundRole)
                self.model.setData(self.model.index(h,5), QtGui.QBrush(QtGui.QColor(236,47,6)), QtCore.Qt.BackgroundRole)

                    
        #poner de color rojo los farmacos que esten mejor de 10 


        #IMPORTATE cerrar la sesion ya que una session tiene los datos de cuando fue abierta , si quieres obtener nuevos datos no podras por que necesitas una nueva session 
        #y esa session tendra los nuevos datos
        #cerrar session y automaticamente se abre otra.
        session.close()

    def update(self):
        self.TableViewInsertSalida()

    def openRef(self):
        self.vtnRef = QtWidgets.QWidget()
        self.uiRef = Ui_VtnES(self.EnOsal)
        self.uiRef.setupUi(self.vtnRef)
        self.vtnRef.show()     



    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        #self.setWindowTitle(_translate("InterFazSalida", "Salidas"))
        self.label_8.setText(_translate("InterFazSalida", "Clave:"))
        self.label_9.setText(_translate("InterFazSalida", "Descripción:"))
        self.btnFinalizarSalida.setText(_translate("InterFazSalida", "Finalizar"))
        item = self.TableSalida.horizontalHeaderItem(0)
        item.setText(_translate("InterFazSalida", "Eliminar"))
        item = self.TableSalida.horizontalHeaderItem(1)
        item.setText(_translate("InterFazSalida", "N.Salida"))
        item = self.TableSalida.horizontalHeaderItem(2)
        item.setText(_translate("InterFazSalida", "Clave"))
        item = self.TableSalida.horizontalHeaderItem(3)
        item.setText(_translate("InterFazSalida", "Descripción"))
        item = self.TableSalida.horizontalHeaderItem(4)
        item.setText(_translate("InterFazSalida", "Presentación"))
        item = self.TableSalida.horizontalHeaderItem(5)
        item.setText(_translate("InterFazSalida", "Cantidad"))
        item = self.TableSalida.horizontalHeaderItem(6)
        item.setText(_translate("InterFazSalida", "Caducidad"))
        item = self.TableSalida.horizontalHeaderItem(7)
        item.setText(_translate("InterFazSalida", "Fecha pedido"))
        item = self.TableSalida.horizontalHeaderItem(8)
        item.setText(_translate("InterFazSalida", "Fecha Entrega"))

        self.btnTotalEntradasEntra.setShortcut(_translate("InterFazSalida", "Ctrl+E"))
        self.label_16.setText(_translate("InterFazSalida", "N.Salida:"))
        self.label_17.setText(_translate("InterFazSalida", "Fecha Entrega:"))
        self.DateFechaPSalida.setDisplayFormat(_translate("InterFazSalida", "dd/MM/yyyy"))
        self.label_18.setText(_translate("InterFazSalida", "Destino:"))
        self.label_19.setText(_translate("InterFazSalida", "Fecha Pedido:"))
        self.DateFechaESalida.setDisplayFormat(_translate("InterFazSalida", "dd/MM/yyyy"))
        self.comboboxSalida.setItemText(0, _translate("InterFazSalida", "Medicamento"))
        self.comboboxSalida.setItemText(1, _translate("InterFazSalida", "M.Curacion"))
        self.label_20.setText(_translate("InterFazSalida", "Tipo:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InterFazSalida = QtWidgets.QWidget()
    ui = SubWindow()
    ui.createSubWindow()
    InterFazSalida.show()
    sys.exit(app.exec_())
