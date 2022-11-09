class Pojazd:
    nazwa = "nazwa"
    rodzaj = "rodzaj"
    kolor = "kolor"
    wartosc = 100.00
    def opis(self):
        tekst_opis = "%s to %s %s warty %.2f zl." % (self.nazwa, self.kolor, self.rodzaj, self.wartosc)
        return tekst_opis
    
Auto1 = Pojazd()
Auto1.nazwa = "Ferrari"
Auto1.rodzaj = "kabriolet"
Auto1.kolor = "czerwony"
Auto1.wartosc = 60000

Auto2 = Pojazd()
Auto2.nazwa = "Ikarus"
Auto2.rodzaj = "autobus"
Auto2.kolor = "niebieski"
Auto2.wartosc = 10000
# sprawdzenie kodu
print (Auto1.opis())
print (Auto2.opis())
