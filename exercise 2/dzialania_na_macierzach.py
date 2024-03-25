#by Wojciech Błyskal 247632, Łukasz Centkowski 247638, zespół 2
import numpy as np
from colorama import init

class Dzialania_na_macierzach:
    def __init__(self):
        init()

    """def switch_rows(matrix, row1, row2):
        matrix2 = [row[:] for row in matrix]
        for j in range(len(matrix[0])):
            matrix[row1][j], matrix[row2][j] = matrix2[row2][j], matrix2[row1][j]"""

    def subtraction(matrix, base_row_index, subtracted_row_index, amount): #base_row to wiersz z odjemnnymi, subtracted_row z odjemnikami
        base_row = []
        subtracted_row = []
        for row_index, row in enumerate(matrix): #wydobywamy wlasciwe wiersze
            if row_index == subtracted_row_index:
                for column in range(len(row)):
                    subtracted_row.append(row[column])
            elif row_index == base_row_index:
                for column in range(len(row)):
                    base_row.append(row[column])
        
        for i in range(len(subtracted_row)): #mnozymy odjemniki przez wielokrotnosc wiersza ktora chcemy odjac
            subtracted_row[i] = subtracted_row[i] * amount
        
        for i in range(len(base_row)): #odejmujemy wiersze od siebie
            base_row[i] = base_row[i] - subtracted_row[i]

        for row_index, row in enumerate(matrix): #kopiujemy wiersz po odejmowaniu do macierzy
            if row_index == base_row_index:
                for column in range(len(row)):
                    row[column] = base_row[column]