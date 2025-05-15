from PyQt5.QtWidgets import *
from sikayet import Ui_MainWindow
from veritabani import DATABASEPAGE
import sys


class COMPLAINTPAGE(QMainWindow):  #SIKAYETTT
    def __init__(self):
        super().__init__()
        self.sikayet = Ui_MainWindow()
        self.sikayet.setupUi(self)
        self.sikayet.pushButton.clicked.connect(self.Geridon)
        self.db = DATABASEPAGE()
        self.SikayetListele()#
        self.sikayet.pushButtonYenile.clicked.connect(self.SikayetListele)
    
    def SikayetListele(self):
        
        self.sikayet.tableWidget.setColumnWidth(0,25)
        self.sikayet.tableWidget.setColumnWidth(1,75)
        self.sikayet.tableWidget.setColumnWidth(2,435)

        veriler = self.db.SikayetCek()
        numOfLines = 0
        headers = ['ID','PLAKA','ŞİKAYET']
        #self.sikayet.tableWidget.setHorizontalHeader(headers)#

        if veriler != False:
            self.sikayet.tableWidget.clearContents()
            self.sikayet.tableWidget.setRowCount(len(veriler))
            for veri in veriler:
                self.sikayet.tableWidget.setItem(int(numOfLines), 0, QTableWidgetItem(str(veri[0])))
                self.sikayet.tableWidget.setItem(int(numOfLines), 1, QTableWidgetItem(str(veri[1])))
                self.sikayet.tableWidget.setItem(int(numOfLines), 2, QTableWidgetItem(str(veri[2])))

                numOfLines+=1
        else:
            return False



    def Geridon(self):
        self.hide()


        #SIKAYETI YAPARKEN ONCESINDE ESKI DB YI SIL SONRA YENISINI KOY