import numpy as np
from functions import Functions as fun
import matplotlib.pyplot as plt


value = 0

choice_function = input("Podaj nr funkcji ktora chcesz wybrac: \n'1' oznacza liniową \n'2' oznacza wielomianową \n'3' oznacza trygonometryczną\n'4' oznacza z modulem z argumentu\n'5' oznacza mieszana\n")
if choice_function == '1':
    chase_function = fun.linear
elif choice_function == '2':
    level_string = int(input("Podaj stopien wielomianu ktory chcesz zbadac:"))
    level = int(level_string) 
    polynomial_list = fun.give_polynomial(fun, level)
    chase_function = fun.horner(polynomial_list)
elif choice_function == '3':
    chase_function = fun.trygonometric
elif choice_function == '4':
    chase_function = fun.absolute
else:
    chase_function = fun.mixed

left = input("Wybierz lewy przedział aproksymacji\n")
right = input("Wybierz prawy przedział aproksymacji\n")

function_range = np.linspace(float(left), float(right), 1000)
function_to_plot = chase_function(function_range)

plt.plot(function_range, function_to_plot, label='funkcja oryginalna', color='blue')

plt.show()
fun.gauss_hermite()