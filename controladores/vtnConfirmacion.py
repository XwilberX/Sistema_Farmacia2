# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnConfirmacion.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_vtnDatosCorrectos(object):
    def setupUi(self, vtnDatosCorrectos):
        vtnDatosCorrectos.setObjectName("vtnDatosCorrectos")
        vtnDatosCorrectos.setWindowModality(QtCore.Qt.NonModal)
        vtnDatosCorrectos.resize(253, 235)
        vtnDatosCorrectos.setMinimumSize(QtCore.QSize(253, 235))
        vtnDatosCorrectos.setMaximumSize(QtCore.QSize(253, 235))
        vtnDatosCorrectos.setMouseTracking(False)
        vtnDatosCorrectos.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagenes/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        vtnDatosCorrectos.setWindowIcon(icon)
        vtnDatosCorrectos.setAccessibleName("")
        vtnDatosCorrectos.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size: 15px;\n"
"}\n"
"#vtnCantidad{\n"
" background:#fefefe;\n"
"}\n"
"QPushButton{\n"
"border-radius:15px;\n"
"background:#ffc001;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:#dea806;\n"
"}\n"
"QLineEdit{\n"
"    border:none;\n"
"    border-bottom: 1px solid black;\n"
"    background:transparent;\n"
"}\n"
"\n"
"\n"
"")
        vtnDatosCorrectos.setSizeGripEnabled(False)
        vtnDatosCorrectos.setModal(False)
        self.label = QtWidgets.QLabel(vtnDatosCorrectos)
        self.label.setGeometry(QtCore.QRect(40, 10, 171, 61))
        self.label.setObjectName("label")
        self.btnCancelardialogClave = QtWidgets.QPushButton(vtnDatosCorrectos)
        self.btnCancelardialogClave.setGeometry(QtCore.QRect(30, 190, 91, 31))
        self.btnCancelardialogClave.setObjectName("btnCancelardialogClave")
        self.btnAceptardialogClave = QtWidgets.QPushButton(vtnDatosCorrectos)
        self.btnAceptardialogClave.setGeometry(QtCore.QRect(140, 190, 91, 31))
        self.btnAceptardialogClave.setObjectName("btnAceptardialogClave")
        self.label_2 = QtWidgets.QLabel(vtnDatosCorrectos)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 241, 31))
        self.label_2.setStyleSheet("color: rgb(255, 59, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(vtnDatosCorrectos)
        self.label_3.setGeometry(QtCore.QRect(90, 80, 81, 71))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../imagenes/alert_icon_129491.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(vtnDatosCorrectos)
        QtCore.QMetaObject.connectSlotsByName(vtnDatosCorrectos)

    def retranslateUi(self, vtnDatosCorrectos):
        _translate = QtCore.QCoreApplication.translate
        vtnDatosCorrectos.setWindowTitle(_translate("vtnDatosCorrectos", "Confirmacion"))
        self.label.setText(_translate("vtnDatosCorrectos", "<html><head/><body><p><span style=\" font-size:16pt;\">¿Todos los datos</span></p><p><span style=\" font-size:16pt;\">están correctos?</span></p></body></html>"))
        self.btnCancelardialogClave.setText(_translate("vtnDatosCorrectos", "Cancelar"))
        self.btnCancelardialogClave.setShortcut(_translate("vtnDatosCorrectos", "Esc"))
        self.btnAceptardialogClave.setText(_translate("vtnDatosCorrectos", "Aceptar"))
        self.label_2.setText(_translate("vtnDatosCorrectos", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Esta acción es irreversible</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    vtnDatosCorrectos = QtWidgets.QDialog()
    ui = Ui_vtnDatosCorrectos()
    ui.setupUi(vtnDatosCorrectos)
    vtnDatosCorrectos.show()
    sys.exit(app.exec_())
