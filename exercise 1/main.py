#by Wojciech Błyskal 247632, Łukasz Centkowski 247638, zespół 2, wariant 01B
import math

def konwersja_string_na_integer(napis):
    return int(napis)

def konwersja_string_na_double(napis): 
    return float(napis)

def bisekcja(funkcja, a, b):
    srodek = (b[-1] + a[-1]) / 2
    wartosc_na_srodku = funkcja(srodek)
    if funkcja(a[-1]) * wartosc_na_srodku < 0:
        b.append(srodek) #w pythonie wszystkie zmienne sa referencjami, zatem zmiany dokonane na zmiennych przekazanych do funkcji, zmieniaja je rowniez poza funkcja 
    else:
        a.append(srodek)
    return srodek

def sinus(x):
    return math.cos(x)

wybrana_funkcja_string = input("Podaj nr funkcji ktora chcesz wybrac: '1'.")
if wybrana_funkcja_string == '1':
    wybrana_funkcja = sinus;

lewy_koniec_przedzialu_string = input("Podaj najmniejsza wartosc x, ktora bierzemy pod uwage(lewy kraniec przedzialu:)")
lewy_koniec_przedzialu = []
lewy_koniec_przedzialu.append(konwersja_string_na_double(lewy_koniec_przedzialu_string))

prawy_koniec_przedzialu_string = input("Podaj najwieksza wartosc x, ktora bierzemy pod uwage(prawy kraniec przedzialu:)")
prawy_koniec_przedzialu = []
prawy_koniec_przedzialu.append(konwersja_string_na_double(prawy_koniec_przedzialu_string))

if lewy_koniec_przedzialu[0] >= prawy_koniec_przedzialu[0]:
    print("Niewlasciwy przedzial, lewy koniec przedzialu musi byc mniejszy od prawego.")
elif wybrana_funkcja(lewy_koniec_przedzialu[0]) * wybrana_funkcja(prawy_koniec_przedzialu[0]) > 0:
    print("Niewlasciwy przedzial, dla funkcji ciaglej bedzie mial wiele miejsc zerowych lub nie bedzie mial zadnego miejsca zerowego.")
else:
    miejsce_zerowe = (prawy_koniec_przedzialu[-1] + lewy_koniec_przedzialu[-1]) / 2
    epsilon_czy_ilosc_iteracji = input("Jesli chcesz, by algorytm zakonczyl sie po znalezieniu miejsca zerowego z dokladnoscia do wybranej wartosci epsilon, napisz '1', jesli chcesz, by algorytm zakonczyl sie po wybranej liczbie iteracji, napisz cokolwiek innego:")
    if epsilon_czy_ilosc_iteracji == '1':
        epsilon_string = input("Podaj dokladnosc, z jaka ma byc wykonany algorytm:")
        epsilon = konwersja_string_na_double(epsilon_string)
        while abs(wybrana_funkcja(miejsce_zerowe)) >= epsilon:
            miejsce_zerowe = bisekcja(wybrana_funkcja, lewy_koniec_przedzialu, prawy_koniec_przedzialu) #indeks -1 w python oznacza ostatni element tablicy
        print("Miejscem zerowym funkcji jest:" + str(miejsce_zerowe))
    else:
        ilosc_iteracji_string = input("Podaj ilosc iteracji, po ktorych ma sie zakonczyc algorytm:")
        ilosc_iteracji = konwersja_string_na_integer(ilosc_iteracji_string)
        iterator = 0
        while ilosc_iteracji > iterator:
            miejsce_zerowe = bisekcja(wybrana_funkcja, lewy_koniec_przedzialu, prawy_koniec_przedzialu)
            iterator = iterator + 1
        print("Miejscem zerowym funkcji jest:" + str(miejsce_zerowe))
