

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, MetaData, Table,DateTime, Date , ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from PyQt5 import QtCore, QtGui, QtWidgets
from InterfazEntradas import Ui_Main
import pymysql
import sys
sys.path.append('../Modelo/')
from farm import Usuario
user = 'root'
passw = 'admin'
host = 'localhost'
port = '3307'
database = 'farmaciaDB'

engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(user, passw, host, port, database))
Session = sessionmaker(bind=engine)
session = Session()

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(891, 752)
        Login.setMinimumSize(QtCore.QSize(891, 752))
        Login.setMaximumSize(QtCore.QSize(891, 752))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagenes/Mono.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Login.setWindowIcon(icon)
        Login.setStyleSheet("*{\n"
"    font-family:century gothic;\n"
"    font-size: 24px;\n"
"}\n"
"#Login{\n"
"    background: #b8f4f0;\n"
"}\n"
"#frame1{\n"
" background:#fefefe;\n"
"border-radius:50px;\n"
"}\n"
"\n"
"#toolButtonOne{\n"
"    border-radius:60px;\n"
"     background:#fefefe;\n"
"\n"
"}\n"
"\n"
"#label1{\n"
"color:#005bea;\n"
"}\n"
"\n"
"QPushButton{\n"
"border-radius:25px;\n"
"background:#ffc001;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background:#dea806;\n"
"}\n"
"QLineEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    border-bottom: 1px solid black;\n"
"}\n"
"#error{\n"
"    font-size: 18px;\n"
"    color: red;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(220, 90, 451, 471))
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.label1 = QtWidgets.QLabel(self.frame1)
        self.label1.setGeometry(QtCore.QRect(150, 50, 161, 61))
        self.label1.setObjectName("label1")
        self.pushButton = QtWidgets.QPushButton(self.frame1)
        self.pushButton.setGeometry(QtCore.QRect(110, 310, 241, 51))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame1)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 390, 241, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame1)
        self.lineEdit.setGeometry(QtCore.QRect(110, 170, 241, 30))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame1)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 240, 241, 30))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.frame1)
        self.label.setGeometry(QtCore.QRect(50, 240, 41, 31))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../imagenes/1458264596_authorisation_lock_padlock_safe_password_privacy_security_icon-icons.com_55333.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame1)
        self.label_2.setGeometry(QtCore.QRect(50, 170, 41, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../imagenes/Mono.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.error = QtWidgets.QLabel(self.frame1)
        self.error.setGeometry(QtCore.QRect(80, 110, 301, 31))
        self.error.setText("")
        self.error.setObjectName("error")
        self.toolButtonOne = QtWidgets.QToolButton(self.centralwidget)
        self.toolButtonOne.setGeometry(QtCore.QRect(380, 30, 130, 131))
        self.toolButtonOne.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagenes/Mono.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonOne.setIcon(icon1)
        self.toolButtonOne.setIconSize(QtCore.QSize(100, 100))
        self.toolButtonOne.setObjectName("toolButtonOne")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 250, 141, 101))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 201, 401))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../imagenes/decoracion10reves2.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(690, 0, 201, 401))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../imagenes/volteada.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(210, 570, 441, 111))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../imagenes/pastillas123.png"))
        self.label_6.setObjectName("label_6")
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 36))
        self.menubar.setObjectName("menubar")
        Login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        self.pushButton_2.clicked.connect(self.lineEdit.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_2.clear)
        QtCore.QMetaObject.connectSlotsByName(Login)
        Login.setTabOrder(self.lineEdit, self.lineEdit_2)
        Login.setTabOrder(self.lineEdit_2, self.pushButton)
        Login.setTabOrder(self.pushButton, self.pushButton_2)
        Login.setTabOrder(self.pushButton_2, self.toolButtonOne)



        #Al pulsar el boton Aceptar pone a trabajar la funcion
        self.pushButton.clicked.connect(self.ValidacionDeSesion)
        self.lineEdit.returnPressed.connect(self.pressEnter)
        self.lineEdit_2.returnPressed.connect(self.pressEnter)




    def pressEnter(self):
        print('precionaste enter')
        if self.lineEdit.hasFocus():
            self.lineEdit_2.setFocus()
        else:
            self.pushButton.setFocus()


    #funcion para poder iniciar sesion y valida si esta correcto los campos.
    def ValidacionDeSesion(self):

        usuarioInter = str(self.lineEdit.text())
        contrasena = str(self.lineEdit_2.text())
        q = session.query(Usuario.id).filter_by(nombre=usuarioInter, contrasena=contrasena).scalar()
        if q:
            self.ventana = QtWidgets.QMainWindow()
            self.ui=Ui_Main()
            self.ui.setupUi(self.ventana)
            self.ventana.show()
            Login.close()
        else:
             self.error.setText('Usuario o Contraseña Incorrectos')

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Inicio de Sesion"))
        self.label1.setText(_translate("Login", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Bienvenido</span></p></body></html>"))
        self.pushButton.setText(_translate("Login", "Aceptar"))
        self.pushButton.setShortcut(_translate("Login", "Return"))
        self.pushButton_2.setText(_translate("Login", "Cancelar"))
        self.lineEdit.setPlaceholderText(_translate("Login", "Usuario"))
        self.lineEdit_2.setPlaceholderText(_translate("Login", "Contraseña"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
