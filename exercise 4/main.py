import numpy as np
import os
polynolmal_list = []
accuracy = input("Podaj dokładność do obliczania: ")
def function(x):
    return x**2
def complex_newton_cortes(f, a, b, n):

    if n % 2 != 0:
        raise ValueError("Liczba podprzedziałów musi być parzysta")

    h = (b - a) / n
    suma = f(a) + f(b)

    for i in range(1, n, 2):
        suma += 4 * f(a + i * h)

    for i in range(2, n-1, 2):
        suma += 2 * f(a + i * h)

    wynik = (h / 3) * suma
    return wynik
a = 0
b = 1
n = 100
result = complex_newton_cortes(function, a, b, n)
print("Wynik całkowania:", result)

p = 4
script_directory = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(script_directory, 'hermite.txt')
#filename = "hermite.txt"
def read_data_from_file(filename, p):
    data = []
    with open(filename, 'r') as file:
        found_n = False
        for line in file:
            if line.startswith("n = " + str(p)):
                found_n = True
            elif found_n and line.startswith("n = "):
                lines = file.readlines()
                line = lines[-1]
            elif found_n:
                numbers = line.split('   ')
                if numbers[0] != '\n':
                    data.append((float(numbers[0]), float(numbers[1])))
    return data
data = read_data_from_file(filename, p)
print(data)
