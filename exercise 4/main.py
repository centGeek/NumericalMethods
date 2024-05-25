import numpy as np
import os
from functions import Functions as fun

value = 0

choice_function = input("Podaj nr funkcji ktora chcesz wybrac: \n'1' oznacza liniową \n'2' oznacza wielomianową \n'3' oznacza trygonometryczną\n'4' oznacza z modulem z argumentu\n'5' oznacza mieszana\n")
if choice_function == '1':
    chosen_function = fun.linear
elif choice_function == '2':
    level_string = input("Podaj stopien wielomianu ktory chcesz zbadac:")
    level = int(level_string) 
    polynomial_list = fun.give_polynomial(fun, level)
    chosen_function = fun.horner(polynomial_list)
elif choice_function == '3':
    chosen_function = fun.trygonometric
elif choice_function == '4':
    chosen_function = fun.absolute
else:
    chosen_function = fun.mixed 

choice_method = input("Podaj sposob calkowania, ktory chcesz wybrac: \n'1' jesli metode Newtona-Cotesa(Simpsona)\ncokolwiek innego jesli Gaussa Hermita\n")
if choice_method == '1':
    choice_weight = input("Czy chcesz zastosowac wage e^(-x^2)? Jesli tak napisz '1', jesli nie napisz cokolwiek innego:\n")
    accuracy_string = input("Podaj oczekiwana dokladnosc:\n")
    accuracy = float(accuracy_string)
    if choice_weight == '1':
        value = fun.limes(fun, chosen_function, accuracy, 1)
    else:
        choice_left = input("Podaj lewy kraniec przedzialu:\n")
        choice_right = input("Podaj prawy kraniec przedzialu:\n")
        value = fun.limes_ab(fun, chosen_function, accuracy, 2, float(choice_left), float(choice_right))
else:
    number_string = input("Podaj ile chcesz przedzialow calkowania:\n")
    number = int(number_string)
    script_directory = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_directory, 'hermite.txt')
    data = fun.read_data_from_file(filename, number + 1) # + 1 as data in file shows n = 2 when it should be n = 1.
    value = fun.gauss_hermite(data, chosen_function)

print("Wynik całkowania:", value)