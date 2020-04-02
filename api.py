#-*- coding: UTF-8 -*-

import kodek
import requests
import bs4 as bs
import operator

class api(object):
    def ayar(self, giris_url, url, user, passwd):
        with requests.session() as c:
            giris_verileri = {"log": user,"pwd": passwd}

            giris_sayfasi = c.post(giris_url, data=giris_verileri)
            sayfa = c.get(url)

            self.veri = bs.BeautifulSoup(sayfa.content, "lxml")
            self.soru = self.veri.find("title")
            if self.soru.text.find("Sayfa bulunamadı") == -1 and self.soru.text.find("Page not found") == -1:
                self.veri2 = self.veri.find("article")
                return(self.veri2)
            else:
                return("404")

    def basliklar(self, veri):
        k = kodek.kodek()
        baslikliste = ["h1","h2","h3","h4"]
        h1 = []
        h2 = []
        h3 = []
        h4 = []
        baslik = veri.find("h1", {"class": "entry-title"})
        h1.append(k.isleme(baslik.text))
        for i in baslikliste:
            baslik = veri.find_all(i)
            for j in baslik:
                if i == "h2":
                    h2.append(k.isleme(j.text))
                elif i == "h3":
                    h3.append(k.isleme(j.text))
                elif i == "h4":
                    h4.append(k.isleme(j.text))
        return(h1,h2,h3,h4)


    def paragraf(self, veri):
        #Değişkenler Ve Veri
        k = kodek.kodek()
        hamveri = []
        kelime = ""
        kelimeliste = []
        hatasizliste = []
        kontrolliste = []
        islenmis = {}
        ekliste = ["bir","ve","veya","yada","bu","gibi","yani","ne","o","da","ile","şey","ait","için","şimdi","de","ancak","artık","hemen","var","yok","ise","hangi"]
        paragraflar = veri.find_all("p")
        diger = veri.find_all("li")

        #Paragrafların taglerden Ayıklanarak Bir Listeye Atılması
        for i in paragraflar:
            hamveri.append(i.text)
        for i in diger:
            hamveri.append(i.text)

        #Paragrafların İçerisindeki Tüm Kelimelerin Ayıklanıp Farklı Bir Listeye Taşınması
        for i in hamveri:
            for b in i:
                if b == chr(32) or b == "." or b == "\n":
                    kelimeliste.append(kelime.lower())
                    kelime = ""
                else:
                    kelime = kelime + b

        #Ascii Kodu 8xxx Olan Karakterlerin Kodek'e Gönderilip Son Listeye Kelimelerin Düzgün Hallerinin Atılması
        for i in kelimeliste:
            try:
                ekliste.index(i)
            except ValueError:
                hatasizliste.append(k.isleme(i))

        while True:
            try:
                hatasizliste.remove("")
            except ValueError:
                break

        for i in hatasizliste:
            try:
                kontrolliste.index(i)
            except ValueError:
                kontrolliste.append(i)

        for i in kontrolliste:
            islenmis[i] = hatasizliste.count(i)

        islenmis1 = sorted(islenmis.items(), key=operator.itemgetter(1))
        return(islenmis1)
