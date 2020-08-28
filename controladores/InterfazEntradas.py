# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfazEntradas.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, MetaData, Table,DateTime, Date , ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QCompleter, QTableView,QHeaderView,QMessageBox, QMdiSubWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import sys
sys.path.append('../Modelo/')
from farm import Farmaco, Clave
from BusquedaDPview3 import Ui_BDP
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIntValidator
from subwindow import SubWindow
import pandas as pd

engine = create_engine('mysql+pymysql://root:wil99@localhost/prueba')
Session = sessionmaker(bind=engine)
session = Session()

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1291, 911)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagenes/Mono.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main.setWindowIcon(icon)
        Main.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size: 15px;\n"
"}\n"
"QFrame{\n"
"border-radius: 60px;\n"
" background:#fefefe;\n"
"}\n"
"QLabel{\n"
"    background:transparent;\n"
"}\n"
"#Main{\n"
"background: #b8f4f0;\n"
"}\n"
"QLineEdit{\n"
"    border:none;\n"
"    border-bottom: 1px solid black;\n"
"}\n"
"\n"
"#FrameEntradaprimero{\n"
"border-radius:30px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 121, 350))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../imagenes/decoracion10reves2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1170, 0, 121, 350))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../imagenes/volteada.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 10, 191, 70))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../imagenes/salud_logo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(840, 10, 201, 70))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../imagenes/chiapas.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(120, 90, 1051, 721))
        self.mdiArea.setStyleSheet("background-color: rgb(184, 244, 240);\n"
"")
        self.mdiArea.setObjectName("mdiArea")
        self.subwindowEntradas = QtWidgets.QWidget()
        self.subwindowEntradas.setStyleSheet("QCalendarWidget QAbstractItemView\n"
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
        self.subwindowEntradas.setObjectName("subwindowEntradas")
        self.FrameEntradaprimero = QtWidgets.QFrame(self.subwindowEntradas)
        self.FrameEntradaprimero.setGeometry(QtCore.QRect(40, 20, 921, 81))
        self.FrameEntradaprimero.setStyleSheet("\n"
"background:#fefefe;\n"
"")
        self.FrameEntradaprimero.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameEntradaprimero.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameEntradaprimero.setObjectName("FrameEntradaprimero")
        self.label_5 = QtWidgets.QLabel(self.FrameEntradaprimero)
        self.label_5.setGeometry(QtCore.QRect(30, 10, 71, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.FrameEntradaprimero)
        self.label_6.setGeometry(QtCore.QRect(40, 50, 51, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.FrameEntradaprimero)
        self.label_7.setGeometry(QtCore.QRect(590, 30, 161, 20))
        self.label_7.setObjectName("label_7")
        self.LineOrigenEntra = QtWidgets.QLineEdit(self.FrameEntradaprimero)
        self.LineOrigenEntra.setGeometry(QtCore.QRect(100, 9, 121, 21))
        self.LineOrigenEntra.setObjectName("LineOrigenEntra")
        self.DateFechaEntra = QtWidgets.QDateEdit(self.FrameEntradaprimero)
        self.DateFechaEntra.setGeometry(QtCore.QRect(100, 50, 121, 22))
        self.DateFechaEntra.setAccelerated(False)
        self.DateFechaEntra.setProperty("showGroupSeparator", False)
        self.DateFechaEntra.setCalendarPopup(True)
        self.DateFechaEntra.setTimeSpec(QtCore.Qt.UTC)
        self.DateFechaEntra.setDate(QtCore.QDate(2020, 1, 1))
        self.DateFechaEntra.setObjectName("DateFechaEntra")
        self.LineControlEntra = QtWidgets.QLineEdit(self.FrameEntradaprimero)
        self.LineControlEntra.setEnabled(False)
        self.LineControlEntra.setGeometry(QtCore.QRect(740, 19, 113, 31))
        self.LineControlEntra.setObjectName("LineControlEntra")
        self.label_15 = QtWidgets.QLabel(self.FrameEntradaprimero)
        self.label_15.setGeometry(QtCore.QRect(300, 30, 41, 20))
        self.label_15.setObjectName("label_15")
        self.comboBoxEntradas = QtWidgets.QComboBox(self.FrameEntradaprimero)
        self.comboBoxEntradas.setGeometry(QtCore.QRect(340, 30, 151, 22))
        self.comboBoxEntradas.setObjectName("comboBoxEntradas")
        self.comboBoxEntradas.addItem("")
        self.comboBoxEntradas.addItem("")
        self.frame_2 = QtWidgets.QFrame(self.subwindowEntradas)
        self.frame_2.setGeometry(QtCore.QRect(40, 120, 921, 531))
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
        self.LineClaveEntra = QtWidgets.QLineEdit(self.frame_2)
        self.LineClaveEntra.setGeometry(QtCore.QRect(120, 10, 191, 31))
        self.LineClaveEntra.setObjectName("LineClaveEntra")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 111, 21))
        self.label_9.setObjectName("label_9")
        self.TextDescriEntra = QtWidgets.QTextEdit(self.frame_2)
        #
        #
        #
        self.TextDescriEntra.setEnabled(True)
        #
        #
        #
        self.TextDescriEntra.setGeometry(QtCore.QRect(120, 50, 271, 51))
        self.TextDescriEntra.setStyleSheet("background-color: rgb(184, 244, 240);\n"
"")
        self.TextDescriEntra.setObjectName("TextDescriEntra")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(10, 120, 111, 21))
        self.label_10.setObjectName("label_10")
        self.TableEntra = QtWidgets.QTableWidget(self.frame_2)
        self.TableEntra.setGeometry(QtCore.QRect(20, 170, 881, 321))
        self.TableEntra.setObjectName("TableEntra")
        self.TableEntra.setColumnCount(11)
        self.TableEntra.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagenes/ic_delete_128_28267.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.TableEntra.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
        self.TableEntra.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
        self.TableEntra.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
        self.TableEntra.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
        self.TableEntra.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
        self.TableEntra.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
        self.TableEntra.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
        self.TableEntra.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
        self.TableEntra.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
        self.TableEntra.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
        self.TableEntra.setHorizontalHeaderItem(10, item)
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(400, 70, 71, 31))
        self.label_11.setObjectName("label_11")
        self.LineCantidadEntra = QtWidgets.QLineEdit(self.frame_2)
        self.LineCantidadEntra.setGeometry(QtCore.QRect(510, 60, 161, 31))
        self.LineCantidadEntra.setObjectName("LineCantidadEntra")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(400, 30, 121, 16))
        self.label_12.setObjectName("label_12")
        self.btnClaveEntra = QtWidgets.QPushButton(self.frame_2)
        self.btnClaveEntra.setGeometry(QtCore.QRect(320, 20, 21, 21))
        self.btnClaveEntra.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../imagenes/minoculares.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClaveEntra.setIcon(icon2)
        self.btnClaveEntra.setIconSize(QtCore.QSize(20, 20))
        self.btnClaveEntra.setObjectName("btnClaveEntra")
        self.LineaAreaEntra = QtWidgets.QLineEdit(self.frame_2)
        self.LineaAreaEntra.setGeometry(QtCore.QRect(510, 20, 161, 31))
        self.LineaAreaEntra.setObjectName("LineaAreaEntra")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(400, 130, 91, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(700, 30, 47, 13))
        self.label_14.setObjectName("label_14")
        self.LineLoteEntra = QtWidgets.QLineEdit(self.frame_2)
        self.LineLoteEntra.setGeometry(QtCore.QRect(750, 19, 113, 31))
        self.LineLoteEntra.setObjectName("LineLoteEntra")
        self.btnAgregarEntra = QtWidgets.QPushButton(self.frame_2)
        self.btnAgregarEntra.setGeometry(QtCore.QRect(720, 60, 141, 31))
        self.btnAgregarEntra.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background:#ffc001;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background:#dea806;\n"
"}\n"
"")
        self.btnAgregarEntra.setObjectName("btnAgregarEntra")
        self.btnFinalizarEntra = QtWidgets.QPushButton(self.frame_2)
        self.btnFinalizarEntra.setGeometry(QtCore.QRect(720, 100, 141, 31))
        self.btnFinalizarEntra.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background:#ffc001;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background:#dea806;\n"
"}\n"
"")
        self.btnFinalizarEntra.setObjectName("btnFinalizarEntra")
        self.DateCaducidadEntra = QtWidgets.QDateEdit(self.frame_2)
        self.DateCaducidadEntra.setGeometry(QtCore.QRect(500, 130, 110, 22))
        self.DateCaducidadEntra.setCalendarPopup(True)
        self.DateCaducidadEntra.setTimeSpec(QtCore.Qt.LocalTime)
        self.DateCaducidadEntra.setDate(QtCore.QDate(2020, 1, 1))
        self.DateCaducidadEntra.setObjectName("DateCaducidadEntra")
        self.TextPresentaEntra = QtWidgets.QTextEdit(self.frame_2)
        #
        #
        #
        self.TextPresentaEntra.setEnabled(True)
        #
        #
        #
        self.TextPresentaEntra.setGeometry(QtCore.QRect(120, 110, 271, 51))
        self.TextPresentaEntra.setStyleSheet("background-color: rgb(184, 244, 240);\n"
"")
        self.TextPresentaEntra.setObjectName("TextPresentaEntra")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1291, 26))
        self.menubar.setObjectName("menubar")
        self.menuEntradas = QtWidgets.QMenu(self.menubar)
        self.menuEntradas.setObjectName("menuEntradas")
        self.menuSalidas = QtWidgets.QMenu(self.menubar)
        self.menuSalidas.setObjectName("menuSalidas")
        self.menuConsultas = QtWidgets.QMenu(self.menubar)
        self.menuConsultas.setObjectName("menuConsultas")
        self.menuClaves = QtWidgets.QMenu(self.menubar)
        self.menuClaves.setObjectName("menuClaves")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(Main)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setObjectName("toolBar")
        Main.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionEntradas = QtWidgets.QAction(Main)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../imagenes/agregar clave (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEntradas.setIcon(icon3)
        self.actionEntradas.setObjectName("actionEntradas")
        self.actionSalidas = QtWidgets.QAction(Main)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../imagenes/medicina.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalidas.setIcon(icon4)
        self.actionSalidas.setObjectName("actionSalidas")
        self.actionkardex = QtWidgets.QAction(Main)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../imagenes/salidas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionkardex.setIcon(icon5)
        self.actionkardex.setObjectName("actionkardex")
        self.actionAgregar_claves = QtWidgets.QAction(Main)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../imagenes/agregar clave (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAgregar_claves.setIcon(icon6)
        self.actionAgregar_claves.setObjectName("actionAgregar_claves")
        self.actionlogo_chiapas = QtWidgets.QAction(Main)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../imagenes/secretaria de salud.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionlogo_chiapas.setIcon(icon7)
        self.actionlogo_chiapas.setObjectName("actionlogo_chiapas")
        self.actionlogo_secretaria_salud = QtWidgets.QAction(Main)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../imagenes/salud_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionlogo_secretaria_salud.setIcon(icon8)
        self.actionlogo_secretaria_salud.setObjectName("actionlogo_secretaria_salud")
        self.actionIntroducir_Inventario = QtWidgets.QAction(Main)
        self.actionIntroducir_Inventario.setObjectName("actionIntroducir_Inventario")
        self.actionSalida_de_inventario = QtWidgets.QAction(Main)
        self.actionSalida_de_inventario.setObjectName("actionSalida_de_inventario")
        self.actionConsulta_de_inventario = QtWidgets.QAction(Main)
        self.actionConsulta_de_inventario.setObjectName("actionConsulta_de_inventario")
        self.actionAgregar_claves_de_inventario = QtWidgets.QAction(Main)
        self.actionAgregar_claves_de_inventario.setObjectName("actionAgregar_claves_de_inventario")
        self.menuEntradas.addAction(self.actionEntradas)
        self.menuSalidas.addAction(self.actionSalidas)
        self.menuConsultas.addAction(self.actionkardex)
        self.menuClaves.addAction(self.actionAgregar_claves)
        self.menubar.addAction(self.menuEntradas.menuAction())
        self.menubar.addAction(self.menuSalidas.menuAction())
        self.menubar.addAction(self.menuConsultas.menuAction())
        self.menubar.addAction(self.menuClaves.menuAction())
        self.toolBar.addAction(self.actionEntradas)
        self.toolBar.addAction(self.actionSalidas)
        self.toolBar.addAction(self.actionkardex)
        self.toolBar.addAction(self.actionAgregar_claves)
        
        self.subwindowEntradas.setWindowTitle('Entradas')
        self.mdiArea.addSubWindow(self.subwindowEntradas)
        self.subwindowEntradas.showMaximized()

        # Agregando subwindow de salida
        self.uiSalida = SubWindow()
        self.uiSalida.createSubWindow()
        self.mdiArea.addSubWindow(self.uiSalida)

        self.mdiArea.activateNextSubWindow()
        
        #inicio del codigo
        # Para que aparezca la ventana de entradas al iniciar

        self.actionEntradas.triggered.connect(self.abrirVentana)
        self.actionSalidas.triggered.connect(self.abrirSalidas)



        #agregar Items a la tabla de Entradas
        self.btnAgregarEntra.clicked.connect(self.enviar)


        #aumentar el numero de control
        self.conta = 0
        self.control()

        #coloca la fecha actual en los QdateEdit
        now = datetime.now()
        self.DateCaducidadEntra.setDate(now)
        self.DateFechaEntra.setDate(now)
        
        #Busqueda en tiempo real
        self.BusquedaTreal()
        #pone la desc y presentacion en los textEdit
        self.LineClaveEntra.returnPressed.connect(self.ConsultaDesc)
        #abre la ventana para buscar por DESC o PRESENTACION
        self.btnClaveEntra.clicked.connect(self.BusquedaDP)


        self.btnFinalizarEntra.clicked.connect(self.FinalizarTabla)
        
        intonly = QIntValidator()
        self.LineCantidadEntra.setValidator(intonly)

        self.comboBoxEntradas.currentIndexChanged.connect(self.BusquedaTreal)



        self.retranslateUi(Main)
        self.btnFinalizarEntra.clicked.connect(self.LineCantidadEntra.clear)
        self.btnFinalizarEntra.clicked.connect(self.LineaAreaEntra.clear)
        self.btnFinalizarEntra.clicked.connect(self.LineLoteEntra.clear)
        self.btnFinalizarEntra.clicked.connect(self.TextDescriEntra.clear)
        self.btnFinalizarEntra.clicked.connect(self.LineClaveEntra.clear)
        self.btnFinalizarEntra.clicked.connect(self.LineOrigenEntra.clear)

        #
        self.btnFinalizarEntra.clicked.connect(self.TextPresentaEntra.clear)
        #
        #
        self.btnAgregarEntra.clicked.connect(self.LineLoteEntra.clear)
        #


        self.retranslateUi(Main)
        self.btnFinalizarEntra.clicked.connect(self.LineCantidadEntra.clear)
        self.btnFinalizarEntra.clicked.connect(self.LineaAreaEntra.clear)
        self.btnFinalizarEntra.clicked.connect(self.LineLoteEntra.clear)
        self.btnFinalizarEntra.clicked.connect(self.TextDescriEntra.clear)
        self.btnFinalizarEntra.clicked.connect(self.LineClaveEntra.clear)
        self.btnFinalizarEntra.clicked.connect(self.LineOrigenEntra.clear)
        self.btnAgregarEntra.clicked.connect(self.LineaAreaEntra.clear)
        self.btnAgregarEntra.clicked.connect(self.LineCantidadEntra.clear)
        self.btnAgregarEntra.clicked.connect(self.TextDescriEntra.clear)
        self.btnAgregarEntra.clicked.connect(self.LineClaveEntra.clear)
        self.btnAgregarEntra.clicked.connect(self.TextPresentaEntra.clear)
        QtCore.QMetaObject.connectSlotsByName(Main)
        Main.setTabOrder(self.LineOrigenEntra, self.DateFechaEntra)
        Main.setTabOrder(self.DateFechaEntra, self.LineControlEntra)
        Main.setTabOrder(self.LineControlEntra, self.LineClaveEntra)
        Main.setTabOrder(self.LineClaveEntra, self.btnClaveEntra)
        Main.setTabOrder(self.btnClaveEntra, self.TextDescriEntra)
        Main.setTabOrder(self.TextDescriEntra, self.LineaAreaEntra)
        Main.setTabOrder(self.LineaAreaEntra, self.LineCantidadEntra)
        Main.setTabOrder(self.LineCantidadEntra, self.DateCaducidadEntra)
        Main.setTabOrder(self.DateCaducidadEntra, self.LineLoteEntra)
        Main.setTabOrder(self.LineLoteEntra, self.TableEntra)
        Main.setTabOrder(self.TableEntra, self.btnAgregarEntra)
        Main.setTabOrder(self.btnAgregarEntra, self.btnFinalizarEntra)

 #FUNCIONES
    # VER QUE BORRE EL FINALIZAR Y EL AGREGAR
    def abrirSalidas(self):
        self.subwindowEntradas.hide()
        self.uiSalida.showMaximized()
    def abrirVentana(self):
        self.uiSalida.hide()
        self.subwindowEntradas.showMaximized()
    def FinalizarTabla(self):
        try:
            lista=[]
            Dp = pd.DataFrame()
            rows = self.TableEntra.rowCount()
            Column = self.TableEntra.columnCount()
            #TUVIMOS QUE ARREGLAR EL ORDEN DE LOS HEADERS PARA QUE JALE LA CONSULTA JUSTO CON LA TABLA DE BD Y EL DATAFRAME
            headers = ['idFarmaco', 'origen', 'clave_corta', 'area','cantidad','caducidad','lote','fecha']
            for i in range(rows):
                for j in range(Column):
                    #Este If es por que no necesitamos las columnas de descripcion y presentacion en el ingreso al DATAFRAME ya que al ingresar el dataframe a la BD no estan esos campos
                    if j != 4 and j != 5 and j != 0:
                        Dp.loc[i,j] = self.TableEntra.item(i,j).text()
            Dp.columns =headers
            print(Dp)
            #Ingreso DEl dataframe a la bd tipo ingreso pandas(NO SQLALCHEMY)
            Dp.to_sql('farmaco', engine, index= False, if_exists="append")
            for i in reversed(range(self.TableEntra.rowCount())):
                self.TableEntra.removeRow(i)
            self.conta= 0
            self.control()
        except:
            self.LineClaveEntra.setFocus()
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
            error_dialog.setText("No hay datos en la tabla")
            error_dialog.setWindowTitle("Error")
            error_dialog.exec()

    def BusquedaDP(self):
        self.ventanaDP = QtWidgets.QMainWindow()
        self.x = str(self.comboBoxEntradas.currentIndex())
        self.ui=Ui_BDP(self.x)
        self.ui.setupUi(self.ventanaDP)
        self.ventanaDP.show()
        self.ui.tableView.doubleClicked.connect(self.fnti)
        #self.ui.tableView.doubleClicked.connect(self.fnti)
    
    def fnti(self):  
        index = self.ui.tableView.currentIndex().row()
        value = self.ui.tableView.model().index(index,0).data()
        self.LineClaveEntra.setText(value)
        self.ConsultaDesc()
          

    #Traer la descripcion y presentacion con la clave 
    def ConsultaDesc(self):
        try: 
            self.LineClaveEntra.setStyleSheet("QLineEdit { border-color: black;}")
            print('EJECUTANDO LA FUNCION')
            tipos = self.comboBoxEntradas.currentIndex()
            Vclave = self.LineClaveEntra.text()
            if tipos == 0:
                Desc = session.query(Clave.descripcion, Clave.presentacion).filter_by(corta=Vclave, tipo=0).one()
            if tipos == 1:
                Desc = session.query(Clave.descripcion, Clave.presentacion).filter_by(corta=Vclave, tipo=1).one()

            print(Desc[0])
            print(Desc[1])
            self.TextDescriEntra.setText(Desc[0])
            self.TextPresentaEntra.setText(Desc[1])
        except:
            self.LineClaveEntra.setStyleSheet("QLineEdit { border-color: red;}")
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setIcon(QtWidgets.QMessageBox.Information)
            error_dialog.setText("La clave no existe o el tipo es diferente")
            error_dialog.setWindowTitle("Informacion!!!")
            error_dialog.exec()
            
        
            

    #consulta para el Numero de control
    def control(self):
        
        self.Ncontrol = session.query(Farmaco).count()
        self.conta= self.conta + 1
        self.LineControlEntra.setText(str(self.Ncontrol + self.conta))


    
    #busqueda en tiempo real
    def BusquedaTreal(self):
        list = []
        tipos = self.comboBoxEntradas.currentIndex()
        print(tipos)
        if tipos == 0:
            clave123 = session.query(Clave.corta).filter_by(tipo=0).all()
        if tipos == 1:
            clave123 = session.query(Clave.corta).filter_by(tipo=1).all()
        for n in clave123:
            for c in n:
                list.append(c)
        ListaClave = list
        completer =  QCompleter(ListaClave)
        self.LineClaveEntra.setCompleter(completer)
    





    #Envia los datos a la tabla
    def enviar(self):
        if self.LineClaveEntra.text() == "":
            self.LineClaveEntra.setStyleSheet("QLineEdit { border-color: red;}")
            self.LineClaveEntra.setFocus()
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setIcon(QtWidgets.QMessageBox.Information)
            error_dialog.setText("Clave vacia")
            error_dialog.setWindowTitle("Error")
            error_dialog.exec()
        else:
            row = self.TableEntra.rowCount()
            rowPosition = self.TableEntra.rowCount()
            self.TableEntra.insertRow(rowPosition)

            Date =  self.DateCaducidadEntra.date()
            caducidad = Date.toPyDate()
            Date2 = self.DateFechaEntra.date()
            FechaIngreso = Date2.toPyDate()
            #self.TableEntra.verticalHeader().hide()
            self.btnDelete = QtWidgets.QPushButton(self.frame_2)
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
            
            self.TableEntra.setCellWidget(row,0,self.btnDelete)
            
            self.TableEntra.setItem(row, 1, QTableWidgetItem(
                str(self.LineControlEntra.text())))
            self.TableEntra.setItem(row, 2, QTableWidgetItem(
                str(self.LineOrigenEntra.text())))
            self.TableEntra.setItem(row, 3, QTableWidgetItem(
                str(self.LineClaveEntra.text())))
            self.TableEntra.setItem(row, 4, QTableWidgetItem(
                str(self.TextDescriEntra.toPlainText())))
            self.TableEntra.setItem(row, 5, QTableWidgetItem(
                str(self.TextPresentaEntra.toPlainText())))
            self.TableEntra.setItem(row, 6, QTableWidgetItem(
                str(self.LineaAreaEntra.text())))
            self.TableEntra.setItem(row, 7, QTableWidgetItem(
                str(self.LineCantidadEntra.text())))
            self.TableEntra.setItem(row, 8, QTableWidgetItem(
                str(caducidad)))
            self.TableEntra.setItem(row, 9, QTableWidgetItem(
                str(self.LineLoteEntra.text())))    
            self.TableEntra.setItem(row, 10, QTableWidgetItem(
                str(FechaIngreso)))
            self.control()    
            self.btnDelete.clicked.connect(self.contador)
    
    
    
    #Elimina las filas del tablewitget
    def contador(self):
        rowC = self.TableEntra.currentRow()
        self.TableEntra.removeRow(rowC)
        self.conta = self.conta - 1 
        self.LineControlEntra.setText(str(self.Ncontrol + self.conta))
        row2 = self.TableEntra.rowCount()
        for a in range(row2):
                if a >= rowC:
                        hola = int(self.TableEntra.item(a,1).text())
                        pedro = hola - 1 
                        self.TableEntra.setItem(a,1,QTableWidgetItem(str(pedro)))

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Sistema de Inventario"))
        self.subwindowEntradas.setWindowTitle(_translate("Main", "Entradas"))
        self.label_5.setText(_translate("Main", "Origen:"))
        self.label_6.setText(_translate("Main", "Fecha:"))
        self.label_7.setText(_translate("Main", "Control Secuencial:"))
        self.DateFechaEntra.setDisplayFormat(_translate("Main", "dd/MM/yyyy"))
        self.label_15.setText(_translate("Main", "Tipo:"))
        self.comboBoxEntradas.setItemText(0, _translate("Main", "Medicina"))
        self.comboBoxEntradas.setItemText(1, _translate("Main", "Material/Curacion"))
        self.label_8.setText(_translate("Main", "Clave:"))
        self.label_9.setText(_translate("Main", "Descripción:"))
        self.label_10.setText(_translate("Main", "Presentación:"))
        item = self.TableEntra.horizontalHeaderItem(0)
        item.setText(_translate("Main", "Eliminar"))
        item = self.TableEntra.horizontalHeaderItem(1)
        item.setText(_translate("Main", "Control"))
        item = self.TableEntra.horizontalHeaderItem(2)
        item.setText(_translate("Main", "Origen"))
        item = self.TableEntra.horizontalHeaderItem(3)
        item.setText(_translate("Main", "Clave"))
        item = self.TableEntra.horizontalHeaderItem(4)
        item.setText(_translate("Main", "Descripción"))
        item = self.TableEntra.horizontalHeaderItem(5)
        item.setText(_translate("Main", "Presentación"))
        item = self.TableEntra.horizontalHeaderItem(6)
        item.setText(_translate("Main", "Area Almacen"))
        item = self.TableEntra.horizontalHeaderItem(7)
        item.setText(_translate("Main", "Cantidad"))
        item = self.TableEntra.horizontalHeaderItem(8)
        item.setText(_translate("Main", "Caducidad"))
        item = self.TableEntra.horizontalHeaderItem(9)
        item.setText(_translate("Main", "Lote"))
        item = self.TableEntra.horizontalHeaderItem(10)
        item.setText(_translate("Main", "Fecha"))
        self.label_11.setText(_translate("Main", "Cantidad:"))
        self.label_12.setText(_translate("Main", "Area Almacen:"))
        self.label_13.setText(_translate("Main", "Caducidad:"))
        self.label_14.setText(_translate("Main", "Lote:"))
        self.btnAgregarEntra.setText(_translate("Main", "Agregar"))
        self.btnFinalizarEntra.setText(_translate("Main", "Finalizar"))
        self.DateCaducidadEntra.setDisplayFormat(_translate("Main", "dd/MM/yyyy"))
        self.menuEntradas.setTitle(_translate("Main", "Entradas"))
        self.menuSalidas.setTitle(_translate("Main", "Salidas"))
        self.menuConsultas.setTitle(_translate("Main", "Consultas"))
        self.menuClaves.setTitle(_translate("Main", "Claves"))
        self.toolBar.setWindowTitle(_translate("Main", "toolBar"))
        self.actionEntradas.setText(_translate("Main", "Introduce Entradas"))
        self.actionEntradas.setToolTip(_translate("Main", "Entradas"))
        self.actionEntradas.setShortcut(_translate("Main", "Alt+1"))
        self.actionSalidas.setText(_translate("Main", "Realizar Salidas"))
        self.actionSalidas.setToolTip(_translate("Main", "salidas"))
        self.actionSalidas.setShortcut(_translate("Main", "Alt+2"))
        self.actionkardex.setText(_translate("Main", "Realizar Consultas"))
        self.actionkardex.setToolTip(_translate("Main", "kardex"))
        self.actionkardex.setShortcut(_translate("Main", "Alt+3"))
        self.actionAgregar_claves.setText(_translate("Main", "Introducir Claves"))
        self.actionAgregar_claves.setToolTip(_translate("Main", "Agregar claves"))
        self.actionAgregar_claves.setShortcut(_translate("Main", "Alt+4"))
        self.actionlogo_chiapas.setText(_translate("Main", "logo chiapas"))
        self.actionlogo_chiapas.setToolTip(_translate("Main", "logo de chiapas"))
        self.actionlogo_secretaria_salud.setText(_translate("Main", "logo secretaria salud"))
        self.actionlogo_secretaria_salud.setToolTip(_translate("Main", "secretaria de salud"))
        self.actionIntroducir_Inventario.setText(_translate("Main", "Introducir Inventario"))
        self.actionSalida_de_inventario.setText(_translate("Main", "Salida de inventario"))
        self.actionConsulta_de_inventario.setText(_translate("Main", "Consulta de inventario"))
        self.actionAgregar_claves_de_inventario.setText(_translate("Main", "Agregar claves de inventario"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())