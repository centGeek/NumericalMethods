#by Wojciech Błyskal 247632, Łukasz Centkowski 247638, zespół 2
import numpy as np
from colorama import init

class Dzialania_na_macierzach:
    def __init__(self):
        init()

    def switch_rows(self, matrix, row1, row2): #odpowiada za zamiane wierszy w macierzy
        matrix2 = [row[:] for row in matrix]
        for j in range(len(matrix[0])):
            matrix[row1][j], matrix[row2][j] = matrix2[row2][j], matrix2[row1][j]

    def isCalculable(self, row, result, e):
        for i in row:
            if round(i, e) != 0:
                return 0 #zwraca 0, jesli uklad wedlug tego wiersza jest oznaczony
        if round(result, e) != 0:
            return 1 #zwraca 1 dla ukladu sprzecznego
        return 2 #zwraca 2 dla ukladu nieoznaczonego
    
    def Jordan(self, matrix, result, dimension, e):
        lista_buforowa = [0] * dimension
        for k in range(dimension): #k oznacza indeks kolumny
            for row in matrix:  #fragment sprawdzajacy czy na tym etapie mozna uklad uznac za sprzeczny lub nieoznaczony
                if self.isCalculable(row, result[k], e) == 1:
                    print("Układ sprzeczny")
                    return None
                elif self.isCalculable(row, result[k], e) == 2:
                    print("Układ nieoznaczony")
                    return None
            max = abs(matrix[k][k]) #ustawiamy wiersze, by tworzyly macierz przekatniowo dominujaca(nie gwarantuje to idealnego rezultatu, ale bedzie zblizony)
            index = k #szukamy najwiekszego elementu kolumny. Na poczatku zakladamy pierwszy, a potem zmieniamy go, jesli znajdziemy wiekszy
            for i in range(dimension - k): #i oznacza indeks wiersza. dimension - k jest oznaczeniem ilosci wierszy sprawdzanych
                if abs(matrix[k + i][k]) > max: # iterujemy od k-tego wiersza do ostatniego. nie bierzemy pod uwage wczesniejszych wierszy, gdyz byloby to kontrproduktywne ze wzcesniejszymi iteracjami
                    max = abs(matrix[k + i][k])
                    index = k + i
            if index != k:
                self.switch_rows(matrix, k, index) #jesli pierwszy element nie byl najwiekszy dokonujemy zamiany wierszy
                aux = result[index] #pamietajmy, ze przy zamianie wierszy nalezy tez zamienic elementy w tablicy wynikowej
                result[index] = result[k]
                result[k] = aux
            akk = matrix[k][k] #akk-element podstawowy
            result[k] /= akk
            for j in range(dimension - k):
                matrix[k][k + j] /= akk
            for i in range(dimension):
                if i != k:
                    aik = matrix[i][k]
                    result[i] -= result[k] * aik
                    for j in range(dimension):
                         matrix[i][j] -= matrix[k][j] * aik     
        result = [x for x in result]
        return result
            