# Form implementation generated from reading ui file 'C:\Users\nesto\OneDrive - Universidad de la Sabana\Diseño proyecto final\Diseno\DAgregarInscripcion.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AgregarInscripciones(object):
    def setupUi(self, AgregarInscripciones):
        AgregarInscripciones.setObjectName("AgregarInscripciones")
        AgregarInscripciones.resize(552, 490)
        self.centralwidget = QtWidgets.QWidget(parent=AgregarInscripciones)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 80, 431, 185))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.PBSalir = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.PBSalir.setObjectName("PBSalir")
        self.gridLayout.addWidget(self.PBSalir, 5, 0, 1, 1)
        self.CodigoACtividad = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.CodigoACtividad.setMaximum(999999999)
        self.CodigoACtividad.setObjectName("CodigoACtividad")
        self.gridLayout.addWidget(self.CodigoACtividad, 3, 1, 1, 1)
        self.CodigoAdulto = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.CodigoAdulto.setMaximum(999999999)
        self.CodigoAdulto.setObjectName("CodigoAdulto")
        self.gridLayout.addWidget(self.CodigoAdulto, 2, 1, 1, 1)
        self.PBAgregar = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.PBAgregar.setObjectName("PBAgregar")
        self.gridLayout.addWidget(self.PBAgregar, 5, 1, 1, 1)
        self.Calificacion = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.Calificacion.setMaximum(10)
        self.Calificacion.setObjectName("Calificacion")
        self.gridLayout.addWidget(self.Calificacion, 4, 1, 1, 1)
        self.LTitulo = QtWidgets.QLabel(parent=self.layoutWidget)
        self.LTitulo.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LTitulo.setFont(font)
        self.LTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LTitulo.setObjectName("LTitulo")
        self.gridLayout.addWidget(self.LTitulo, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_4.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.CBCali = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.CBCali.setObjectName("CBCali")
        self.gridLayout.addWidget(self.CBCali, 4, 2, 1, 1)
        AgregarInscripciones.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=AgregarInscripciones)
        self.statusbar.setObjectName("statusbar")
        AgregarInscripciones.setStatusBar(self.statusbar)

        self.retranslateUi(AgregarInscripciones)
        QtCore.QMetaObject.connectSlotsByName(AgregarInscripciones)

    def retranslateUi(self, AgregarInscripciones):
        _translate = QtCore.QCoreApplication.translate
        AgregarInscripciones.setWindowTitle(_translate("AgregarInscripciones", "MainWindow"))
        self.PBSalir.setText(_translate("AgregarInscripciones", "Salir"))
        self.PBAgregar.setText(_translate("AgregarInscripciones", "Agregar"))
        self.LTitulo.setText(_translate("AgregarInscripciones", "Agregar Inscripcion"))
        self.label_2.setText(_translate("AgregarInscripciones", "Codigo Adulto"))
        self.label_3.setText(_translate("AgregarInscripciones", "Codigo Actividad"))
        self.label_4.setText(_translate("AgregarInscripciones", "Calificacion"))
        self.CBCali.setText(_translate("AgregarInscripciones", "No hay calificacion"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AgregarInscripciones = QtWidgets.QMainWindow()
    ui = Ui_AgregarInscripciones()
    ui.setupUi(AgregarInscripciones)
    AgregarInscripciones.show()
    sys.exit(app.exec())
