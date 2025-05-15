from PyQt5.QtWidgets import *
from hakkimizda import Ui_MainWindow


class ABOUTUSPAGE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.hakkimizda = Ui_MainWindow()
        self.hakkimizda.setupUi(self)
        self.hakkimizda.pushButtonHakkimizdaGeriDon.clicked.connect(self.GeriDon)

        
    def GeriDon(self):
        self.hide()
        
        