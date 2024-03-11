#by Wojciech Błyskal 247632, Łukasz Centkowski 247638, zespół 2, wariant 01B
import numpy as np
import matplotlib.pyplot as plt
from colorama import Fore
from funkcje_matematyczne import Funkcje_Matematyczne
import przyklady_funkcji as pf 
import funkcje_zlozone as fz
fm = Funkcje_Matematyczne()
miejsce_zerowe = ""
wybrana_funkcja_string = input("Podaj nr funkcji ktora chcesz wybrac: \n'1' oznacza sinusoidalną \n'2' oznacza wielomianową \n'3' oznacza wykładniczą\n'4' oznacza złożoną\n")
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
     wybor = input("Wybierz odpowiednią kombinację funkcji, które należy złączyć \n1.Wielomianowa i Wykladnicza, \n2.Trygonometryczna i Wykladnicza \n3.Trygonometryczna i Wielomianowa\n4.Wszystkie podane powyzej\n")
     if(wybor=='1'):
            wybrana_funkcja = fz.wykladnicza_i_wielomian
            wybrana_funkcja_poch = fz.pochodna_wykladnicza_i_wielomian
     if(wybor=='2'):
            wybrana_funkcja =  fz.trygonometryczna_i_wykladnicza
            wybrana_funkcja_poch = fz.poch_trygonometryczna_i_wykladnicza
     if(wybor=='3'):
            wybrana_funkcja =  fz.trygonometryczna_i_wielomian
            wybrana_funkcja_poch = fz.poch_trygonometryczna_i_wielomian
     if(wybor=='4'):
            wybrana_funkcja =  fz.wszystkie
            wybrana_funkcja_poch = fz.poch_wszystkie

lewy_koniec_przedzialu_string = input("Podaj najmniejsza wartosc x, ktora bierzemy pod uwage(lewy kraniec przedzialu):")
lewy_koniec_przedzialu = []
lewy_koniec_przedzialu.append(fm.konwersja_string_na_double(lewy_koniec_przedzialu_string))

prawy_koniec_przedzialu_string = input("Podaj najwieksza wartosc x, ktora bierzemy pod uwage(prawy kraniec przedzialu):")
prawy_koniec_przedzialu = []
prawy_koniec_przedzialu.append(fm.konwersja_string_na_double(prawy_koniec_przedzialu_string))

if lewy_koniec_przedzialu[-1] >= prawy_koniec_przedzialu[-1]:
    print(Fore.RED+"Niewlasciwy przedzial, lewy koniec przedzialu musi byc mniejszy od prawego.")
elif wybrana_funkcja(lewy_koniec_przedzialu[-1]) * wybrana_funkcja(prawy_koniec_przedzialu[-1]) > 0:
    print(Fore.RED+"Niewlasciwy przedzial, dla funkcji ciaglej, nie bedzie mial zadnego miejsca zerowego")
else:
    miejsce_zerowe = (prawy_koniec_przedzialu[-1] + lewy_koniec_przedzialu[-1]) / 2
    epsilon_czy_ilosc_iteracji = input("Jesli chcesz, by algorytm zakonczyl sie po znalezieniu miejsca zerowego z dokladnoscia do wybranej wartosci epsilon, napisz '1', jesli chcesz, by algorytm zakonczyl sie po wybranej liczbie iteracji, napisz cokolwiek innego:")
    if epsilon_czy_ilosc_iteracji == '1':
        epsilon_string = input("Podaj dokladnosc, z jaka ma byc wykonany algorytm:")
        epsilon = fm.konwersja_string_na_double(epsilon_string)
        wybor_metody = input ("Jesli chcesz, by zastosowano metode bisekcji, napisz '1', jesli chcesz, by algorytm zastosowal metode stycznych, napisz cokolwiek innego:")
        if wybor_metody == '1':
            while abs(wybrana_funkcja(miejsce_zerowe)) >= epsilon:
                miejsce_zerowe = fm.bisekcja(wybrana_funkcja, lewy_koniec_przedzialu, prawy_koniec_przedzialu) #indeks -1 w python oznacza ostatni element tablicy
            print("Miejscem zerowym funkcji jest:" + str(miejsce_zerowe))
        else:
            x_poczatkowe = input("Podaj poczatkowa wartosc x:")
            miejsce_zerowe_s = [fm.konwersja_string_na_double(x_poczatkowe)]
            while abs(wybrana_funkcja(miejsce_zerowe_s[-1])) >= epsilon:
                if wybrana_funkcja_poch(miejsce_zerowe_s[-1] == 0):
                    print("Przerwano wykonywanie algorytmu, poniewaz pochodna funkcji wynosi 0.")
                    epsilon = float('inf')
                else:
                    miejsce_zerowe_s.append(fm.styczne(wybrana_funkcja, wybrana_funkcja_poch, miejsce_zerowe_s[-1]))
                    print("Miejscem zerowym funkcji jest:" + str(miejsce_zerowe_s[-1]))
    else:
        ilosc_iteracji_string = input("Podaj ilosc iteracji, po ktorych ma sie zakonczyc algorytm:")
        ilosc_iteracji = fm.konwersja_string_na_integer(ilosc_iteracji_string)
        iterator = 0
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
                if wybrana_funkcja_poch(miejsce_zerowe_s[-1] == 0):
                    print("Przerwano wykonywanie algorytmu, poniewaz pochodna funkcji wynosi 0.")
                    iterator = ilosc_iteracji
                else:
                    miejsce_zerowe_s.append(fm.styczne(wybrana_funkcja, wybrana_funkcja_poch, miejsce_zerowe_s[-1]))
                    iterator += 1
                    print("Miejscem zerowym funkcji jest:" + str(miejsce_zerowe_s[-1]))
przedzialy_funkcji = np.linspace(int(lewy_koniec_przedzialu_string), int(prawy_koniec_przedzialu_string), 1000)
funkcja_do_wykresu = wybrana_funkcja(przedzialy_funkcji)
indeks_miejsca_zerowego = np.abs(przedzialy_funkcji - miejsce_zerowe).argmin()
y_punkt = funkcja_do_wykresu[indeks_miejsca_zerowego]
plt.plot(przedzialy_funkcji, funkcja_do_wykresu)
plt.title('Wykres funkcji')
is_local = "miejsce_zerowe_s" in locals()
if is_local:
     zmienna = miejsce_zerowe_s[-1]
     indeks_miejsca_zerowego_s = np.abs(przedzialy_funkcji - miejsce_zerowe_s[-1]).argmin()     
     y_punkt_s = funkcja_do_wykresu[indeks_miejsca_zerowego_s]
     plt.scatter(zmienna, y_punkt_s, color='red', label=f'Punkt ({zmienna}, {y_punkt})', zorder=5)
     
else:
     plt.scatter(miejsce_zerowe, y_punkt, color='red', label=f'Punkt ({miejsce_zerowe}, {y_punkt})', zorder=5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
