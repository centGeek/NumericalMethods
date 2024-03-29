#by Wojciech Błyskal 247632, Łukasz Centkowski 247638, zespół 2, wariant 01B
import numpy as np
import matplotlib.pyplot as plt
from colorama import init, Fore
from funkcje_matematyczne import Funkcje_Matematyczne
import przyklady_funkcji as pf 
import funkcje_zlozone as fz
init(autoreset=True)
fm = Funkcje_Matematyczne()
wybrana_funkcja_string = input("Podaj nr funkcji ktora chcesz wybrac: \n'1' oznacza sinusoidalną \n'2' oznacza wielomianową \n'3' oznacza wykładniczą\n'4' oznacza wielomianowa podana przez uzytkownika\n'5' oznacza złożoną\n")
if wybrana_funkcja_string == '1':
    wybrana_funkcja = pf.sinus
    wybrana_funkcja_poch = pf.poch_sinus
if wybrana_funkcja_string == '2':
    wybrana_funkcja = pf.wielomian
    wybrana_funkcja_poch = pf.poch_wielomian
if wybrana_funkcja_string == '3':
    wybrana_funkcja = pf.wykladnicza
    wybrana_funkcja_poch = pf.pochodna_wykladniczej
if wybrana_funkcja_string == '4':
    stopien_string = input("Podaj stopien wielomianu ktory chcesz zbadac:")
    stopien = int(stopien_string) #fm.konwersja_string_na_integer(stopien_string)
    wspolczynniki = []
    wspolczynniki = fm.podajwielomian(stopien)
    wybrana_funkcja = fm.funkcja_horner(wspolczynniki)
    wybrana_funkcja_poch = fm.funkcja_horner(fm.horner_poch(wspolczynniki))
if wybrana_funkcja_string == '5':
     wybor = input("Wybierz odpowiednią kombinację funkcji, które należy złączyć \n1.Wielomianowa i Wykladnicza, \n2.Trygonometryczna i Wykladnicza \n3.Trygonometryczna i Wielomianowa\n4.Wszystkie podane powyzej\n")
     if(wybor=='1'):
            wybrana_funkcja = fz.wykladnicza_i_wielomian
            wybrana_funkcja_poch = fz.wykladnicza_i_wielomian_poch
     if(wybor=='2'):
            wybrana_funkcja =  fz.trygonometryczna_i_wykladnicza
            wybrana_funkcja_poch = fz.trygonometryczna_i_wykladnicza_poch
     if(wybor=='3'):
            wybrana_funkcja =  fz.trygonometryczna_i_wielomian
            wybrana_funkcja_poch = fz.trygonometryczna_i_wielomian_poch
     if(wybor=='4'):
            wybrana_funkcja =  fz.wszystkie
            wybrana_funkcja_poch = fz.wszystkie_poch

lewy_koniec_przedzialu_string = input("Podaj najmniejsza wartosc x, ktora bierzemy pod uwage(lewy kraniec przedzialu):")
lewy_koniec_przedzialu = []
lewy_koniec_przedzialu.append(fm.konwersja_string_na_double(lewy_koniec_przedzialu_string))

prawy_koniec_przedzialu_string = input("Podaj najwieksza wartosc x, ktora bierzemy pod uwage(prawy kraniec przedzialu):")
prawy_koniec_przedzialu = []
prawy_koniec_przedzialu.append(fm.konwersja_string_na_double(prawy_koniec_przedzialu_string))

if lewy_koniec_przedzialu[-1] >= prawy_koniec_przedzialu[-1]:
    print(Fore.RED+"Niewlasciwy przedzial, lewy koniec przedzialu musi byc mniejszy od prawego.")
elif wybrana_funkcja(lewy_koniec_przedzialu[0]) * wybrana_funkcja(prawy_koniec_przedzialu[0]) > 0:
    print(Fore.RED+"Niewlasciwy przedzial, dla funkcji ciaglej bedzie mial wiele miejsc zerowych lub nie bedzie mial zadnego miejsca zerowego.")
else:
    miejsce_zerowe = (prawy_koniec_przedzialu[-1] + lewy_koniec_przedzialu[-1]) / 2
    iterator = 0
    epsilon_czy_ilosc_iteracji = input("Jesli chcesz, by algorytm zakonczyl sie po znalezieniu miejsca zerowego z dokladnoscia do wybranej wartosci epsilon, napisz '1', jesli chcesz, by algorytm zakonczyl sie po wybranej liczbie iteracji, napisz cokolwiek innego:")
    if epsilon_czy_ilosc_iteracji == '1':
        epsilon_string = input("Podaj dokladnosc, z jaka ma byc wykonany algorytm:")
        epsilon = fm.konwersja_string_na_double(epsilon_string)
        wybor_metody = input ("Jesli chcesz, by zastosowano metode bisekcji, napisz '1', jesli chcesz, by algorytm zastosowal metode stycznych, napisz cokolwiek innego:")
        if wybor_metody == '1':
            while abs(wybrana_funkcja(miejsce_zerowe)) >= epsilon:
                iterator += 1
                miejsce_zerowe = fm.bisekcja(wybrana_funkcja, lewy_koniec_przedzialu, prawy_koniec_przedzialu)
            print("Miejscem zerowym funkcji jest:" + str(miejsce_zerowe) + ". Liczba wykonanych iteracji: " + str(iterator))
        else:
            x_poczatkowe = input("Podaj poczatkowa wartosc x:")
            miejsce_zerowe_s = [fm.konwersja_string_na_double(x_poczatkowe)]
            while abs(wybrana_funkcja(miejsce_zerowe_s[-1])) >= epsilon:
                iterator += 1
                if wybrana_funkcja_poch(miejsce_zerowe_s[-1]) == 0:
                    print("Przerwano wykonywanie algorytmu, poniewaz pochodna funkcji wynosi 0. Liczba wykonanych iteracji:" + str(iterator))
                    epsilon = float('inf')
                else:
                    miejsce_zerowe_s.append(fm.styczne(wybrana_funkcja, wybrana_funkcja_poch, miejsce_zerowe_s[-1]))
            print("Miejscem zerowym funkcji jest:" + str(miejsce_zerowe_s[-1]) + ". Liczba wykonanych iteracji: " + str(iterator))
            miejsce_zerowe = miejsce_zerowe_s[-1]
    else:
        ilosc_iteracji_string = input("Podaj ilosc iteracji, po ktorych ma sie zakonczyc algorytm:")
        ilosc_iteracji = fm.konwersja_string_na_integer(ilosc_iteracji_string)
        wybor_metody = input ("Jesli chcesz, by zastosowano metode bisekcji, napisz '1', jesli chcesz, by algorytm zastosowal metode stycznych, napisz cokolwiek innego:")
        if wybor_metody == '1':
            while ilosc_iteracji > iterator:
                miejsce_zerowe = fm.bisekcja(wybrana_funkcja, lewy_koniec_przedzialu, prawy_koniec_przedzialu) #indeks -1 w python oznacza ostatni element tablicy
                iterator += 1
            print("Miejscem zerowym funkcji jest:" + str(miejsce_zerowe))
        else:
            x_poczatkowe = input("Podaj poczatkowa wartosc x:")
            miejsce_zerowe_s = [fm.konwersja_string_na_double(x_poczatkowe)]
            while ilosc_iteracji > iterator:
                if wybrana_funkcja_poch(miejsce_zerowe_s[-1]) == 0:
                    print("Przerwano wykonywanie algorytmu, poniewaz pochodna funkcji wynosi 0. Liczba wykonanych iteracji:" + str(iterator))
                    iterator = ilosc_iteracji
                else:
                    miejsce_zerowe_s.append(fm.styczne(wybrana_funkcja, wybrana_funkcja_poch, miejsce_zerowe_s[-1]))
                    iterator += 1
            print("Miejscem zerowym funkcji jest:" + str(miejsce_zerowe_s[-1]))
            miejsce_zerowe = miejsce_zerowe_s[-1]
przedzialy_funkcji = np.linspace(fm.konwersja_string_na_double(lewy_koniec_przedzialu_string), fm.konwersja_string_na_double(prawy_koniec_przedzialu_string), 1000)
funkcja_do_wykresu = wybrana_funkcja(przedzialy_funkcji)
indeks_miejsca_zerowego = np.abs(przedzialy_funkcji - miejsce_zerowe).argmin()
y_punkt = funkcja_do_wykresu[indeks_miejsca_zerowego]
plt.plot(przedzialy_funkcji, funkcja_do_wykresu)
plt.title('Wykres funkcji')
plt.scatter(miejsce_zerowe, y_punkt, color='red', label=f'Punkt ({miejsce_zerowe}, {y_punkt})', zorder=5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
