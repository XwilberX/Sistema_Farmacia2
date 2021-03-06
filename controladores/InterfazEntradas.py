
from sqlalchemy import create_engine
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker, relationship
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QCompleter, QTableView,QHeaderView,QMessageBox, QMdiSubWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import webbrowser as wb
from os import path
import sys
sys.path.append('../Modelo/')
from BusquedaDPview2 import Ui_BDP
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIntValidator
from InterfazSalidas import SubWindow
from interfazClave import SubWindow as vtnClave
from farm import Clave, Farmaco, Entrada
from interfazConsultas import SubWindow as vtnConsultas
from vtnReferencia import Ui_VtnES
import pymysql
import pandas as pd
user = 'root'
passw = 'admin'
host = 'localhost'
port = '3307'
database = 'farmaciaDB'

engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(user, passw, host, port, database))
Session = sessionmaker(bind=engine)
session = Session()

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1291, 911)
        Main.setMaximumSize(QtCore.QSize(1291, 911))
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
        self.label_5.setGeometry(QtCore.QRect(20, 10, 91, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.FrameEntradaprimero)
        self.label_6.setGeometry(QtCore.QRect(650, 40, 71, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.FrameEntradaprimero)
        self.label_7.setGeometry(QtCore.QRect(650, 10, 81, 20))
        self.label_7.setObjectName("label_7")
        self.LineOrigenEntra = QtWidgets.QLineEdit(self.FrameEntradaprimero)
        self.LineOrigenEntra.setGeometry(QtCore.QRect(110, 9, 141, 21))
        self.LineOrigenEntra.setObjectName("LineOrigenEntra")
        self.DateFechaEntra = QtWidgets.QDateEdit(self.FrameEntradaprimero)
        self.DateFechaEntra.setGeometry(QtCore.QRect(740, 40, 121, 22))
        self.DateFechaEntra.setAccelerated(False)
        self.DateFechaEntra.setProperty("showGroupSeparator", False)
        self.DateFechaEntra.setCalendarPopup(True)
        self.DateFechaEntra.setTimeSpec(QtCore.Qt.UTC)
        self.DateFechaEntra.setDate(QtCore.QDate(2020, 1, 1))
        self.DateFechaEntra.setObjectName("DateFechaEntra")
        self.LineControlEntra = QtWidgets.QLineEdit(self.FrameEntradaprimero)
        self.LineControlEntra.setEnabled(False)
        self.LineControlEntra.setGeometry(QtCore.QRect(740, 10, 121, 21))
        self.LineControlEntra.setObjectName("LineControlEntra")
        self.label_15 = QtWidgets.QLabel(self.FrameEntradaprimero)
        self.label_15.setGeometry(QtCore.QRect(330, 40, 41, 20))
        self.label_15.setObjectName("label_15")
        self.comboBoxEntradas = QtWidgets.QComboBox(self.FrameEntradaprimero)
        self.comboBoxEntradas.setGeometry(QtCore.QRect(370, 40, 171, 22))
        self.comboBoxEntradas.setObjectName("comboBoxEntradas")
        self.comboBoxEntradas.addItem("")
        self.comboBoxEntradas.addItem("")
        self.LineReferenciaEntra = QtWidgets.QLineEdit(self.FrameEntradaprimero)
        self.LineReferenciaEntra.setEnabled(True)
        self.LineReferenciaEntra.setGeometry(QtCore.QRect(130, 50, 121, 21))
        self.LineReferenciaEntra.setObjectName("LineReferenciaEntra")
        self.label_16 = QtWidgets.QLabel(self.FrameEntradaprimero)
        self.label_16.setGeometry(QtCore.QRect(20, 50, 101, 20))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.FrameEntradaprimero)
        self.label_17.setGeometry(QtCore.QRect(330, 10, 101, 21))
        self.label_17.setObjectName("label_17")
        self.DateFreferenciaEntra = QtWidgets.QDateEdit(self.FrameEntradaprimero)
        self.DateFreferenciaEntra.setGeometry(QtCore.QRect(430, 10, 110, 24))
        self.DateFreferenciaEntra.setAccelerated(False)
        self.DateFreferenciaEntra.setProperty("showGroupSeparator", False)
        self.DateFreferenciaEntra.setCalendarPopup(True)
        self.DateFreferenciaEntra.setTimeSpec(QtCore.Qt.UTC)
        self.DateFreferenciaEntra.setDate(QtCore.QDate(2020, 1, 1))
        self.DateFreferenciaEntra.setObjectName("DateFreferenciaEntra")
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
        self.label_8.setGeometry(QtCore.QRect(50, 20, 81, 21))
        self.label_8.setObjectName("label_8")
        self.LineClaveEntra = QtWidgets.QLineEdit(self.frame_2)
        self.LineClaveEntra.setGeometry(QtCore.QRect(100, 10, 191, 31))
        self.LineClaveEntra.setObjectName("LineClaveEntra")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(360, 20, 101, 21))
        self.label_9.setObjectName("label_9")
        self.TextDescriEntra = QtWidgets.QTextEdit(self.frame_2)
        self.TextDescriEntra.setEnabled(False)
        self.TextDescriEntra.setGeometry(QtCore.QRect(460, 10, 301, 51))
        self.TextDescriEntra.setStyleSheet("background-color: rgb(184, 244, 240);\n"
"")
        self.TextDescriEntra.setObjectName("TextDescriEntra")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(360, 80, 101, 21))
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
        self.label_11.setGeometry(QtCore.QRect(20, 60, 71, 21))
        self.label_11.setObjectName("label_11")
        self.LineCantidadEntra = QtWidgets.QLineEdit(self.frame_2)
        self.LineCantidadEntra.setGeometry(QtCore.QRect(100, 60, 191, 20))
        self.LineCantidadEntra.setObjectName("LineCantidadEntra")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(360, 130, 101, 21))
        self.label_12.setObjectName("label_12")
        self.btnClaveEntra = QtWidgets.QPushButton(self.frame_2)
        self.btnClaveEntra.setGeometry(QtCore.QRect(300, 20, 21, 21))
        self.btnClaveEntra.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../imagenes/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClaveEntra.setIcon(icon2)
        self.btnClaveEntra.setIconSize(QtCore.QSize(20, 20))
        self.btnClaveEntra.setObjectName("btnClaveEntra")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(20, 130, 91, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(60, 93, 41, 20))
        self.label_14.setObjectName("label_14")
        self.LineLoteEntra = QtWidgets.QLineEdit(self.frame_2)
        self.LineLoteEntra.setGeometry(QtCore.QRect(100, 90, 191, 21))
        self.LineLoteEntra.setObjectName("LineLoteEntra")
        self.btnFinalizarEntra = QtWidgets.QPushButton(self.frame_2)
        self.btnFinalizarEntra.setGeometry(QtCore.QRect(770, 100, 141, 31))
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
        self.DateCaducidadEntra.setGeometry(QtCore.QRect(120, 130, 171, 22))
        self.DateCaducidadEntra.setCalendarPopup(True)
        self.DateCaducidadEntra.setTimeSpec(QtCore.Qt.LocalTime)
        self.DateCaducidadEntra.setDate(QtCore.QDate(2020, 1, 1))
        self.DateCaducidadEntra.setObjectName("DateCaducidadEntra")
        self.TextPresentaEntra = QtWidgets.QTextEdit(self.frame_2)
        self.TextPresentaEntra.setEnabled(False)
        self.TextPresentaEntra.setGeometry(QtCore.QRect(460, 70, 301, 51))
        self.TextPresentaEntra.setStyleSheet("background-color: rgb(184, 244, 240);\n"
"")
        self.TextPresentaEntra.setObjectName("TextPresentaEntra")
        self.radioButton = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton.setGeometry(QtCore.QRect(470, 130, 91, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_2.setGeometry(QtCore.QRect(580, 130, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.btnAgregarEntra = QtWidgets.QPushButton(self.frame_2)
        self.btnAgregarEntra.setGeometry(QtCore.QRect(770, 60, 141, 31))
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
        self.btnTotalEntradasEntra = QtWidgets.QPushButton(self.frame_2)
        self.btnTotalEntradasEntra.setGeometry(QtCore.QRect(820, 20, 41, 31))
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../imagenes/papeleo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnTotalEntradasEntra.setIcon(icon3)
        self.btnTotalEntradasEntra.setIconSize(QtCore.QSize(30, 30))
        self.btnTotalEntradasEntra.setObjectName("btnTotalEntradasEntra")
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
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(Main)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setObjectName("toolBar")
        Main.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionEntradas = QtWidgets.QAction(Main)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../imagenes/agregar clave (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEntradas.setIcon(icon4)
        self.actionEntradas.setObjectName("actionEntradas")
        self.actionSalidas = QtWidgets.QAction(Main)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../imagenes/medicina.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalidas.setIcon(icon5)
        self.actionSalidas.setObjectName("actionSalidas")
        self.actionkardex = QtWidgets.QAction(Main)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../imagenes/salidas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionkardex.setIcon(icon6)
        self.actionkardex.setObjectName("actionkardex")
        self.actionAgregar_claves = QtWidgets.QAction(Main)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../imagenes/agregar clave (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAgregar_claves.setIcon(icon7)
        self.actionAgregar_claves.setObjectName("actionAgregar_claves")
        self.actionAyuda = QtWidgets.QAction(Main)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../imagenes/manual.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAyuda.setIcon(icon8)
        self.actionAyuda.setObjectName("actionAyuda")
        self.menuEntradas.addAction(self.actionEntradas)
        self.menuSalidas.addAction(self.actionSalidas)
        self.menuConsultas.addAction(self.actionkardex)
        self.menuClaves.addAction(self.actionAgregar_claves)
        self.menuAyuda.addAction(self.actionAyuda)
        self.menubar.addAction(self.menuEntradas.menuAction())
        self.menubar.addAction(self.menuSalidas.menuAction())
        self.menubar.addAction(self.menuConsultas.menuAction())
        self.menubar.addAction(self.menuClaves.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.toolBar.addAction(self.actionEntradas)
        self.toolBar.addAction(self.actionSalidas)
        self.toolBar.addAction(self.actionkardex)
        self.toolBar.addAction(self.actionAgregar_claves)

        self.retranslateUi(Main)
        self.btnFinalizarEntra.clicked.connect(self.LineCantidadEntra.clear)
        self.btnFinalizarEntra.clicked.connect(self.LineLoteEntra.clear)
        self.btnFinalizarEntra.clicked.connect(self.TextDescriEntra.clear)
        self.btnFinalizarEntra.clicked.connect(self.LineClaveEntra.clear)
        self.btnFinalizarEntra.clicked.connect(self.LineOrigenEntra.clear)
        self.btnFinalizarEntra.clicked.connect(self.TextPresentaEntra.clear)
        self.btnFinalizarEntra.clicked.connect(self.LineReferenciaEntra.clear)
        QtCore.QMetaObject.connectSlotsByName(Main)
        Main.setTabOrder(self.LineOrigenEntra, self.LineReferenciaEntra)
        Main.setTabOrder(self.LineReferenciaEntra, self.DateFreferenciaEntra)
        Main.setTabOrder(self.DateFreferenciaEntra, self.comboBoxEntradas)
        Main.setTabOrder(self.comboBoxEntradas, self.LineControlEntra)
        Main.setTabOrder(self.LineControlEntra, self.DateFechaEntra)
        Main.setTabOrder(self.DateFechaEntra, self.LineClaveEntra)
        Main.setTabOrder(self.LineClaveEntra, self.btnClaveEntra)
        Main.setTabOrder(self.btnClaveEntra, self.TextDescriEntra)
        Main.setTabOrder(self.TextDescriEntra, self.TextPresentaEntra)
        Main.setTabOrder(self.TextPresentaEntra, self.LineCantidadEntra)
        Main.setTabOrder(self.LineCantidadEntra, self.LineLoteEntra)
        Main.setTabOrder(self.LineLoteEntra, self.DateCaducidadEntra)
        Main.setTabOrder(self.DateCaducidadEntra, self.radioButton)
        Main.setTabOrder(self.radioButton, self.radioButton_2)
        Main.setTabOrder(self.radioButton_2, self.btnTotalEntradasEntra)
        Main.setTabOrder(self.btnTotalEntradasEntra, self.btnAgregarEntra)
        Main.setTabOrder(self.btnAgregarEntra, self.btnFinalizarEntra)
        Main.setTabOrder(self.btnFinalizarEntra, self.TableEntra)
        self.LineOrigenEntra.setToolTip('Introducir nombre del proveedor')
        self.DateFreferenciaEntra.setToolTip('Introducir fecha de referencia')
        self.LineReferenciaEntra.setToolTip('Introducir numero de referencia')
        self.comboBoxEntradas.setToolTip('Eligir medicamento o material de curación')
        self.LineControlEntra.setToolTip('Numero automatico de la entrada')
        self.DateFechaEntra.setToolTip('Introduccir fecha de entrada')
        self.LineClaveEntra.setToolTip('Clave del medicamento o material de curación')
        self.btnClaveEntra.setToolTip('Abrir ventana para busqueda de claves')
        self.TextDescriEntra.setToolTip('Descripción correspondiente a la clave')
        self.TextPresentaEntra.setToolTip('Presentación correspondiente a la clave')
        self.LineCantidadEntra.setToolTip('Introducir cantidad entrante')
        self.LineLoteEntra.setToolTip('Introducir lote')
        self.DateCaducidadEntra.setToolTip('Introducir fecha de caducidad del medicamento o material de curación')
        self.btnTotalEntradasEntra.setToolTip('Abrir ventana para modificar entradas ya hechas')
        self.btnAgregarEntra.setToolTip('Agregar farmaco')
        self.btnFinalizarEntra.setToolTip('Guardar los medicamentos y materiales de curación que se han introducido')


        #comente el nombre de todos los titulos de cada pestaña para que no se pusieraS
        #agregando subwindow entrada ,Qt.WindowTitleHint para que no pueda minizar ni cerrar la subwindow
        self.mdiArea.addSubWindow(self.subwindowEntradas,Qt.WindowTitleHint)
        self.subwindowEntradas.showMaximized()

        # Agregando subwindow de salida  , se le coloca ,Qt.WindowTitleHint para que no pueda minizar ni cerrar la subwindow
        self.uiSalida = SubWindow()
        self.uiSalida.createSubWindow()
        self.mdiArea.addSubWindow(self.uiSalida,Qt.WindowTitleHint)

        #agregando subwindow Claves ,Qt.WindowTitleHint para que no pueda minizar ni cerrar la subwindow
        self.uiClave = vtnClave()
        self.uiClave.createSubWindow()
        self.mdiArea.addSubWindow(self.uiClave,Qt.WindowTitleHint)

        #agregando subwindow Consultas ,Qt.WindowTitleHint para que no pueda minizar ni cerrar la subwindow
        self.uiConsulta = vtnConsultas()
        self.uiConsulta.createSubWindow()
        self.mdiArea.addSubWindow(self.uiConsulta,Qt.WindowTitleHint)

        self.radioButton.setChecked(True)
        

        self.mdiArea.activateNextSubWindow()
        
        #inicio del codigo
        # Para que aparezca la ventana de entradas al iniciar

        self.actionEntradas.triggered.connect(self.abrirVentana)
        self.actionSalidas.triggered.connect(self.abrirSalidas)
        self.actionAgregar_claves.triggered.connect(self.abrirClaves)
        self.actionkardex.triggered.connect(self.abrirConsultas)
        self.actionAyuda.triggered.connect(self.manual)


        #agregar Items a la tabla de Entradas
        self.btnAgregarEntra.clicked.connect(self.enviar)


        #aumentar el numero de control
        self.conta = 0
        self.control()

        #coloca la fecha actual en los QdateEdit
        now = datetime.now()
        self.DateCaducidadEntra.setDate(now)
        self.DateFechaEntra.setDate(now)
        self.DateFreferenciaEntra.setDate(now)
        
        #Busqueda en tiempo real
        self.BusquedaTreal()
        #pone la desc y presentacion en los textEdit
        self.LineClaveEntra.returnPressed.connect(self.ConsultaDesc)
        #abre la ventana para buscar por DESC o PRESENTACION
        self.btnClaveEntra.clicked.connect(self.BusquedaDP)


        self.btnFinalizarEntra.clicked.connect(self.FinalizarTabla)
        
        #hace que el LineEdit solo puedan introducir numeros
        intonly = QIntValidator()
        self.LineCantidadEntra.setValidator(intonly)

        self.comboBoxEntradas.currentIndexChanged.connect(self.BusquedaTreal)
        self.btnTotalEntradasEntra.clicked.connect(self.openRef)
        self.EnOsal=1
        

#FUNCIONES
    # VER QUE BORRE EL FINALIZAR Y EL AGREGAR
    def abrirConsultas(self):
        self.subwindowEntradas.hide()
        self.uiClave.hide()
        self.uiSalida.hide()
        self.uiConsulta.showMaximized()
        if self.uiConsulta.isVisible():
                self.uiConsulta.consultar()
    def abrirClaves(self):
        self.uiConsulta.hide()
        self.subwindowEntradas.hide()
        self.uiSalida.hide()
        self.uiClave.showMaximized()
    def abrirSalidas(self):
        self.uiConsulta.hide()
        self.uiClave.hide()
        self.subwindowEntradas.hide()
        self.uiSalida.showMaximized()
        if self.uiSalida.isVisible() == True:
                self.uiSalida.update()
    def abrirVentana(self):
        self.uiConsulta.hide()
        self.uiClave.hide()
        self.uiSalida.hide()
        self.subwindowEntradas.showMaximized()
        if self.subwindowEntradas.isVisible():
                self.BusquedaTreal()
    def FinalizarTabla(self):
        try:
            self.Dp = pd.DataFrame()
            DpEntrada = pd.DataFrame()
            rows = self.TableEntra.rowCount()
            # print(rows)
            Column = self.TableEntra.columnCount()
            # print(Column)
            #TUVIMOS QUE ARREGLAR EL ORDEN DE LOS HEADERS PARA QUE JALE LA CONSULTA JUSTO CON LA TABLA DE BD Y EL DATAFRAME
            headers = ['origen', 'clave_corta', 'area','cantidad','caducidad','lote','fechaIngreso']
            for i in range(rows):
                for j in range(Column):
                    print(j)
                    #Este If es por que no necesitamos las columnas de descripcion y presentacion en el ingreso al DATAFRAME ya que al ingresar el dataframe a la BD no estan esos campos
                    if j != 4 and j != 5 and j != 0 and j != 1:
                        self.Dp.loc[i,j] = self.TableEntra.item(i,j).text()
            self.Dp.columns =headers
            #print(Dp)
            #Ingreso DEl dataframe a la bd tipo ingreso pandas(NO SQLALCHEMY) a la tabla farmaco
            self.Dp.to_sql('farmaco', engine, index= False, if_exists="append")
            print((self.Dp))

            #Tabla de entrada en la base de datos
            headers1 = ['NoReferencia', 'FeReferencia', 'FeEntrada','origen']
            DpEntrada.loc[0,1] = self.referencia
            Date =  self.DateFreferenciaEntra.date()
            fechaReferencia = Date.toPyDate()
            DpEntrada.loc[0,2] = str(fechaReferencia)
            Date =  self.DateFechaEntra.date()
            fechaEntrada = Date.toPyDate()
            DpEntrada.loc[0,3] = str(fechaEntrada)
            DpEntrada.loc[0,4] = self.origen
            DpEntrada.columns =headers1
            print(DpEntrada)
            DpEntrada.to_sql('entrada',engine, index= False, if_exists="append")
            session.close()

            self.insertRecord()
            
            for i in reversed(range(self.TableEntra.rowCount())):
                self.TableEntra.removeRow(i)
            self.conta= 0
            self.control()
            session.close()
            self.TextPresentaEntra.setText('')
            self.LineCantidadEntra.setText('')
            self.LineLoteEntra.setText('')
            self.TextDescriEntra.setText('')
            self.LineClaveEntra.setText('')
            self.LineOrigenEntra.setText('')

        except Exception as e:
            print(e)
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
            tipos = self.comboBoxEntradas.currentIndex()
            Vclave = self.LineClaveEntra.text()
            if tipos == 0:
                Desc = session.query(Clave.descripcion, Clave.presentacion).filter_by(corta=Vclave, tipo=0).one()
            if tipos == 1:
                Desc = session.query(Clave.descripcion, Clave.presentacion).filter_by(corta=Vclave, tipo=1).one()

            # print(Desc[0])
            # print(Desc[1])
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
        #self.Ncontrol = session.query(func.max(Entrada.NoEntrada)).scalar()
        #self.conta = 1
        self.Ncontrol = session.execute("""
    SELECT AUTO_INCREMENT
    FROM information_schema.TABLES
    WHERE TABLE_SCHEMA = "farmaciadb"
    AND TABLE_NAME = "entrada"
""").scalar()
 

        self.LineControlEntra.setText(str(self.Ncontrol))
        session.close()

    def queryClave(self):
            tipos = self.comboBoxEntradas.currentIndex()
            if tipos == 0:
                    self.clave123 = session.query(Clave.corta).filter_by(tipo=0).all()
            if tipos == 1:
                    self.clave123 = session.query(Clave.corta).filter_by(tipo=1).all()
            session.commit()

    # busqueda en tiempo real
    def BusquedaTreal(self):
            self.queryClave()
            list = []
            for n in self.clave123:
                    for c in n:
                            list.append(c)
            ListaClave = list
            completer = QCompleter(ListaClave)
            self.LineClaveEntra.setCompleter(completer)

    #Envia los datos a la tabla
    def enviar(self):
        error_dialog = QtWidgets.QMessageBox()
        error_dialog.setIcon(QtWidgets.QMessageBox.Information)
        #que no pueda poner una cantidad vacia
        if self.LineCantidadEntra.text() == "" or self.LineCantidadEntra.text == "0":
            self.LineCantidadEntra.setFocus()
            error_dialog.setText("Cantidad vacia")
            if self.LineCantidadEntra.text() == "0":
                error_dialog.setText("Introduzca un numero mayor")
            error_dialog.setWindowTitle("Error")
            error_dialog.exec()
        elif self.LineClaveEntra.text() == "":
            self.LineClaveEntra.setStyleSheet("QLineEdit { border-color: red;}")
            self.LineClaveEntra.setFocus()
            error_dialog.setText("Clave vacia")
            error_dialog.setWindowTitle("Error")
            error_dialog.exec()
        if self.LineCantidadEntra.text() != "" and self.LineCantidadEntra.text != "0" and self.LineClaveEntra.text() != "" :
            row = self.TableEntra.rowCount()
            rowPosition = self.TableEntra.rowCount()
            self.TableEntra.insertRow(rowPosition)
            #cambio el formato de fecha
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
            
            #Ver que opcion hay en Area de resguardo
            if self.radioButton.isChecked():
                resguardo = 'Almacen'
            else:
                resguardo = 'Bodega'

            self.TableEntra.setCellWidget(row,0,self.btnDelete)
            
            self.TableEntra.setItem(row, 1, QTableWidgetItem(
                str(self.LineControlEntra.text())))
            self.TableEntra.setItem(row, 2, QTableWidgetItem(
                str(self.LineOrigenEntra.text())))
            self.TableEntra.setItem(row, 3, QTableWidgetItem(
                str(self.LineClaveEntra.text())))
            self.TableEntra.setItem(row, 4, QTableWidgetItem(
                str(self.TextDescriEntra.toPlainText())))
            self.TableEntra.item(row, 4).setToolTip(str(self.TextDescriEntra.toPlainText()))
            self.TableEntra.setItem(row, 5, QTableWidgetItem(
                str(self.TextPresentaEntra.toPlainText())))
            self.TableEntra.item(row, 5).setToolTip(str(self.TextPresentaEntra.toPlainText()))
            self.TableEntra.setItem(row, 6, QTableWidgetItem(resguardo))
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
            self.LineLoteEntra.setText('')
            self.LineCantidadEntra.setText('')
            self.TextDescriEntra.setText('')
            self.LineClaveEntra.setText('')
            self.TextPresentaEntra.setText('')
            self.referencia =  self.LineReferenciaEntra.text()
            self.origen = self.LineOrigenEntra.text()

    #Elimina las filas del tablewitget
    def contador(self):
        rowC = self.TableEntra.currentRow()
        self.TableEntra.removeRow(rowC)
        #self.conta = self.conta - 1
        #self.LineControlEntra.setText(str(self.Ncontrol + self.conta))
        row2 = self.TableEntra.rowCount()
        for a in range(row2):
                if a >= rowC:
                        hola = int(self.TableEntra.item(a,1).text())
                        pedro = hola - 1 
                        self.TableEntra.setItem(a,1,QTableWidgetItem(str(pedro)))

    def manual(self):
        Nombre_pdf ='manual.pdf'
        Nombre_pdf = path.abspath(Nombre_pdf)
        wb.open_new(r'%s'%Nombre_pdf)
        # print(path.abspath(Nombre_pdf))

    def insertRecord(self):
        # Ingreso DEl dataframe a la bd tipo ingreso pandas(NO SQLALCHEMY) pero a la tabla historial
        self.Dp['Entrada_NoEntrada'] = session.query(func.max(Entrada.NoEntrada)).scalar()
        self.Dp.to_sql('historial', engine, index=False, if_exists="append")
        self.Dp.drop(columns=['Entrada_NoEntrada'])
        session.close()

    def openRef(self):
        self.vtnRef = QtWidgets.QWidget()
        self.uiRef = Ui_VtnES(self.EnOsal)
        self.uiRef.setupUi(self.vtnRef)
        self.vtnRef.show()



    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Sistema de Inventario"))
        #self.subwindowEntradas.setWindowTitle(_translate("Main", "Entradas"))
        self.label_5.setText(_translate("Main", "Proveedor:"))
        self.label_6.setText(_translate("Main", "F.Entrada:"))
        self.label_7.setText(_translate("Main", "N.Entrada:"))
        self.DateFechaEntra.setDisplayFormat(_translate("Main", "dd/MM/yyyy"))
        self.label_15.setText(_translate("Main", "Tipo:"))
        self.comboBoxEntradas.setItemText(0, _translate("Main", "Medicamento"))
        self.comboBoxEntradas.setItemText(1, _translate("Main", "M.Curacion"))
        self.label_16.setText(_translate("Main", "N.Referencia:"))
        self.label_17.setText(_translate("Main", "F.Referencia:"))
        self.DateFreferenciaEntra.setDisplayFormat(_translate("Main", "dd/MM/yyyy"))
        self.label_8.setText(_translate("Main", "Clave:"))
        self.label_9.setText(_translate("Main", "Descripción :"))
        self.label_10.setText(_translate("Main", "Presentación:"))
        item = self.TableEntra.horizontalHeaderItem(0)
        item.setText(_translate("Main", "Eliminar"))
        item = self.TableEntra.horizontalHeaderItem(1)
        item.setText(_translate("Main", "N.Entrada"))
        item = self.TableEntra.horizontalHeaderItem(2)
        item.setText(_translate("Main", "Proveedor"))
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
        self.label_12.setText(_translate("Main", "A.resguardo:"))
        self.label_13.setText(_translate("Main", "Caducidad:"))
        self.label_14.setText(_translate("Main", "Lote:"))
        self.btnFinalizarEntra.setText(_translate("Main", "Finalizar"))
        self.DateCaducidadEntra.setDisplayFormat(_translate("Main", "dd/MM/yyyy"))
        self.radioButton.setText(_translate("Main", "Almacen"))
        self.radioButton_2.setText(_translate("Main", "Bodega"))
        self.btnAgregarEntra.setText(_translate("Main", "Agregar"))
        #self.pushButto.setShortcut(_translate("Main", "Enter"))
        self.btnTotalEntradasEntra.setShortcut(_translate("Main", "Ctrl+E"))
        self.menuEntradas.setTitle(_translate("Main", "Entradas"))
        self.menuSalidas.setTitle(_translate("Main", "Salidas"))
        self.menuConsultas.setTitle(_translate("Main", "Consultas"))
        self.menuClaves.setTitle(_translate("Main", "Claves"))
        self.menuAyuda.setTitle(_translate("Main", "Ayuda"))
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
        self.actionAyuda.setText(_translate("Main", "Ayuda"))
        self.actionAyuda.setToolTip(_translate("Main", "Ayuda"))
        self.actionAyuda.setShortcut(_translate("Main", "Alt+5"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
