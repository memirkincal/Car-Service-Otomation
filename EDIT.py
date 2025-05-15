from PyQt5.QtWidgets import *
from duzenleme import Ui_MainWindow
from veritabani import DATABASEPAGE
from PyQt5.QtCore import *


class EDITPAGE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.duzenle = Ui_MainWindow()
        self.duzenle.setupUi(self)
        self.db = DATABASEPAGE()
        self.duzenle.pushButtonGeriDon.clicked.connect(self.GeriDon)
        self.duzenle.pushButtonAra.clicked.connect(self.Ara)
        self.duzenle.pushButtonDuzenle.clicked.connect(self.Kaydet)
        self.duzenle.pushButtonDuzenle.clicked.connect(self.SikayetEkle)
        self.duzenle.pushButtonSil.clicked.connect(self.Sil)

    def Ara(self):
        plaka = self.duzenle.lineEditPlakaAra.text()
        if plaka == "":
            QMessageBox.warning(self, "Uyarı", "Plaka alanı boş bırakılamaz!")
            return
        
        try:
            veri = self.db.get_by_plaka(plaka)
            if veri:
                print(f"Veri: {veri}")
                self.duzenle.labelID.setText(str(veri[0]))  # ID'yi stringe dönüştürerek setText ile kullanma
                self.duzenle.lineEditAracModeli.setText(str(veri[1]))  # Arac Modeli
                self.duzenle.comboBoxMotorHacmi.setCurrentText(str(veri[2]))  # Motor Hacmi
                self.duzenle.lineEditAracYili.setText(str(veri[3]))  # Arac Yılı
                self.duzenle.lineEditKM.setText(str(veri[4]))  # Kilometre
                self.duzenle.lineEditYapilanIslem.setText(str(veri[5]))  # Yapılan İşlem

                date = QDate.fromString(veri[6], "yyyy-MM-dd")
                if date.isValid():
                    self.duzenle.dateEditTarih.setDate(date)
                else:
                    print("Geçersiz tarih formatı:", veri[6])

                time = QTime.fromString(veri[7], "HH:mm")
                if time.isValid():
                    self.duzenle.timeEditSaat.setTime(time)
                else:
                    print("Geçersiz saat formatı:", veri[7])

                self.duzenle.lineEditPlaka.setText(str(veri[8]))  # Plaka
            else:
                QMessageBox.warning(self, "Uyarı", "Bu plakaya ait araç bulunamadı!")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Bir hata oluştu: {e}")


    def Kaydet(self):
        try:
            id = self.duzenle.labelID.text()
            aracModel = self.duzenle.lineEditAracModeli.text()
            MotorHacmi = self.duzenle.comboBoxMotorHacmi.currentText()
            aracinYili = self.duzenle.lineEditAracYili.text()
            kilometre = self.duzenle.lineEditKM.text()
            yapilanIslem = self.duzenle.lineEditYapilanIslem.text()
            yapilisTarihi = self.duzenle.dateEditTarih.date().toString("yyyy-MM-dd")
            saat = self.duzenle.timeEditSaat.time().toString("HH:mm")
            plaka = self.duzenle.lineEditPlaka.text()
            

            if aracModel == "" or MotorHacmi == "" or aracinYili == "" or kilometre == "" or yapilanIslem == "" or yapilisTarihi == "" or saat == "" or plaka == "":
                QMessageBox.warning(self, "Uyarı", "Tüm alanlar doldurulmalıdır!")
                return
            
            guncelle = self.db.Editor(aracModel, MotorHacmi, aracinYili, kilometre, yapilanIslem, yapilisTarihi, saat, plaka)
            if guncelle:
                
                QMessageBox.information(self, "Bilgi", "Veri başarıyla güncellendi.")
            else:
                QMessageBox.critical(self, "Hata", "Veri güncellenirken bir hata oluştu.")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Bir hata oluştu: {e}")
    

    def SikayetEkle(self):
        plaka = self.duzenle.lineEditPlaka.text()
        sikayet = self.duzenle.textEditSikayet.toPlainText()
        guncelleSikayet = self.db.SikayetEkle(plaka,sikayet)
        if guncelleSikayet:
            QMessageBox.information(self, "Bilgi", "Şikayet Eklendi")

        
        
    def Sil(self):
        id = self.duzenle.labelID.text()
        sil = self.db.ServisSil(id)
        sikayetSil = self.db.SikayetSil(id)
        if sil:
            QMessageBox.information(self,"BILGI","ARAC SILINDI")
        else:
            QMessageBox.warning(self,"HATA","ARAC SILINEMEDI")
        if sikayetSil:
            QMessageBox.information(self,"BILGI","ARACIN SIKAYETI SILINDI")
            self.hide()
        else:
            QMessageBox.warning(self,"HATA","ARACIN SIKAYETI SILINEMEDI")

            


    def GeriDon(self):
        self.hide()


        

 