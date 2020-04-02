#-*- coding: UTF-8 -*-

class kodek(object):
    def ayar(self):
        self.cozucu = [8217,8211,8220,8221,8230,775]
        self.donusum = ["'","-","\"","\"","...",""]

    def isleme(self, veri):
        self.ayar()
        sonveri = ""
        for i in veri:
            try:
                sonveri = sonveri + self.donusum[self.cozucu.index(ord(i))]
            except ValueError:
                sonveri = sonveri + i
        return(sonveri)
