import sys

from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QMessageBox)
from PySide6.QtGui import QIcon

from display import Display, Info, ButtonsGrid
from variables import WINDOW_ICON_PATH
from styles import setupTheme

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando o layout básico
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # Título da janela
        self.setWindowTitle('Calculadora')

    def adjustFixedSize(self):
        # Última coisa a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget):
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Definindo o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    app.setWindowIcon(icon)
    window.setWindowIcon(icon)

    # Info
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()