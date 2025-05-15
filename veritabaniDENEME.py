import sqlite3
import os

class kayit():
    def _init_(self):
        dizin_yol = os.path.dirname(os.path.abspath(__file__))
        self.db_yol = os.path.join(dizin_yol,'veritabani.db')
        

    def ac(self):
        self.con = sqlite3.connect(self.db_yol)
        self.cursor = self.con.cursor()

    def kapat(self):
        self.con.close()
    
    def KullaniciEkle(self,ad,soyad,telefon,kullaniciadi,sifre,sifretekrar,email):
        try:
            self.ac()
            sql = "INSERT INTO kayit (Ad, Soyad, Telefon, E-Mail, Sifre) VALUES (?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(sql,(ad,soyad,telefon,kullaniciadi,sifre,sifretekrar,email))
            self.con.commit()
            return True
        except:
            return False
        finally:
            self.kapat()
            
    def KullaniciGetir(self):
     try:
         self.ac()
         sql = "SELECT * FROM kayit ORDER BY id"
         self.cursor.execute(sql)
         veri= self.cursor.fetchall()
         return veri
     except:
         return False
     finally:
         self.kapat()