from PyQt5.QtWidgets import *
from ekle import Ui_MainWindow
from veritabani import DATABASEPAGE
import sys


class ADDPAGE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ekle = Ui_MainWindow()
        self.ekle.setupUi(self)
        self.ekle.pushButtonGeriDon.clicked.connect(self.Geridon)
        self.ekle.pushButtonEkle.clicked.connect(self.ServisEkle)
        self.ekle.pushButtonEkle.clicked.connect(self.SikayetEkle)
        self.db = DATABASEPAGE()

    def Geridon(self):
        self.hide()

    def SikayetEkle(self):
        sikayet = self.ekle.textEditSikayet.toPlainText()
        plaka = self.ekle.lineEditPlaka.text()
        normal=True
        if sikayet == "":
            QMessageBox.information(self, "BILGI","SIKAYET BELIRTILMEDI")
        
        if normal:
            sikayetAdd = self.db.SikayetEkle(plaka,sikayet)
            if sikayetAdd:
                QMessageBox.information(self, "BILGI", "SIKAYET BASARIYLA OLUSTURULDU")
            else:
                QMessageBox.information(self, "HATA", "SIKAYET OLUSTURULAMADI")


            

    def ServisEkle(self):
        aracModel = self.ekle.lineEditAracModeli.text()
        MotorHacmi = self.ekle.comboBoxMotorHacmi.currentText()
        aracinYili = self.ekle.lineEditAracYili.text()
        kilometre = self.ekle.lineEditKM.text()
        yapilanIslem = self.ekle.lineEditYapilanIslem.text()
        yapilisTarihi = self.ekle.dateEditTarih.date().toString("yyyy-MM-dd")
        saat = self.ekle.timeEditSaat.time().toString("HH:mm")
        plaka = self.ekle.lineEditPlaka.text()
        

        normal = True
        if aracModel == "" or MotorHacmi == "" or aracinYili == "" or kilometre == "" or yapilanIslem == "" or yapilisTarihi == "" or saat == "" or plaka == "":
            QMessageBox.warning(self, "BILGI", "KAYIT BILGILERI BOS KALAMAZ")
            normal = False

        if normal:
            servisAdd = self.db.ServisEkle(aracModel, MotorHacmi, aracinYili, kilometre, yapilanIslem, yapilisTarihi, saat, plaka)
            if servisAdd:
                QMessageBox.information(self, "BILGI", "KAYIT BASARIYLA OLUSTURULDU")
            else:
                QMessageBox.warning(self, "HATA", "KAYIT OLUSTURULAMADI")





