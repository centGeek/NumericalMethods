import numpy as np
import os
from functions import Functions as fun

a = float('-inf')
b = float('inf')
value = 0

choice_function = input("Podaj nr funkcji ktora chcesz wybrac: \n'1' oznacza liniową \n'2' oznacza wielomianową \n'3' oznacza trygonometryczną\n'4' oznacza z modulem z argumentu\n")
if choice_function == '1':
    chosen_function = fun.linear
    #chosen_function_weigth = fun.linear_weight
elif choice_function == '2':
    level_string = input("Podaj stopien wielomianu ktory chcesz zbadac:")
    level = int(level_string) 
    polynomial_list = fun.give_polynomial(level)
    #chosen_function = fun.horner(polynomial_list)
elif choice_function == '3':
    chosen_function = fun.trygonometric
    #chosen_function_weigth = fun.trygonometric_weight
else:
    chosen_function = fun.absolute
    #chosen_function_weigth = fun.absolute_weight

choice_method = input("Podaj sposob calkowania, ktory chcesz wybrac: \n'1' jesli metode Newtona-Cotesa(Simpsona)\ncokolwiek innego jesli Gaussa Hermita\n")
if choice_method == 1:
    chosen_method = 1
    choice_weight = input("Czy chcesz zastosowac wage e^(-x^2)? Jesli tak napisz '1', jesli nie napisz cokolwiek innego:\n")
    accuracy = input("Podaj oczekiwana dokladnosc:\n")
    if choice_weight == '1':
        value = fun.complex_newton_cotes(chosen_function, a, b, accuracy, 1)
    else:
        value = fun.complex_newton_cotes(chosen_function, a, b, accuracy, 2)
else:
    chosen_method = 2




accuracy = input("Podaj dokładność do obliczania: ")

chosen_function = fun.test

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