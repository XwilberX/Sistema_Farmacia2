from PyQt5.QtWidgets import QMdiSubWindow, QMainWindow, QWidget, QPushButton,QTableView,QHeaderView,QTableWidgetItem
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIntValidator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from vtnCantidad import Ui_vtnCantidad
import sys
sys.path.append('../Modelo/')
from farm import Salida
from farm import Clave
from farm import Farmaco
import pandas as pd

engine = create_engine('mysql+pymysql://root:@localhost/prueba')
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
        self.frame_2.setGeometry(QtCore.QRect(50, 110, 961, 560))
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
        self.Frame2 = QtWidgets.QFrame(self)
        self.Frame2.setGeometry(QtCore.QRect(90, 20, 881, 71))
        self.Frame2.setStyleSheet("\n"
" background:#fefefe;\n"
"\n"
"")
        self.Frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame2.setObjectName("Frame2")
        self.label_16 = QtWidgets.QLabel(self.Frame2)
        self.label_16.setGeometry(QtCore.QRect(30, 10, 91, 20))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.Frame2)
        self.label_17.setGeometry(QtCore.QRect(550, 10, 91, 21))
        self.label_17.setObjectName("label_17")
        self.LineControlSalida = QtWidgets.QLineEdit(self.Frame2)
        self.LineControlSalida.setGeometry(QtCore.QRect(120, 10, 121, 21))
        self.LineControlSalida.setObjectName("LineControlSalida")
        #
        self.LineControlSalida.setEnabled(False)
        #
        self.DateFechaPSalida = QtWidgets.QDateEdit(self.Frame2)
        self.DateFechaPSalida.setGeometry(QtCore.QRect(640, 10, 121, 22))
        self.DateFechaPSalida.setAccelerated(False)
        self.DateFechaPSalida.setProperty("showGroupSeparator", False)
        self.DateFechaPSalida.setCalendarPopup(True)
        self.DateFechaPSalida.setTimeSpec(QtCore.Qt.UTC)
        self.DateFechaPSalida.setDate(QtCore.QDate(2020, 1, 1))
        self.DateFechaPSalida.setObjectName("DateFechaPSalida")
        self.label_18 = QtWidgets.QLabel(self.Frame2)
        self.label_18.setGeometry(QtCore.QRect(30, 40, 41, 20))
        self.label_18.setObjectName("label_18")
        self.LineAreaSalida = QtWidgets.QLineEdit(self.Frame2)
        self.LineAreaSalida.setGeometry(QtCore.QRect(120, 40, 121, 21))
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

        
        #INICIO DEL CODIGO
        now = datetime.now()
        self.DateFechaESalida.setDate(now)
        self.DateFechaPSalida.setDate(now)

        #Consulta al numero de control Ventana Salida
        self.conta = 0
        self.NcontrolS()
        self.TableViewInsertSalida()
        self.comboboxSalida.currentIndexChanged.connect(self.TableViewInsertSalida)

        self.LineDescripSalida.mousePressEvent = self.click
        

        self.tableViewSalida.doubleClicked.connect(self.insertDatosTablaWid)
        



    def insertDatosTablaWid(self):
        
        indexTableview = self.tableViewSalida.currentIndex().row()
        #saca id ID de la tableView
        self.claveid = self.tableViewSalida.model().index(indexTableview,0).data()
        print(self.claveid)
        #consulta para sacar los campos  y luego meterlos al tableWidget
        self.Query = session.query(Clave.descripcion,Clave.presentacion, Farmaco.cantidad,Farmaco.caducidad).join(Clave).filter(Farmaco.idFarmaco == self.claveid).one()
        print(self.Query)

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

    #cierra la ventana de vtnCantidad
    def closeVtn(self):
        QtWidgets.qApp.activeWindow().close()

    def inserDatosBtn(self):
        cantidadPuesta = int(self.vtncanti.LineCantidaddialogSalida.text())
        if cantidadPuesta <= self.Query[2]:
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
            self.TableSalida.setItem(Nrow,2,QTableWidgetItem(str(self.claveid)))
            self.TableSalida.setItem(Nrow,3,QTableWidgetItem(str(self.Query[0])))
            self.TableSalida.setItem(Nrow,4,QTableWidgetItem(str(self.Query[1])))
            self.TableSalida.setItem(Nrow,5,QTableWidgetItem(str(cantidadPuesta)))
            self.TableSalida.setItem(Nrow,6,QTableWidgetItem(str(self.Query[3])))
            self.TableSalida.setItem(Nrow,7,QTableWidgetItem(str(self.DateFechaPSalida.text())))
            self.TableSalida.setItem(Nrow,8,QTableWidgetItem(str(self.DateFechaESalida.text())))

            self.btnDeleteSalida.clicked.connect(self.contadorSalida)
            #aumenta el numero en el control de salida
            self.NcontrolS()
            #cierra la ventana
            self.closeVtn()
        else: 
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
            error_dialog.setText("Ingresa una cantidad Menor")
            error_dialog.setWindowTitle("Error")
            error_dialog.exec()

    #funcion con la cual controlamos el control de salida
    def NcontrolS(self):  
        self.Ncontrol = session.query(Salida).count()
        self.conta= self.conta + 1
        self.LineControlSalida.setText(str(self.Ncontrol + self.conta))

    #Elimina filas den tableWidget y resta a al control de salida
    def contadorSalida(self):
        rowC = self.TableSalida.currentRow()
        self.TableSalida.removeRow(rowC)
        self.conta = self.conta - 1 
        self.LineControlSalida.setText(str(self.Ncontrol + self.conta))
        row2 = self.TableSalida.rowCount()
        for a in range(row2):
                if a >= rowC:
                        hola = int(self.TableSalida.item(a,1).text())
                        pedro = hola - 1 
                        self.TableSalida.setItem(a,1,QTableWidgetItem(str(pedro)))


    #le pasa el parametro de busqueda al lineDescribe
    def click(self,event):
        if event.buttons() and QtCore.Qt.LeftButton:
            self.TableViewInsertSalida()
        #Rellena el TableView Atravez de un QstandarItem
    def TableViewInsertSalida(self):
        #poner otra columna del ID-FARMACO
        self.x = str(self.comboboxSalida.currentIndex())
        self.q = session.query(Farmaco.idFarmaco,Farmaco.clave_corta, Clave.descripcion, Farmaco.caducidad, Farmaco.cantidad, Farmaco.lote,Farmaco.area,Farmaco.fecha).join(Clave).filter(Clave.tipo == self.x).all()
        self.numero  = session.query(Farmaco.clave_corta).join(Clave).filter(Clave.tipo == self.x).count()
        self.model = QStandardItemModel(0,8)
        self.model.setHorizontalHeaderLabels(['Id farmaco','Clave', 'Descripción','Caducidad', 'Cantidad', 'Lote', 'Area Almacen','Fecha Ingreso'])
        self.tableViewSalida.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        #aqui se necesita convertir a str por que el datatime hacia problemas
        for item in self.q:
            self.model.appendRow([QStandardItem(str(x)) for x in item])
        buscador = QSortFilterProxyModel()
        buscador.setSourceModel(self.model)
        buscador.setFilterKeyColumn(1)
        self.LineClaveSalida.textChanged.connect(buscador.setFilterRegExp)
        #condicion para que pueda buscar en descripcion
        if self.LineDescripSalida.hasFocus():
            buscador.setFilterKeyColumn(2)
            self.LineDescripSalida.textChanged.connect(buscador.setFilterRegExp)
        self.tableViewSalida.setModel(buscador)





    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("InterFazSalida", "Salidas"))
        self.label_8.setText(_translate("InterFazSalida", "Clave:"))
        self.label_9.setText(_translate("InterFazSalida", "Descripción:"))
        self.btnFinalizarSalida.setText(_translate("InterFazSalida", "Finalizar"))
        item = self.TableSalida.horizontalHeaderItem(0)
        item.setText(_translate("InterFazSalida", "Eliminar"))
        item = self.TableSalida.horizontalHeaderItem(1)
        item.setText(_translate("InterFazSalida", "Control Salida"))
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
        self.label_16.setText(_translate("InterFazSalida", "Control Salida:"))
        self.label_17.setText(_translate("InterFazSalida", "Fecha Pedido:"))
        self.DateFechaPSalida.setDisplayFormat(_translate("InterFazSalida", "dd/MM/yyyy"))
        self.label_18.setText(_translate("InterFazSalida", "Area:"))
        self.label_19.setText(_translate("InterFazSalida", "Fecha Entrega:"))
        self.DateFechaESalida.setDisplayFormat(_translate("InterFazSalida", "dd/MM/yyyy"))
        self.comboboxSalida.setItemText(0, _translate("InterFazSalida", "Medicina"))
        self.comboboxSalida.setItemText(1, _translate("InterFazSalida", "Material/Curacion"))
        self.label_20.setText(_translate("InterFazSalida", "Tipo:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InterFazSalida = QtWidgets.QWidget()
    ui = SubWindow()
    ui.createSubWindow()
    InterFazSalida.show()
    sys.exit(app.exec_())
