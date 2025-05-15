import sqlite3
import os


class DATABASEPAGE():
    def __init__(self):
        dizin_yol = os.path.dirname(os.path.abspath(__file__)) #dizini buldu
        self.db_yol = os.path.join(dizin_yol, 'veritabani.db')#dizin ile veritabani ismi birlestirme
    
    
    def dbac(self):
        self.con = sqlite3.connect(self.db_yol)
        self.cursor = self.con.cursor()


    def dbkapat(self):
        self.con.close()
   

    def KayitEkle(self,ad ,soyad ,telefon ,kullaniciAdi ,sifre ,sifreTekrar ,EMail):
        try:
            self.dbac()
            sql = "insert into KAYITEKRANI('ad' ,'soyad' ,'telefon' ,'kullaniciAdi' ,'sifre' ,'sifreTekrar' ,'EMail') values(?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(sql,(ad ,soyad ,telefon ,kullaniciAdi ,sifre ,sifreTekrar ,EMail))
            self.con.commit()
            return True
        except:
            return False
        finally:
            self.dbkapat()


    def KayitCek(self):
        try:
            self.dbac()
            sql = "SELECT * FROM KAYITEKRANI ORDER BY kullaniciAdi"  # SQL DEN ARAMA KOMUTU
            self.cursor.execute(sql)
            veriler = self.cursor.fetchall()
            print(veriler)
            return veriler
        except Exception as e:
            print(f"Hata: {e}")  # Hata mesajını yazdır
            return False
        finally:
            self.dbkapat()

    
    def Listele(self, filtredegeri):
        try:
            filtredegeri
            self.dbac()
            sql = "SELECT * FROM SERVIS  WHERE filtredegeri LIKE? OR tarih LIKE? or plaka LIKE?"
            self.cursor.execute(sql,('%' + filtredegeri + '%', '%'+ filtredegeri + '%','%'+ filtredegeri + '%') )#yapar
            veriler =self.cursor.fetchall()
            print('kontrol')
            return veriler
        except:
            return False
        finally:
            self.dbkapat()
    

    def ServisCek(self):
        try:
            self.dbac()
            sql = "SELECT * FROM SERVIS ORDER BY id DESC"
            self.cursor.execute(sql)
            veriler = self.cursor.fetchall()
            return veriler
        except Exception as e:
            print(f"ServisCek Hatasi: {e}")
            return False
        finally:
            self.dbkapat()


    def ServisEkle(self, aracModel, MotorHacmi, aracinYili, kilometre, yapilanIslem, yapilisTarihi, saat, plaka):
        try:
            self.dbac()
            sql = "INSERT INTO SERVIS (aracModel, MotorHacmi, aracinYili, kilometre, yapilanIslem, yapilisTarihi, saat, plaka) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(sql, (aracModel, MotorHacmi, aracinYili, kilometre, yapilanIslem, yapilisTarihi, saat, plaka))
            self.con.commit()
            return True
        except Exception as e:
            print(f"ServisEkle Hatası: {e}")
            return False
        finally:
            self.dbkapat()


    def SikayetEkle(self, plaka, sikayet):
        try:
            self.dbac()
            sql = "insert into SIKAYET('plaka','sikayet') values(?, ?)"
            self.cursor.execute(sql,(plaka,sikayet))
            self.con.commit()
            return True
        except Exception as e:
            print(f"SikayetEkle Hatasi: {e}")
            return False
        finally:
            self.dbkapat()


    def SikayetCek(self):
        try:
            self.dbac()
            sql = "SELECT * FROM SIKAYET ORDER BY plaka"
            self.cursor.execute(sql)
            veriler = self.cursor.fetchall()
            return veriler
        except Exception as e:
            print(f"SikayetCek Hatasi: {e}")
            return False
        finally:
            self.dbkapat()


    def Editor(self,aracModel, MotorHacmi, aracinYili, kilometre, yapilanIslem, yapilisTarihi, saat, plaka):
        try:
            self.dbac()
            veriler = (aracModel, MotorHacmi, aracinYili, kilometre, yapilanIslem, yapilisTarihi, saat, plaka)
            sql = "UPDATE SERVIS SET aracModel=? , MotorHacmi=? , aracinYili=? , kilometre=?, yapilanIslem=?, yapilisTarihi=?, saat=? WHERE plaka=?"
            self.cursor.execute(sql,(veriler))
            self.con.commit()
            


            return True
        except Exception as e:
            print(f"Hata: {e}")
            return False
        finally:
            self.dbkapat()


    def get_by_plaka(self, plaka):
        try:
            self.dbac()
            sql = "SELECT * FROM SERVIS WHERE plaka=?"
            self.cursor.execute(sql, (plaka,))
            veri = self.cursor.fetchone()
            return veri
        except Exception as e:
            print(f"Veritabanı hatası: {e}")
            return None
        finally:
            self.dbkapat()


    def ServisSil(self, id):
        try:
            self.dbac()
            sql = "DELETE FROM SERVIS WHERE id=?"
            
            self.cursor.execute(sql, (id,))
            self.con.commit()
            return True
        except Exception as e:
            print("Hata:", e)
            return False
        finally:
            self.dbkapat()
    def SikayetSil(self,id):
        try:
            self.dbac()
            sql = "DELETE FROM SIKAYET WHERE id=?"
            self.cursor.execute(sql,(id,))
            self.con.commit()
            return True
        except: 
            return False
        finally:
            self.dbkapat()
        
            

        














