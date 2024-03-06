from colorama import init, Fore
class Funkcje_Matematyczne:
    def __init__(self):
        init()

    def konwersja_string_na_integer(self, napis):
        try:
            return int(napis)
        except ValueError:
            raise ValueError(Fore.RED+f"Nie można skonwertować {napis} na liczbę")

    def konwersja_string_na_double(self, napis): 
        try:
            return float(napis)
        except ValueError:
            raise ValueError(Fore.RED+f"Nie można skonwertować {napis} na zmienną typu float")

    def bisekcja(self, funkcja, a, b):
        srodek = (b[-1] + a[-1]) / 2
        wartosc_na_srodku = funkcja(srodek)
        if funkcja(a[-1]) * wartosc_na_srodku < 0:
            b.append(srodek) #w pythonie wszystkie zmienne sa referencjami, zatem zmiany dokonane na zmiennych przekazanych do funkcji, zmieniaja je rowniez poza funkcja 
        else:
            a.append(srodek)
        return srodek

    def styczne(self, funkcja, funkcja_pochodna, xi):
        return xi - funkcja(xi) / funkcja_pochodna(xi)



