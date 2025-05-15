from PyQt5.QtWidgets import *
from giris import Ui_MainWindow
from ANASAYFA import ANAMENUPAGE
from REGISTER import REGISTERPAGE
from veritabani import DATABASEPAGE




class LOGINPAGE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.giris = Ui_MainWindow()
        self.giris.setupUi(self)
        self.anamenuac = ANAMENUPAGE()
        self.kayitolac = REGISTERPAGE()
        self.veriTabaniAc = DATABASEPAGE()
        self.giris.pushButtonGiris.clicked.connect(self.GirisYap)
        self.giris.pushButtonKayitOl.clicked.connect(self.KayitOlAc)
        

    def KayitOlAc(self):    #kayit sayfasi acar
        self.kayitolac.show()

        
    def GirisYap(self):  # Giriş yapar
        KullaniciAdi = self.giris.lineEditGirisKullaniciAdi.text()
        sifre = self.giris.lineEditGirisSifre.text()
        dogrulama = self.veriTabaniAc.KayitCek()

        if KullaniciAdi == "" or sifre == "":
            QMessageBox.warning(self, "Uyari", "Giris Bilgileri Bos Birakilamaz!!!")
        else:
            basarili_giris = False
            for deger in dogrulama:
                if deger[4] == KullaniciAdi and deger[5] == sifre:
                    basarili_giris = True
                    break

        if basarili_giris:
            self.anamenuac.show()
            self.hide()
        else:
            QMessageBox.warning(self, "BILGI", "Giris basarisiz")



app = QApplication([])
sayfa = LOGINPAGE()
sayfa.show()
app.exec()