# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dise�oJOdQKM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 60))
        self.frame_superior.setMaximumSize(QSize(16777215, 60))
        self.frame_superior.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_menu = QPushButton(self.frame_superior)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"Recursos/1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(65, 65))

        self.horizontalLayout_2.addWidget(self.btn_menu)

        self.horizontalSpacer = QSpacerItem(502, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_segundoplano = QPushButton(self.frame_superior)
        self.btn_segundoplano.setObjectName(u"btn_segundoplano")
        self.btn_segundoplano.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"Recursos/minimizar logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_segundoplano.setIcon(icon1)
        self.btn_segundoplano.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btn_segundoplano)

        self.btn_minimizar = QPushButton(self.frame_superior)
        self.btn_minimizar.setObjectName(u"btn_minimizar")
        self.btn_minimizar.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"Recursos/min logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimizar.setIcon(icon2)
        self.btn_minimizar.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btn_minimizar)

        self.btn_maximizar = QPushButton(self.frame_superior)
        self.btn_maximizar.setObjectName(u"btn_maximizar")
        self.btn_maximizar.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"Recursos/maxi_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximizar.setIcon(icon3)
        self.btn_maximizar.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btn_maximizar)

        self.btn_cerrar = QPushButton(self.frame_superior)
        self.btn_cerrar.setObjectName(u"btn_cerrar")
        self.btn_cerrar.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"Recursos/salir logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cerrar.setIcon(icon4)
        self.btn_cerrar.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btn_cerrar)


        self.verticalLayout.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.centralwidget)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_inferior)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(0, 16777215))
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(0, 128, 55);\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Small Fonts\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"color: rgb(0, 128, 55);\n"
"font: 10pt \"Small Fonts\";\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon5 = QIcon()
        icon5.addFile(u"Recursos/home logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(True)
        icon6 = QIcon()
        icon6.addFile(u"Recursos/Captura logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon7 = QIcon()
        icon7.addFile(u"Recursos/imagen logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon8 = QIcon()
        icon8.addFile(u"Recursos/Archivo logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon8)
        self.pushButton_9.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon9 = QIcon()
        icon9.addFile(u"Recursos/ajustes logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon9)
        self.pushButton_10.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.pushButton_10)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_inferior)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QFrame{\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(0, 128, 55);\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Small Fonts\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"color: rgb(0, 128, 55);\n"
"font: 10pt \"Small Fonts\";\n"
"}")
        self.inicio = QWidget()
        self.inicio.setObjectName(u"inicio")
        self.label = QLabel(self.inicio)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 20, 281, 41))
        self.label.setStyleSheet(u"background: #000000ff;\n"
"font: 20pt \"Nexa-Bold\";\n"
"color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.inicio)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(90, 80, 331, 321))
        self.label_7.setPixmap(QPixmap(u"Recursos/1.png"))
        self.label_7.setScaledContents(True)
        self.label_8 = QLabel(self.inicio)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(540, 10, 231, 51))
        self.label_8.setStyleSheet(u"background: #000000ff;\n"
"font: 16pt \"Nexa-Bold\";\n"
"color: rgb(255, 255, 255);")
        self.label_9 = QLabel(self.inicio)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(540, 80, 211, 241))
        self.label_9.setPixmap(QPixmap(u"Recursos/OpenBill (6).png"))
        self.label_9.setScaledContents(True)
        self.stackedWidget.addWidget(self.inicio)
        self.capturar = QWidget()
        self.capturar.setObjectName(u"capturar")
        self.camara = QLabel(self.capturar)
        self.camara.setObjectName(u"camara")
        self.camara.setGeometry(QRect(120, 60, 271, 351))
        self.camara.setStyleSheet(u"border: 1px solid rgb(0, 128, 55)")
        self.camara.setScaledContents(True)
        self.btn_capturar = QPushButton(self.capturar)
        self.btn_capturar.setObjectName(u"btn_capturar")
        self.btn_capturar.setGeometry(QRect(60, 470, 141, 31))
        self.btn_volver = QPushButton(self.capturar)
        self.btn_volver.setObjectName(u"btn_volver")
        self.btn_volver.setGeometry(QRect(310, 470, 141, 31))
        self.label_3 = QLabel(self.capturar)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 20, 251, 31))
        self.label_3.setStyleSheet(u"background: #000000ff;\n"
"font: 20pt \"Nexa-Bold\";\n"
"color: rgb(255, 255, 255)")
        self.label_10 = QLabel(self.capturar)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(530, 20, 231, 51))
        self.label_10.setStyleSheet(u"background: #000000ff;\n"
"font: 16pt \"Nexa-Bold\";\n"
"color: rgb(255, 255, 255);")
        self.btn_on = QPushButton(self.capturar)
        self.btn_on.setObjectName(u"btn_on")
        self.btn_on.setGeometry(QRect(120, 420, 131, 31))
        self.btn_off = QPushButton(self.capturar)
        self.btn_off.setObjectName(u"btn_off")
        self.btn_off.setGeometry(QRect(260, 420, 131, 31))
        self.label_11 = QLabel(self.capturar)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(530, 80, 221, 231))
        self.label_11.setPixmap(QPixmap(u"Recursos/OpenBill (7).png"))
        self.label_11.setScaledContents(True)
        self.stackedWidget.addWidget(self.capturar)
        self.selec_foto = QWidget()
        self.selec_foto.setObjectName(u"selec_foto")
        self.label_4 = QLabel(self.selec_foto)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(150, 30, 221, 41))
        self.label_4.setStyleSheet(u"background: #000000ff;\n"
"font: 20pt \"Nexa-Bold\";\n"
"color: rgb(255, 255, 255);")
        self.prev_foto = QLabel(self.selec_foto)
        self.prev_foto.setObjectName(u"prev_foto")
        self.prev_foto.setGeometry(QRect(140, 90, 261, 271))
        self.prev_foto.setStyleSheet(u"border: 1px solid rgb(0, 128, 55)")
        self.prev_foto.setScaledContents(True)
        self.btn_seleccionar = QPushButton(self.selec_foto)
        self.btn_seleccionar.setObjectName(u"btn_seleccionar")
        self.btn_seleccionar.setGeometry(QRect(220, 380, 101, 31))
        self.btn_search = QPushButton(self.selec_foto)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setGeometry(QRect(90, 440, 111, 31))
        self.bnt_volver2 = QPushButton(self.selec_foto)
        self.bnt_volver2.setObjectName(u"bnt_volver2")
        self.bnt_volver2.setGeometry(QRect(320, 440, 121, 31))
        self.label_12 = QLabel(self.selec_foto)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(570, 30, 231, 51))
        self.label_12.setStyleSheet(u"background: #000000ff;\n"
"font: 16pt \"Nexa-Bold\";\n"
"color: rgb(255, 255, 255);")
        self.label_13 = QLabel(self.selec_foto)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(540, 80, 231, 251))
        self.label_13.setPixmap(QPixmap(u"Recursos/OpenBill (8).png"))
        self.label_13.setScaledContents(True)
        self.stackedWidget.addWidget(self.selec_foto)
        self.selec_archivo = QWidget()
        self.selec_archivo.setObjectName(u"selec_archivo")
        self.prev_file = QLabel(self.selec_archivo)
        self.prev_file.setObjectName(u"prev_file")
        self.prev_file.setGeometry(QRect(140, 100, 211, 241))
        self.prev_file.setStyleSheet(u"border: 1px solid rgb(0, 128, 55);")
        self.prev_file.setScaledContents(True)
        self.btn_search2 = QPushButton(self.selec_archivo)
        self.btn_search2.setObjectName(u"btn_search2")
        self.btn_search2.setGeometry(QRect(420, 370, 75, 23))
        self.btn_aceptar = QPushButton(self.selec_archivo)
        self.btn_aceptar.setObjectName(u"btn_aceptar")
        self.btn_aceptar.setGeometry(QRect(90, 440, 121, 31))
        self.btn_volver3 = QPushButton(self.selec_archivo)
        self.btn_volver3.setObjectName(u"btn_volver3")
        self.btn_volver3.setGeometry(QRect(270, 440, 121, 31))
        self.file_path = QLineEdit(self.selec_archivo)
        self.file_path.setObjectName(u"file_path")
        self.file_path.setGeometry(QRect(20, 370, 391, 20))
        self.label_5 = QLabel(self.selec_archivo)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 30, 281, 31))
        self.label_5.setStyleSheet(u"background: #000000ff;\n"
"font: 20pt \"Nexa-Bold\";\n"
"color: rgb(255, 255, 255);")
        self.label_14 = QLabel(self.selec_archivo)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(550, 20, 231, 51))
        self.label_14.setStyleSheet(u"background: #000000ff;\n"
"font: 16pt \"Nexa-Bold\";\n"
"color: rgb(255, 255, 255);")
        self.label_15 = QLabel(self.selec_archivo)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(550, 80, 221, 231))
        self.label_15.setPixmap(QPixmap(u"Recursos/OpenBill (9).png"))
        self.label_15.setScaledContents(True)
        self.stackedWidget.addWidget(self.selec_archivo)
        self.ajustes = QWidget()
        self.ajustes.setObjectName(u"ajustes")
        self.label_2 = QLabel(self.ajustes)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 50, 361, 51))
        self.label_2.setStyleSheet(u"background: #000000ff;\n"
"font: 20pt \"Nexa-Bold\";\n"
"\n"
"color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.ajustes)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(90, 130, 311, 301))
        self.label_6.setTextFormat(Qt.PlainText)
        self.label_6.setPixmap(QPixmap(u"Recursos/1.png"))
        self.label_6.setScaledContents(True)
        self.label_16 = QLabel(self.ajustes)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(550, 100, 211, 201))
        self.label_16.setPixmap(QPixmap(u"Recursos/OpenBill.png"))
        self.label_16.setScaledContents(True)
        self.stackedWidget.addWidget(self.ajustes)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame_inferior)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText("")
        self.btn_segundoplano.setText("")
        self.btn_minimizar.setText("")
        self.btn_maximizar.setText("")
        self.btn_cerrar.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"INICIO", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"CAPTURAR FOTO", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"SELECCIONAR FOTO", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"SELECCIONAR ARCHIVO", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"AJUSTES", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bienvenido de nuevo!!", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"SIGUE LOS PASOS", None))
        self.label_9.setText("")
        self.camara.setText("")
        self.btn_capturar.setText(QCoreApplication.translate("MainWindow", u"CAPTURAR", None))
        self.btn_volver.setText(QCoreApplication.translate("MainWindow", u"VOLVER", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Capturar Imagen", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"SIGUE LOS PASOS", None))
        self.btn_on.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.btn_off.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label_11.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Seleccionar foto", None))
        self.prev_foto.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_seleccionar.setText(QCoreApplication.translate("MainWindow", u"SELECCIONAR", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"BUSCAR IMAGEN", None))
        self.bnt_volver2.setText(QCoreApplication.translate("MainWindow", u"VOLVER", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"SIGUE LOS PASOS", None))
        self.label_13.setText("")
        self.prev_file.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_search2.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.btn_aceptar.setText(QCoreApplication.translate("MainWindow", u"ACEPTAR", None))
        self.btn_volver3.setText(QCoreApplication.translate("MainWindow", u"VOLVER", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Archivo", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"SIGUE LOS PASOS", None))
        self.label_15.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Estamos mejorando por ti...", None))
        self.label_6.setText("")
        self.label_16.setText("")
    # retranslateUi

