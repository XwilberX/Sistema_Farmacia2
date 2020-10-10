from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, MetaData, Table,DateTime, Date , ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from PyQt5.QtWidgets import  QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import winsound
import sys
sys.path.append('../Modelo/')
from farm import Clave
from vtnConfirmacion import Ui_vtnDatosCorrectos
import pymysql

engine = create_engine('mysql+pymysql://root:wil99@localhost/farmaciaDB')
Session = sessionmaker(bind=engine)
session = Session()


class SubWindow(QWidget):
    def createSubWindow(self):
        self.setObjectName("InterFazClave")
        self.resize(1034, 687)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagenes/medicina.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size: 15px;\n"
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
"\n"
"\n"
"QPushButton:hover{\n"
"background:#dea806;\n"
"}")
        self.frame_3 = QtWidgets.QFrame(self)
        self.frame_3.setGeometry(QtCore.QRect(220, 30, 561, 561))
        self.frame_3.setStyleSheet("\n"
" background:#fefefe;\n"
"\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.btnFinalizarClave = QtWidgets.QPushButton(self.frame_3)
        self.btnFinalizarClave.setGeometry(QtCore.QRect(210, 460, 141, 31))
        self.btnFinalizarClave.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background:#ffc001;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background:#dea806;\n"
"}\n"
"")
        self.btnFinalizarClave.setObjectName("btnFinalizarClave")
        self.comboboxClave = QtWidgets.QComboBox(self.frame_3)
        self.comboboxClave.setGeometry(QtCore.QRect(180, 180, 231, 22))
        self.comboboxClave.setObjectName("comboboxClave")
        self.comboboxClave.addItem("")
        self.comboboxClave.addItem("")
        self.label_20 = QtWidgets.QLabel(self.frame_3)
        self.label_20.setGeometry(QtCore.QRect(120, 180, 31, 20))
        self.label_20.setObjectName("label_20")
        self.TextDescriClave = QtWidgets.QTextEdit(self.frame_3)
        self.TextDescriClave.setGeometry(QtCore.QRect(170, 360, 271, 61))
        self.TextDescriClave.setStyleSheet("background-color: rgb(184, 244, 240);")
        self.TextDescriClave.setObjectName("TextDescriClave")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(60, 350, 91, 31))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_3)
        self.label_17.setGeometry(QtCore.QRect(60, 290, 101, 31))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame_3)
        self.label_18.setGeometry(QtCore.QRect(60, 260, 101, 21))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_3)
        self.label_19.setGeometry(QtCore.QRect(60, 220, 101, 21))
        self.label_19.setObjectName("label_19")
        self.LineClaveLClave = QtWidgets.QLineEdit(self.frame_3)
        self.LineClaveLClave.setGeometry(QtCore.QRect(170, 210, 271, 31))
        self.LineClaveLClave.setObjectName("LineClaveLClave")
        self.LineClaveCClave = QtWidgets.QLineEdit(self.frame_3)
        self.LineClaveCClave.setGeometry(QtCore.QRect(170, 250, 271, 31))
        self.LineClaveCClave.setObjectName("LineClaveCClave")
        self.label_21 = QtWidgets.QLabel(self.frame_3)
        self.label_21.setGeometry(QtCore.QRect(170, 20, 211, 31))
        self.label_21.setStyleSheet("font-size:24px;\n"
"color:#005bea;")
        self.label_21.setObjectName("label_21")
        self.TextPresentaClave = QtWidgets.QTextEdit(self.frame_3)
        self.TextPresentaClave.setGeometry(QtCore.QRect(170, 290, 271, 61))
        self.TextPresentaClave.setStyleSheet("background-color: rgb(184, 244, 240);")
        self.TextPresentaClave.setObjectName("TextPresentaClave")
        self.label_22 = QtWidgets.QLabel(self.frame_3)
        self.label_22.setGeometry(QtCore.QRect(220, 60, 121, 111))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("../imagenes/claveproducto.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.comboboxClave.setToolTip('Elegir entre medicamento o material de curacion')
        self.LineClaveLClave.setToolTip('Ingresar calve larga')
        self.LineClaveCClave.setToolTip('Ingresar clave corta')
        self.TextDescriClave.setToolTip('Ingresa la descricion de la clave')
        self.TextPresentaClave.setToolTip('Ingresa la presentacion de la clave')
        self.btnFinalizarClave.setToolTip('Enviar los datos')
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.btnFinalizarClave.clicked.connect(self.GetDatos)


   #funcion para recojer todos los datos y meterlos a la base de datos
    def GetDatos(self):
        try:
                self.tipo = self.comboboxClave.currentIndex()
                self.claveLarga = self.LineClaveLClave.text()
                self.claveCorta = self.LineClaveCClave.text()
                self.presentacion =self.TextPresentaClave.toPlainText()
                self.descripcion = self.TextDescriClave.toPlainText()
                mensaje = ''
                if self.claveLarga == '' or self.claveCorta == '' or  self.presentacion == '' or self.descripcion == '':
                        mensaje = 'Hay un campo vacio'
                        self.mensajeCritico(mensaje)
                        if self.claveLarga =='':
                                self.LineClaveLClave.setFocus()
                        if self.claveCorta == '':
                                self.LineClaveCClave.setFocus()
                        if self.presentacion == '':
                                self.TextPresentaClave.setFocus()
                        if self.descripcion == '':
                                self.TextDescriClave.setFocus()
                ifExistId = session.query(Clave.corta).filter(Clave.corta == self.claveCorta).scalar()
                print(ifExistId)
                if  ifExistId:
                        mensaje = 'ya existe esa clave'
                        self.mensajeCritico(mensaje)
                if ifExistId == None and mensaje!='Hay un campo vacio':
                        winsound.PlaySound("../otros_recursos/audios/hey", winsound.SND_FILENAME)
                        self.ventana = QtWidgets.QDialog()
                        self.vtnConfirmacion = Ui_vtnDatosCorrectos()
                        self.vtnConfirmacion.setupUi(self.ventana)
                        self.ventana.show()
                        self.vtnConfirmacion.btnAceptardialogClave.clicked.connect(self.setDatos)
                        self.vtnConfirmacion.btnCancelardialogClave.clicked.connect(self.cerrarVtn)
                        

        except Exception as e:
                print(e)
              
    def cerrarVtn(self):
        QtWidgets.qApp.activeWindow().close()

    def setDatos(self):
        insertClave = Clave(corta=self.claveCorta,clave=self.claveLarga,descripcion=self.descripcion,presentacion=self.presentacion,tipo=self.tipo)
        session.add(insertClave)
        session.commit()
        self.cerrarVtn()

    def mensajeCritico(self,mensaje):
        error_dialog = QtWidgets.QMessageBox()
        error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
        error_dialog.setText(mensaje)
        error_dialog.setWindowTitle("Error")
        error_dialog.exec()

    def limpiar(self):
        self.btnFinalizarClave.clicked.connect(self.LineClaveLClave.clear)
        self.btnFinalizarClave.clicked.connect(self.LineClaveCClave.clear)
        self.btnFinalizarClave.clicked.connect(self.TextPresentaClave.clear)
        self.btnFinalizarClave.clicked.connect(self.TextDescriClave.clear)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        #self.setWindowTitle(_translate("InterFazClave", "Claves"))
        self.btnFinalizarClave.setText(_translate("InterFazClave", "Aceptar"))
        self.comboboxClave.setItemText(0, _translate("InterFazClave", "Medicina"))
        self.comboboxClave.setItemText(1, _translate("InterFazClave", "Material/Curacion"))
        self.label_20.setText(_translate("InterFazClave", "Tipo:"))
        self.label_16.setText(_translate("InterFazClave", "Descripción:"))
        self.label_17.setText(_translate("InterFazClave", "Presentación:"))
        self.label_18.setText(_translate("InterFazClave", "Clave Corta:"))
        self.label_19.setText(_translate("InterFazClave", "Clave Larga:"))
        self.label_21.setText(_translate("InterFazClave", "La clave es unica"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InterFazClave = QtWidgets.QWidget()
    ui = SubWindow()
    ui.createSubWindow()
    InterFazClave.show()
    sys.exit(app.exec_())
