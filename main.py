from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow)
from ui_main import Ui_MainWindow
import sys
from uiFuncProd import consulta_cnpj
from database import Database

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("SysDev - Sistema de cadastro de empresas")
        
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)

        self.btn_Home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pgHome))
        self.btn_Cadastrar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pgCadastrar))
        self.btn_Contato.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pgContatos))
        self.btn_Sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pgSobre))

        self.btAlternar.clicked.connect(self.alternar_menu)

    def alternar_menu(self):
        width = self.leftContainer.width()
        if width == 9:
            newWidth = 200
        else:
            newWidth = 9

        self.animation = QtCore.QPropertyAnimation(self.leftContainer, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def consultApi(self):
        campos = consulta_cnpj(self.txt_cnpj.text())

        self.txt_nomeEmpresarial.setText(campos[0])
        self.txt_logradouro.setText(campos[1])
        self.txt_numero.setText(campos[2])
        self.txt_complemento.setText(campos[3])
        self.txt_bairro.setText(campos[4])
        self.txt_municipio.setText(campos[5])
        self.txt_uf.setText(campos[6])
        self.txt_cep.setText(campos[7].replace('.', '').replace('-', ''))
        self.txt_telefone.setText(campos[8].replace('(', '').replace('-', '').replace(')', ''))
        self.txt_email.setText(campos[9])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()