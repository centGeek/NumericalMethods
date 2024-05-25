import numpy as np
from functions import Functions as fun
import matplotlib.pyplot as plt
import os
from algorithms import Interpolation

alg = Interpolation()
value = 0
choice_function = input("Podaj nr funkcji ktora chcesz wybrac: \n'1' oznacza liniową \n'2' oznacza wielomianową \n'3' oznacza trygonometryczną\n'4' oznacza z modulem z argumentu\n'5' oznacza mieszana\n")
if choice_function == '1':
    chosen_function = fun.linear
elif choice_function == '2':
    level_string = int(input("Podaj stopien wielomianu ktory chcesz zbadac:"))
    level = int(level_string) 
    polynomial_list = fun.give_polynomial(fun, level)
    chosen_function = fun.horner(polynomial_list)
elif choice_function == '3':
    chosen_function = fun.trygonometric
elif choice_function == '4':
    chosen_function = fun.absolute
else:
    chosen_function = fun.mixed

left = float(input("Wybierz lewy przedział aproksymacji\n"))
right = float(input("Wybierz prawy przedział aproksymacji\n"))
function_range = np.linspace(left, right, 1000)
accuracy = float(input("Podaj dokładność dla metody całkowania: "))
number_string = input("Podaj ile chcesz przedzialow calkowania:\n")
number = int(number_string)
script_directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_directory, 'hermite.txt')
data = fun.read_data_from_file(filename, number + 1)


function_to_plot = chosen_function(function_range)
script_directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_directory, 'hermite.txt')
data = fun.read_data_from_file(filename, number + 1)
value = alg.gauss_hermite(data, chosen_function)
max_degree = 5
number_of_points = 20 
x_values = np.linspace(-2, 2, 100)
data = fun.read_data_from_file(filename, number_of_points + 1)
approximated_values = [alg.hermite_approximation(fun.horner, x, max_degree, data) for x in x_values]

plt.plot(x_values, [chosen_function(x) for x in x_values], label='Original function')
plt.plot(x_values, approximated_values, label='Hermite approximation')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function approximation using Hermite polynomials')
plt.show()
