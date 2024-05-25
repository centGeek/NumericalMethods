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
number_string = input("Podaj ile chcesz przedzialow calkowania:\n")
number = int(number_string)
function_range = np.linspace(left, right, 1000)
accuracy = float(input("Podaj dokładność dla metody całkowania: "))
weight = int(input("Podaj wagę (1 lub 0): "))

function_to_plot = chosen_function(function_range)
script_directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_directory, 'hermite.txt')
data = fun.read_data_from_file(filename, number + 1)

hermite_approx = alg.hermite_interpolation(chosen_function, level, left, right, accuracy, weight)
x_values = np.linspace(left, right, 400)
print(x_values)
original_values = np.array([chosen_function(x) for x in x_values])
print(original_values)
approx_values = np.array([hermite_approx(x) for x in x_values])

plt.plot(x_values, original_values, label='Oryginalna funkcja')
plt.plot(x_values, approx_values, label='Aproksymacja Hermite\'a', linestyle='dashed')


plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Aproksymacja funkcji przy użyciu wielomianów Hermite\'a')
plt.grid(True)
plt.show()
