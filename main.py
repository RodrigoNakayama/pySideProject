from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
import sys

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

    def leftContainer(self):
        width = self.left_container.width()
        if width == 9:
            newWidth = 200
        else:
            newWidth = 9

        self.animation = Qtcore.QProperyAnimation(self.left_container, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animationsetEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

