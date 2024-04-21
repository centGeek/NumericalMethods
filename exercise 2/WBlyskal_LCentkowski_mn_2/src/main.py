#by Wojciech Błyskal 247632, Łukasz Centkowski 247638, zespół 2
import numpy as np
import matplotlib.pyplot as plt
import os
from dzialania_na_macierzach import Dzialania_na_macierzach as dnm

e = 8
dimension_string = input("Podaj wymiar macierzy:")
dimension = int(dimension_string)

def extract_numbers_from_file(file_path): #wczytywanie danych z pliku
    numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            elements = line.split()
            for element in elements:
                try:
                    number = float(element)
                    numbers.append(number)
                except ValueError:
                    pass
    return numbers

script_directory = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_directory, 'macierz.txt')

numbers = extract_numbers_from_file(file_path)

matrix = np.array
matrix = np.zeros((dimension, dimension))
result = np.zeros(dimension)

for i in range(dimension):
    for j in range(dimension + 1):
        if j < dimension:
            matrix[i, j] = numbers[i * (dimension + 1) + j]
        else:
            result[i] = numbers[i * (dimension + 1) + dimension]

for row in matrix:
    print(row)

for i in result:
    print(i)

a = dnm()
b = a.Jordan(matrix, result, dimension, e)
if b != None:
    print("Kolejne wartosci zmiennych to:", b)
                