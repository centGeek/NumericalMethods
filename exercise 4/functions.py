import numpy as np

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
