# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import urllib.request
import api
from hakkimizda import Ui_hakkimizda
from bs4 import BeautifulSoup

#Veritabanı Bağlantısı
vt = sqlite3.connect("aseo.sqlite")
ex = vt.cursor()
tablo_yap = """CREATE TABLE IF NOT EXISTS veri
(giris, kullanici, sifre)"""
ex.execute(tablo_yap)
vt.commit()
vt.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(974, 686)
        MainWindow.setMinimumSize(QtCore.QSize(974, 686))
        MainWindow.setMaximumSize(QtCore.QSize(974, 686))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("KernelBlog.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.url_g = QtWidgets.QLineEdit(self.centralwidget)
        self.url_g.setGeometry(QtCore.QRect(430, 80, 351, 31))
        self.url_g.setText("")
        self.url_g.setObjectName("url_g")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 80, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 10, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.giris_b = QtWidgets.QPushButton(self.centralwidget)
        self.giris_b.setGeometry(QtCore.QRect(520, 251, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.giris_b.setFont(font)
        self.giris_b.setObjectName("giris_b")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 161, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.user_g = QtWidgets.QLineEdit(self.centralwidget)
        self.user_g.setGeometry(QtCore.QRect(410, 161, 141, 31))
        self.user_g.setText("")
        self.user_g.setObjectName("user_g")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 201, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pass_g = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_g.setGeometry(QtCore.QRect(410, 201, 141, 31))
        self.pass_g.setText("")
        self.pass_g.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_g.setObjectName("pass_g")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 321, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.ilk10 = QtWidgets.QTextEdit(self.centralwidget)
        self.ilk10.setGeometry(QtCore.QRect(50, 361, 271, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ilk10.setFont(font)
        self.ilk10.setReadOnly(True)
        self.ilk10.setObjectName("ilk10")
        self.tumkelime = QtWidgets.QTextEdit(self.centralwidget)
        self.tumkelime.setGeometry(QtCore.QRect(350, 361, 271, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tumkelime.setFont(font)
        self.tumkelime.setReadOnly(True)
        self.tumkelime.setObjectName("tumkelime")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 321, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.baslik_a = QtWidgets.QTextEdit(self.centralwidget)
        self.baslik_a.setGeometry(QtCore.QRect(650, 361, 271, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.baslik_a.setFont(font)
        self.baslik_a.setReadOnly(True)
        self.baslik_a.setObjectName("baslik_a")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(750, 321, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.kayitli = QtWidgets.QComboBox(self.centralwidget)
        self.kayitli.setGeometry(QtCore.QRect(580, 201, 161, 31))
        self.kayitli.setObjectName("kayitli")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(610, 171, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(340, 250, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.url_g_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.url_g_2.setGeometry(QtCore.QRect(380, 120, 351, 31))
        self.url_g_2.setText("")
        self.url_g_2.setObjectName("url_g_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(220, 120, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 974, 21))
        self.menubar.setObjectName("menubar")
        self.menuMen = QtWidgets.QMenu(self.menubar)
        self.menuMen.setObjectName("menuMen")
        self.menuYard_m = QtWidgets.QMenu(self.menubar)
        self.menuYard_m.setObjectName("menuYard_m")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHakk_m_zda = QtWidgets.QAction(MainWindow)
        self.actionHakk_m_zda.setObjectName("actionHakk_m_zda")
        self.cikis = QtWidgets.QAction(MainWindow)
        self.cikis.setObjectName("cikis")
        self.guncelleme = QtWidgets.QAction(MainWindow)
        self.guncelleme.setObjectName("guncelleme")
        self.menuMen.addAction(self.cikis)
        self.menuYard_m.addAction(self.actionHakk_m_zda)
        self.menuYard_m.addAction(self.guncelleme)
        self.menubar.addAction(self.menuMen.menuAction())
        self.menubar.addAction(self.menuYard_m.menuAction())
        self.veriguncel()


        self.retranslateUi(MainWindow)
        self.actionHakk_m_zda.triggered.connect(self.hakkimizda)
        self.cikis.triggered.connect(self.kapat)
        self.guncelleme.triggered.connect(self.guncellik)
        self.giris_b.clicked.connect(self.islem)
        self.kayitli.currentIndexChanged.connect(self.girisbilgi)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KernelBlog Seo Aracı"))
        self.label.setText(_translate("MainWindow", "* Yazının Önizleme URL\'ini Giriniz:"))
        self.label_2.setText(_translate("MainWindow", "KernelBlog Seo Aracına Hoşgeldiniz"))
        self.giris_b.setText(_translate("MainWindow", "Başlat"))
        self.label_3.setText(_translate("MainWindow", "* Bot Kullanıcı Adı:"))
        self.label_4.setText(_translate("MainWindow", "* Bot Parolası :"))
        self.label_5.setText(_translate("MainWindow", "En Çok Kullanılan İlk 10 Kelime"))
        self.ilk10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.ilk10.setPlaceholderText(_translate("MainWindow", "Veriler Bekleniyor"))
        self.tumkelime.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.tumkelime.setPlaceholderText(_translate("MainWindow", "Veriler Bekleniyor"))
        self.label_6.setText(_translate("MainWindow", "Tüm Kelimeler"))
        self.baslik_a.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.baslik_a.setPlaceholderText(_translate("MainWindow", "Veriler Bekleniyor"))
        self.label_7.setText(_translate("MainWindow", "Başlıklar"))
        self.label_8.setText(_translate("MainWindow", "Kayıtlı Hesaplar"))
        self.checkBox.setText(_translate("MainWindow", "Giriş Bilgilerini Kaydet"))
        self.label_9.setText(_translate("MainWindow", "* Giriş URL\'ini Giriniz:"))
        self.menuMen.setTitle(_translate("MainWindow", "Menü"))
        self.menuYard_m.setTitle(_translate("MainWindow", "Yardım"))
        self.actionHakk_m_zda.setText(_translate("MainWindow", "Hakkımızda"))
        self.cikis.setText(_translate("MainWindow", "Çıkış"))
        self.guncelleme.setText(_translate("MainWindow", "Güncellemeri Denetle"))

    def uyari(self, yazi):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(yazi)
        msgBox.setWindowTitle("Uyarı")
        msgBox.setStandardButtons(QMessageBox.Ok)
        returnValue = msgBox.exec()

    def temizlik(self):
        self.ilk10.clear()
        self.tumkelime.clear()
        self.baslik_a.clear()

    def islem(self):
        self.temizlik()
        if self.url_g.text() == "" or self.user_g.text() == "" or self.pass_g.text() == "" or self.url_g_2.text() == "":
            self.uyari("Kutular Boş Bırakılamaz!!!")
        else:
            api2 = api.api()
            veri = api2.ayar(self.url_g_2.text(), self.url_g.text(), self.user_g.text(), self.pass_g.text())
            if veri == "404":
                self.uyari("Kullanıcı Adı Veya Şifre Hatalı!")
            else:
                if self.checkBox.isChecked():
                    vt = sqlite3.connect("aseo.sqlite")
                    ex = vt.cursor()
                    bilgiler = (self.url_g_2.text(), self.user_g.text())
                    komut = """SELECT * FROM veri WHERE giris = (?) and kullanici = (?)"""
                    ex.execute(komut, bilgiler)
                    sifre = ex.fetchone()
                    if sifre == None:
                        bilgiler = (self.url_g_2.text(), self.user_g.text(), self.pass_g.text())
                        kaydet = """INSERT INTO veri VALUES (?,?,?)"""
                        ex.execute(kaydet, bilgiler)
                    else:
                        pass
                    vt.commit()
                    vt.close()
                else:
                    pass
                self.statusbar.showMessage("Veriler Alınıyor...",3000)
                self.url_g_2.setText("")
                self.user_g.setText("")
                self.pass_g.setText("")
                kelimeler = api2.paragraf(veri)
                h1, h2, h3, h4 = api2.basliklar(veri)
                self.ilk10fonk(kelimeler)
                self.tumfonk(kelimeler)
                self.baslikfonk(h1, h2, h3, h4)
                self.veriguncel()

    def ilk10fonk(self, liste):
        for i in range(-10,0):
            self.ilk10.append(liste[i][0]+" >>> "+str(liste[i][1]))

    def tumfonk(self, liste):
        for i in liste:
            self.tumkelime.append(i[0]+" >>> "+str(i[1]))

    def baslikfonk(self, h1, h2, h3, h4):
        self.baslik_a.append("h1 Başlıklar")
        for i in h1:
            self.baslik_a.append("\""+i+"\"")
        self.baslik_a.append("\nh2 Başlıklar")
        for i in h2:
            self.baslik_a.append("\""+i+"\"")
        self.baslik_a.append("\nh3 Başlıklar")
        for i in h3:
            self.baslik_a.append("\""+i+"\"")
        self.baslik_a.append("\nh4 Başlıklar")
        for i in h4:
            self.baslik_a.append("\""+i+"\"")

    def hakkimizda(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_hakkimizda()
        self.ui.setupUi(self.window)
        self.window.show()

    def girisbilgi(self):
        if self.kayitli.currentText() == "":
            self.url_g_2.setText("")
            self.user_g.setText("")
            self.pass_g.setText("")
        else:
            kullanici = ""
            site = ""
            durum = 0
            for i in self.kayitli.currentText():
                if i == ":":
                    durum = 1
                if durum == 0:
                    kullanici = kullanici + i
                else:
                    site = site + i
            site = site[1:]
            self.url_g_2.setText(site)
            self.user_g.setText(kullanici)
            bilgiler = (site, kullanici)
            vt = sqlite3.connect("aseo.sqlite")
            ex = vt.cursor()
            komut = """SELECT * FROM veri WHERE giris = (?) and kullanici = (?)"""
            ex.execute(komut, bilgiler)
            self.sifre = ex.fetchone()
            self.pass_g.setText(self.sifre[2])
            vt.commit()
            vt.close()

    def veriguncel(self):
        self.kayitli.clear()
        self.kayitli.addItem("")
        vt = sqlite3.connect("aseo.sqlite")
        ex = vt.cursor()
        al = """SELECT * FROM veri"""
        ex.execute(al)
        for i in ex:
            self.kayitli.addItem(i[1]+":"+i[0])
        vt.commit()
        vt.close()

    def kapat(self):
        QtWidgets.QApplication.quit()

    def guncellik(self):
        url = "https://felis.kernelblog.org/aseo-tarih.txt"
        try:
        	url_oku = urllib.request.urlopen(url)
        except urllib.error.URLError as e:
        	self.uyari("Lütfen İnternet Bağlantınızı Kontrol Ediniz!")
        	sys.exit(0)
        soup = BeautifulSoup(url_oku, 'html.parser')
        if str(soup) == "02/04/2020":
        	self.uyari("A+SEO Güncel.")
        else:
            app.exit(app.exec())
            os.system("python3 /usr/share/aseo/guncelleme.py")
            sys.exit(0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
