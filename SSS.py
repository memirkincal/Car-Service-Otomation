from PyQt5.QtWidgets import *
from sikcasorulansorular import Ui_MainWindow


class SSSPAGE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.SSS = Ui_MainWindow()
        self.SSS.setupUi(self)
        self.SSS.pushButtonSSSGeriDon.clicked.connect(self.GeriDon)

        
    def GeriDon(self):
        self.hide()