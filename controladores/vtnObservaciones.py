# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnObservaciones.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Observaciones(object):
    def setupUi(self, Observaciones):
        Observaciones.setObjectName("Observaciones")
        Observaciones.resize(391, 148)
        Observaciones.setMinimumSize(QtCore.QSize(391, 148))
        Observaciones.setMaximumSize(QtCore.QSize(391, 148))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagenes/iconoComentarios.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Observaciones.setWindowIcon(icon)
        Observaciones.setStyleSheet("*{\n"
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
"")
        self.btnAceptarObservaciones = QtWidgets.QPushButton(Observaciones)
        self.btnAceptarObservaciones.setGeometry(QtCore.QRect(130, 100, 111, 31))
        self.btnAceptarObservaciones.setObjectName("btnAceptarObservaciones")
        self.textObservaciones = QtWidgets.QTextEdit(Observaciones)
        self.textObservaciones.setGeometry(QtCore.QRect(10, 30, 371, 61))
        self.textObservaciones.setObjectName("textObservaciones")
        self.label = QtWidgets.QLabel(Observaciones)
        self.label.setGeometry(QtCore.QRect(140, 0, 121, 31))
        self.label.setObjectName("label")
        self.btnAceptarObservaciones.setToolTip('Se añadiran las observaciones al reporte si se indican')
        self.textObservaciones.setToolTip('Añada sus observaciones de la salida para adjuntarlo al reporte')

        self.retranslateUi(Observaciones)
        #self.btnAceptarObservaciones.clicked.connect(Observaciones.close)
        QtCore.QMetaObject.connectSlotsByName(Observaciones)
        Observaciones.setTabOrder(self.textObservaciones, self.btnAceptarObservaciones)

    def retranslateUi(self, Observaciones):
        _translate = QtCore.QCoreApplication.translate
        Observaciones.setWindowTitle(_translate("Observaciones", "Observaciones"))
        self.btnAceptarObservaciones.setText(_translate("Observaciones", "Aceptar"))
        self.btnAceptarObservaciones.setShortcut(_translate("Observaciones", "Enter"))
        self.label.setText(_translate("Observaciones", "<html><head/><body><p>Observaciones</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Observaciones = QtWidgets.QWidget()
    ui = Ui_Observaciones()
    ui.setupUi(Observaciones)
    Observaciones.show()
    sys.exit(app.exec_())
