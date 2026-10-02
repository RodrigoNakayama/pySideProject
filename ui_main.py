# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menuprinc.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import myrecursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(955, 600)
        MainWindow.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftContainer = QFrame(self.centralwidget)
        self.leftContainer.setObjectName(u"leftContainer")
        self.leftContainer.setMaximumSize(QSize(200, 16777215))
        self.leftContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.leftContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.leftContainer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QPushButton:hover {\n"
"   background-color: rgb(65, 65, 65);\n"
"   border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 156, 434))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_Home = QPushButton(self.page)
        self.btn_Home.setObjectName(u"btn_Home")
        self.btn_Home.setMinimumSize(QSize(0, 30))
        self.btn_Home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_Home.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_Home)

        self.btn_Cadastrar = QPushButton(self.page)
        self.btn_Cadastrar.setObjectName(u"btn_Cadastrar")
        self.btn_Cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_Cadastrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_Cadastrar)

        self.btn_Contato = QPushButton(self.page)
        self.btn_Contato.setObjectName(u"btn_Contato")
        self.btn_Contato.setMinimumSize(QSize(0, 30))
        self.btn_Contato.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_Contato)

        self.btn_Sobre = QPushButton(self.page)
        self.btn_Sobre.setObjectName(u"btn_Sobre")
        self.btn_Sobre.setMinimumSize(QSize(0, 30))
        self.btn_Sobre.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_Sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 156, 434))
        self.toolBox.addItem(self.page_2, u"Page 2")

        self.horizontalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.leftContainer)

        self.mainContainer = QFrame(self.centralwidget)
        self.mainContainer.setObjectName(u"mainContainer")
        self.mainContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.mainContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frmHeader = QFrame(self.mainContainer)
        self.frmHeader.setObjectName(u"frmHeader")
        self.frmHeader.setFrameShape(QFrame.Shape.StyledPanel)
        self.frmHeader.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frmHeader)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frmHeader)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frmHeader)

        self.frmMain = QFrame(self.mainContainer)
        self.frmMain.setObjectName(u"frmMain")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmMain.sizePolicy().hasHeightForWidth())
        self.frmMain.setSizePolicy(sizePolicy)
        self.frmMain.setFrameShape(QFrame.Shape.StyledPanel)
        self.frmMain.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frmMain)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Pages = QStackedWidget(self.frmMain)
        self.Pages.setObjectName(u"Pages")
        self.pgContatos = QWidget()
        self.pgContatos.setObjectName(u"pgContatos")
        self.label_8 = QLabel(self.pgContatos)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(110, 60, 111, 16))
        self.label_11 = QLabel(self.pgContatos)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(70, 90, 31, 31))
        self.label_12 = QLabel(self.pgContatos)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(110, 100, 161, 16))
        self.label_14 = QLabel(self.pgContatos)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(110, 140, 49, 16))
        self.label_7 = QLabel(self.pgContatos)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 50, 31, 31))
        self.label_13 = QLabel(self.pgContatos)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(70, 130, 31, 31))
        self.Pages.addWidget(self.pgContatos)
        self.pgSobre = QWidget()
        self.pgSobre.setObjectName(u"pgSobre")
        self.verticalLayout_9 = QVBoxLayout(self.pgSobre)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_9 = QLabel(self.pgSobre)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_9.addWidget(self.label_9)

        self.label_10 = QLabel(self.pgSobre)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_10)

        self.Pages.addWidget(self.pgSobre)
        self.pgCadastrar = QWidget()
        self.pgCadastrar.setObjectName(u"pgCadastrar")
        self.verticalLayout_6 = QVBoxLayout(self.pgCadastrar)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.pgCadastrar)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.tabWidget = QTabWidget(self.pgCadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_4 = QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_4.addWidget(self.tableWidget)

        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_6 = QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_7.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_7.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_3)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_7.addWidget(self.pushButton_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addWidget(self.frame_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_4 = QFrame(self.tab_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_9 = QLineEdit(self.frame_4)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout.addWidget(self.lineEdit_9, 4, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 3, 4, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 4, 2, 1, 2)

        self.lineEdit_8 = QLineEdit(self.frame_4)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout.addWidget(self.lineEdit_8, 3, 1, 1, 1)

        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 3, 2, 1, 1)

        self.lineEdit_6 = QLineEdit(self.frame_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 4, 4, 1, 1)

        self.lineEdit_10 = QLineEdit(self.frame_4)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout.addWidget(self.lineEdit_10, 5, 1, 1, 1)

        self.lineEdit_11 = QLineEdit(self.frame_4)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout.addWidget(self.lineEdit_11, 5, 2, 1, 3)

        self.lineEdit_3 = QLineEdit(self.frame_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 1, 2, 1, 3)

        self.lineEdit_7 = QLineEdit(self.frame_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout.addWidget(self.lineEdit_7, 2, 1, 1, 4)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 4)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.pushButton_9 = QPushButton(self.tab_2)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_8.addWidget(self.pushButton_9, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_6.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pgCadastrar)
        self.pgHome = QWidget()
        self.pgHome.setObjectName(u"pgHome")
        self.label_4 = QLabel(self.pgHome)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(230, 110, 211, 201))
        self.Pages.addWidget(self.pgHome)

        self.verticalLayout_5.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.frmMain)

        self.frmFooter = QFrame(self.mainContainer)
        self.frmFooter.setObjectName(u"frmFooter")
        self.frmFooter.setFrameShape(QFrame.Shape.StyledPanel)
        self.frmFooter.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frmFooter)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 100, 49, 16))

        self.verticalLayout.addWidget(self.frmFooter)


        self.horizontalLayout.addWidget(self.mainContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SysDev", None))
        self.btn_Home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_Cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_Contato.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btn_Sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"987654321", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/email.png\"/></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Jeffrey.Epstein@gmail.com", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Youtube", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/whatsApp.png\"/></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/Youtube.png\"/></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"sobre", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Este sistema faz consulta do CNPJ utilizando API da Receita Federal e faz o cadastro em um banco de dados. O objetivo deste sistema \u00e9 ensinar como utilizar Python e o QT para desenvolver aplica\u00e7\u00f5es modernas e funcionais.", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:700;\">Empresas</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Munic\u00edpio", None))
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.lineEdit_9.setText(QCoreApplication.translate("MainWindow", u"Munic\u00edpio", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.lineEdit_10.setText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.lineEdit_11.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"Nome Empresarial", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Empresa</p></body></html>", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/logo_sysdev_240px.png\"/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SysDev", None))
    # retranslateUi

