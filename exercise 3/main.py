import numpy as np
import Funkcje as pf
import matplotlib.pyplot as plt

chose_function = input("Podaj nr funkcji ktora chcesz wybrac: \n'1' oznacza liniową \n'2' oznacza wielomianową \n'3' oznacza trygonometryczną\n'4' oznacza złożoną\n")
if chose_function == '1':
    chase_function = pf.load_linear
if chose_function == '2':
    level_string = input("Podaj stopien wielomianu ktory chcesz zbadac:")
    stopien = int(level_string) #fm.konwersja_string_na_integer(stopien_string)
    points = []
    points = pf.podajwielomian(stopien)
    chase_function = pf.funkcja_horner(points)
if chose_function == '3':
    chase_function = pf.load_trigonometrical
if chose_function == '4':
    chase_function = pf.load_complex_functions
    
left = input("Wybierz lewy przedział interpolacji \n")
right = input("Wybierz prawy przedział interpolacji \n")
node_amount = input("Wybierz liczbę węzłów \n")
nodes = []
values = []
for i in range(1, int(node_amount)+1):
    node = input("Wybierz położenie " + str(i) + " węzła \n")
    double_node = float(node)
    values.append(pf.value_in_function(double_node, chose_function))
    nodes.append(float(node))


def lagrange_interpolation(nodes, values, x):
    """
    Funkcja interpolująca Lagrange'a
    """
    result = 0
    for i in range(len(nodes)):
        term = values[i]
        for j in range(len(nodes)):
            if i != j:
                term *= (x - nodes[j]) / (nodes[i] - nodes[j])
        result += term
    return result


function_range = np.linspace(float(left), float(right), 1000)
function_to_plot = chase_function(function_range)  # Założenie: chase_function została zdefiniowana wcześniej

# Rysowanie wykresu
plt.plot(function_range, function_to_plot, label='funkcja oryginalna', color='blue')

interpolated_values = [lagrange_interpolation(nodes, values, x) for x in function_range]
plt.plot(function_range, interpolated_values, label = 'funcja interpolacyjna', color='green')

plt.scatter(nodes, values, label='Węzły', color='red')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolacja Lagrange\'a')
plt.legend()
plt.grid(True)


plt.show()