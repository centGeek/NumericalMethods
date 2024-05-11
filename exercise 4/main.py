import numpy as np
import os
from functions import Functions as fun

polynolmal_list = []

accuracy = input("Podaj dokładność do obliczania: ")

chosen_function = fun.test

a = 0
b = 1
n = 100
result = fun.complex_newton_cortes(chosen_function, a, b, n)
print("Wynik całkowania:", result)

p = 1
script_directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_directory, 'hermite.txt')

data = fun.read_data_from_file(filename, p + 1) # + 1 as data in file shows n = 2 when it should be n = 1.
print(data)

print(fun.gauss_hermite(data, chosen_function))
print(fun.error(p))