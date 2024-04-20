import numpy as np
import Funkcje as pf
import matplotlib.pyplot as plt

chose_function = input("Podaj nr funkcji ktora chcesz wybrac: \n'1' oznacza liniową \n'2' oznacza wielomianową \n'3' oznacza trygonometryczną\n'4' oznacza złożoną\n")
if chose_function == '1':
    chase_function = pf.load_linear
if chose_function == '2':
    chase_function = pf.load_polynominal
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
    values.append(pf.value_in_function(node, chose_function))
    nodes.append(i)


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


# Punkty do narysowania wykresu
x_values = np.linspace(min(nodes), max(nodes), 10000)
y_values = [lagrange_interpolation(nodes, values, x) for x in x_values]

# Rysowanie wykresu
plt.plot(x_values, y_values, label='Interpolacja Lagrange\'a', color='blue')
plt.scatter(nodes, values, label='Węzły', color='red')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolacja Lagrange\'a')
plt.legend()
plt.grid(True)
plt.xlim(left, right)
plt.show()