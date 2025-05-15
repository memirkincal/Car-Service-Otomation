from PyQt5.QtWidgets import *
from kayitol import Ui_MainWindow
from veritabani import DATABASEPAGE


class REGISTERPAGE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.kayitol = Ui_MainWindow()
        self.kayitol.setupUi(self)
        self.kayitol.pushButtonKayitKayit.clicked.connect(self.Kaydet)
        self.veritabani = DATABASEPAGE()

    def Geridon(self):
        self.hide()

    def Kaydet(self):
        ad = self.kayitol.lineEditKayitAd.text()
        soyad = self.kayitol.lineEditKayitSoyad.text()
        telefon = self.kayitol.lineEditKayitTelefon.text()
        kullaniciAdi = self.kayitol.lineEditKayitKullaniciAdi.text()
        sifre = self.kayitol.lineEditKayitSifre.text()
        sifreTekrar = self.kayitol.lineEditKayitSifre2.text()
        EMail = self.kayitol.lineEditKayiteEMail.text()

        if ad == "" or soyad == "" or telefon == "" or kullaniciAdi == "" or sifre == "" or sifreTekrar == "" or EMail == "":
            QMessageBox.warning(self, "Uyari!", "Kayit alanlari bos olamaz!!")
            return

        if sifre != sifreTekrar:
            QMessageBox.warning(self, "Uyari!", "Sifre ile Sifre tekrar ayni olmali!!!")
            return

        degerler = self.veritabani.KayitCek()
        if degerler is False:
            QMessageBox.warning(self, "Hata!", "Veritabanından veriler çekilemedi!")
            return

        for deger in degerler:
            veriKullaniciAdi = deger[4]
            veriEMail = deger[6]
            veriTelefon = deger[3]
            if kullaniciAdi == veriKullaniciAdi:
                QMessageBox.warning(self, "Hata", "Bu Kullanici adi alinmistir")
                return
            elif EMail == veriEMail:
                QMessageBox.warning(self, "Hata", "Bu E-posta alinmistir")
                return
            elif telefon == veriTelefon:
                QMessageBox.warning(self, "Hata", "Bu Telefon alinmistir")
                return

        kayitEkleme = self.veritabani.KayitEkle(ad, soyad, telefon, kullaniciAdi, sifre, sifreTekrar, EMail)
        if kayitEkleme:
            QMessageBox.information(self, "Bilgilendirme", "Kayit basariyla olustu")
            self.Geridon()
        else:
            QMessageBox.warning(self, "Uyari!", "Kayit olusturulamadi")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    register_page = REGISTERPAGE()
    register_page.show()
    sys.exit(app.exec_())
