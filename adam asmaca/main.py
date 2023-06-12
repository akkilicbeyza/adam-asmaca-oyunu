import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

class AdamAsmacaOyunu(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.setWindowTitle("adam asmaca oyunu")
        self.setGeometry(600, 100, 800, 800)
        self.setWindowFlags(Qt.FramelessWindowHint)   # pencerenin çerçevesiz olmasını sağlar

        self.kelime_listesi = [
            ("python", "Dil"),
            ("programlama", "Yazılım"),
            ("oyun", "Eğlence"),
            ("masaüstü", "Mobilya"),
            ("adam", "İnsan"),
            ("asmaca", "Oyun"),
        ]
        self.kelime, self.ipucu = random.choice(self.kelime_listesi)
        self.tahmin = ["_"] * len(self.kelime)
        self.hak_sayisi = 12

        self.label_tahmin = QLabel(" ".join(self.tahmin), self)
        self.label_tahmin.move(20, 20)
        self.label_tahmin.setFont(QFont("Times New Roman", 18))
        self.label_tahmin.setGeometry(20, 150, 1000, 40)

        self.label_hak = QLabel("Kalan Hak: {}".format(self.hak_sayisi), self)
        self.label_hak.move(20, 50)
        self.label_hak.setFont(QFont("Times New Roman", 14))
        self.label_hak.setGeometry(200, 100, 500, 40)
        self.label_hak.setStyleSheet("color: #ff9999")
        font = QFont("Times New Roman", 18)
        font.setBold(True)
        font.setItalic(True)
        self.label_hak.setFont(font)

        self.label_ipucu = QLabel("İpucu: {}".format(self.ipucu), self)
        self.label_ipucu.move(20, 80)
        self.label_ipucu.setFont(QFont("Times New Roman", 14, italic=True))
        self.label_ipucu.setGeometry(20, 280, 500, 40)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 180)
        self.textbox.setFont(QFont("Times New Roman", 14))
        self.textbox.setGeometry(20, 350, 150, 40)

        self.button_tahmin_et = QPushButton("Tahmin Et", self)
        self.button_tahmin_et.move(20, 240)
        font = QFont("Times New Roman", 14)
        font.setBold(True)
        font.setItalic(True)
        self.button_tahmin_et.setFont(font)
        self.button_tahmin_et.setGeometry(20, 500, 150, 40)
        self.button_tahmin_et.clicked.connect(self.tahmin_et)
        self.button_tahmin_et.setStyleSheet("background-color: #cc99ff; color: #FFFFFF;")


        self.adam_label = QLabel(self)
        self.adam_label.setScaledContents(True)  # resimleri tam boyutta göstermek için
        self.adam_label.setGeometry(400, 200, 250, 500)  # resim boyutlarını ayarladım
        self.adam_asma_guncelle()  # 1. resmi başlangıçta göstermek için

        self.button_yeniden_basla = QPushButton("Yeniden Başla", self)
        self.button_yeniden_basla.move(20, 360)
        font = QFont("Times New Roman", 14)
        font.setBold(True)
        font.setItalic(True)
        self.button_yeniden_basla.setFont(font)
        self.button_yeniden_basla.setGeometry(620, 50, 150, 40) 
        self.button_yeniden_basla.clicked.connect(self.yeniden_basla)
        self.button_yeniden_basla.setEnabled(True)  # başlangıçtan itibaren aktif
        self.button_yeniden_basla.setStyleSheet("background-color: #6699ff; color: #FFFFFF;")

        self.button_cikis = QPushButton("Çıkış", self)
        self.button_cikis.move(20, 480)
        font = QFont("Times New Roman", 14)
        font.setBold(True)
        font.setItalic(True)
        self.button_cikis.setFont(font)
        self.button_cikis.setGeometry(700, 740, 80, 40) 
        self.button_cikis.clicked.connect(self.cikis)
        self.button_cikis.setStyleSheet("background-color: #ff0000; color: #FFFFFF;")

    def tahmin_et(self):
        tahmin_harf = self.textbox.text().lower()
        self.textbox.clear()

        if tahmin_harf in self.kelime:
            for i in range(len(self.kelime)):
                if self.kelime[i] == tahmin_harf:
                    self.tahmin[i] = tahmin_harf
            self.label_tahmin.setText(" ".join(self.tahmin))
        else:
            self.hak_sayisi -= 1
            self.label_hak.setText("Kalan Hak: {}".format(self.hak_sayisi))
            self.adam_asma_guncelle()

        if "_" not in self.tahmin:
            self.label_hak.setText("Tebrikler! Kelimeyi buldunuz.")
            self.button_tahmin_et.setEnabled(False)
            self.button_yeniden_basla.setEnabled(True)
            self.label_tahmin.setText("Doğru kelime: " + self.kelime)  # doğru kelimeyi göster
        elif self.hak_sayisi == 0:
            self.label_tahmin.setText("Hakkınız kalmadı. Doğru kelime: " + self.kelime)
            self.button_tahmin_et.setEnabled(False)
            self.button_yeniden_basla.setEnabled(True)

    def adam_asma_guncelle(self):
        asma_resimler = [
            "1.png",
            "2.png",
            "3.png",
            "4.png",
            "5.png",
            "6.png",
            "7.png",
            "8.png",
            "9.png",
            "10.png",
            "11.png",
            "12.png",
        ]
        kalan_hak = self.hak_sayisi
        resim_index = 12 - kalan_hak
        if resim_index < len(asma_resimler):
            resim_adi = asma_resimler[resim_index]
            resim_yolu = "./" + resim_adi
            self.adam_label.setPixmap(QPixmap(resim_yolu).scaledToHeight(500))

    def yeniden_basla(self):
        self.kelime_listesi.remove((self.kelime, self.ipucu))  # mevcut kelime ve ipucunu listeden çıkar
        if len(self.kelime_listesi) == 0:  # kelime listesi boşsa, oyunu yeniden başlat
            self.kelime_listesi = [
                ("python", "Dil"),
                ("programlama", "Yazılım"),
                ("oyun", "Eğlence"),
                ("masaüstü", "Mobilya"),
                ("adam", "İnsan"),
                ("asmaca", "Oyun"),
            ]
        self.kelime, self.ipucu = random.choice(self.kelime_listesi)  # yeni bir kelime ve ipucu seç
        self.tahmin = ["_"] * len(self.kelime)  # yeni kelime için tahmin listesini yeniden oluştur
        self.hak_sayisi = 12  # hakkı yeniden başlat

        self.label_tahmin.setText(" ".join(self.tahmin))
        self.label_hak.setText("Kalan Hak: {}".format(self.hak_sayisi))
        self.label_ipucu.setText("İpucu: {}".format(self.ipucu))
        self.button_tahmin_et.setEnabled(True)
        self.button_yeniden_basla.setEnabled(False)
        self.adam_asma_guncelle()
    
    def cikis(self):
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    oyun = AdamAsmacaOyunu()
    oyun.show()
    sys.exit(app.exec_())
