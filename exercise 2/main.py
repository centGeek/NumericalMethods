#by Wojciech Błyskal 247632, Łukasz Centkowski 247638, zespół 2
import numpy as np
import matplotlib.pyplot as plt
import os
from dzialania_na_macierzach import Dzialania_na_macierzach as dnm

dimension_string = input("Podaj wymiar macierzy:")
dimension = int(dimension_string)

def extract_numbers_from_file(file_path):
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
print("Numbers extracted from the file:", numbers)

matrix = np.array
"""
for i in range(dimension):
    row = []
    for j in range(2 * dimension + 1):
        if j < dimension:
            row.append(numbers[i * (dimension + 1) + j])#tworzy czesc macierzy ze zmiennymi
        elif j < 2 * dimension:#tworzy czesc macierzy jako macierz jednostkowa
            if j == dimension + i:
                row.append(1)
            else:
                row.append(0)
        else:#tworzy ostatnia kolumne macierzy
            row.append(numbers[i * (dimension + 1) + dimension])
    matrix.append(row) # matrix przechowuje macierz wszystkich elementow"""

matrix = np.zeros((dimension, 2 * dimension + 1))

for i in range(dimension):
    for j in range(2 * dimension + 1):
        if j < dimension:
            matrix[i, j] = numbers[i * (dimension + 1) + j]
        elif j < 2 * dimension:
            if j == dimension + i:
                matrix[i, j] = 1
        else:
            matrix[i, j] = numbers[i * (dimension + 1) + dimension]

#for row in matrix:
 #   print(row)
"""
for column_index, elements in enumerate(zip(*matrix)):
    for row_index, element in enumerate(elements):
        if (row_index != column_index and element != 0):
            
        elif (row_index == column_index and element != 1):"""

matrix_tran = matrix.T

for column_index, column in matrix_tran:
    if column_index < dimension:
        for row_index, element in column:
            if column_index != row_index and element != 0:
                for column_index_2, column2 in matrix_tran:
                    for row_index_2, element in column2:
                        if column_index == column_index_2 and row_index != row_index_2 and element != 0:

            elif column_index == row_index and element != 1:
                