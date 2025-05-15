from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QTableWidgetItem, QTableWidget
from anamenu import Ui_Dialog
from EDIT import EDITPAGE
from ABOUTUS import ABOUTUSPAGE
from SSS import SSSPAGE
from veritabani import DATABASEPAGE
from COMPLAINT import COMPLAINTPAGE
from ADD import ADDPAGE






class ANAMENUPAGE(QDialog):
    def __init__(self):
        super().__init__()
        self.anasayfa = Ui_Dialog()
        self.anasayfa.setupUi(self)  
        #--------------------------------------
        self.duzenleme = EDITPAGE()
        self.hakkimizda = ABOUTUSPAGE()
        self.sss = SSSPAGE()
        self.db = DATABASEPAGE()
        self.complaint = COMPLAINTPAGE()
        self.add = ADDPAGE()
        self.ServisListele()
        self.anasayfa.pushButtonDuzenle.clicked.connect(self.DuzenleAc)
        self.anasayfa.commandLinkButtonHakkimizda.clicked.connect(self.HakkimizdaAc)
        self.anasayfa.commandLinkButtonSSS.clicked.connect(self.SSSAc)
        self.anasayfa.pushButtonYenile.clicked.connect(self.ServisListele)
        self.anasayfa.tableWidgetListe.clicked.connect(self.SikayetAc)
        self.anasayfa.pushButtonEkle.clicked.connect(self.EkleAc)
    



    

    def ListeyiGuncelle(self, veriler):
        self.anasayfa.tableWidgetListe.clearContents()
        self.anasayfa.tableWidgetListe.setRowCount(len(veriler))
        self.anasayfa.tableWidgetListe.setColumnCount(10)
        ilankolonlar = ["ID", "Araç Modeli", "Motor Hacmi", "Araç Yılı", "Kilometre", "Yapılan İşlem", "Yapılış Tarihi", "Saat", "Plaka", "ŞİKAYETİ"]
        self.anasayfa.tableWidgetListe.setHorizontalHeaderLabels(ilankolonlar)

        

        

    def ServisListele(self):
        self.anasayfa.tableWidgetListe.setColumnWidth(0,25)
        self.anasayfa.tableWidgetListe.setColumnWidth(1,160)
        self.anasayfa.tableWidgetListe.setColumnWidth(2,60)
        self.anasayfa.tableWidgetListe.setColumnWidth(3,60)
        self.anasayfa.tableWidgetListe.setColumnWidth(4,75)
        self.anasayfa.tableWidgetListe.setColumnWidth(5,270)
        self.anasayfa.tableWidgetListe.setColumnWidth(6,80)
        self.anasayfa.tableWidgetListe.setColumnWidth(7,50)
        self.anasayfa.tableWidgetListe.setColumnWidth(8,105)
        self.anasayfa.tableWidgetListe.setColumnWidth(9,90)
        
               
        veriler = self.db.ServisCek()
        numberOfLines = 0
        headers = ["ID", "Araç Modeli", "Motor Hacmi", "Araç Yılı", "Kilometre", "Yapılan İşlem", "Yapılış Tarihi", "Saat", "Plaka","ŞİKAYETİ",] #BASLIKLAR
        self.anasayfa.tableWidgetListe.setHorizontalHeaderLabels(headers)                                                          #BASLIKLARI YAZAN KOMUT

        if veriler!=False:
            self.anasayfa.tableWidgetListe.setRowCount(len(veriler))
            for veri in veriler:
                self.anasayfa.tableWidgetListe.setItem(int(numberOfLines), 0, QTableWidgetItem(str(veri[0])))
                self.anasayfa.tableWidgetListe.setItem(int(numberOfLines), 1, QTableWidgetItem(str(veri[1])))
                self.anasayfa.tableWidgetListe.setItem(int(numberOfLines), 2, QTableWidgetItem(str(veri[2])))
                self.anasayfa.tableWidgetListe.setItem(int(numberOfLines), 3, QTableWidgetItem(str(veri[3])))
                self.anasayfa.tableWidgetListe.setItem(int(numberOfLines), 4, QTableWidgetItem(str(veri[4])))
                self.anasayfa.tableWidgetListe.setItem(int(numberOfLines), 5, QTableWidgetItem(str(veri[5])))
                self.anasayfa.tableWidgetListe.setItem(int(numberOfLines), 6, QTableWidgetItem(str(veri[6])))
                self.anasayfa.tableWidgetListe.setItem(int(numberOfLines), 7, QTableWidgetItem(str(veri[7])))
                self.anasayfa.tableWidgetListe.setItem(int(numberOfLines), 8, QTableWidgetItem(str(veri[8])))
                self.anasayfa.tableWidgetListe.setItem(int(numberOfLines), 9, QTableWidgetItem("ŞİKAYET"))
                
                
                numberOfLines += 1



    def SSSAc(self):
        self.sss.show()
 

    def HakkimizdaAc(self):  
        self.hakkimizda.show()
    
    def SikayetAc(self):
        selectLine = self.anasayfa.tableWidgetListe.currentRow()
        clikedColumn = self.anasayfa.tableWidgetListe.currentColumn()
        if clikedColumn == 9:
            selectedID = self.anasayfa.tableWidgetListe.item(selectLine,0).text()
            self.complaint.show()
    def DuzenleAc(self):
        self.duzenleme.show()
        
        
        
        
    

    def EkleAc(self):
        self.add.show()






        




