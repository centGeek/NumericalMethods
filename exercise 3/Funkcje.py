import numpy as np
# def load_polynominal(x):
#     return x *(x *(x + 3) + 4) + 5
def load_linear(x):
    return 3 * x + 2
def load_trigonometrical(x):
    return 5 * np.cos(x) + 3 * np.sin(x)
def load_complex_functions(x):
    return x * x * (3 + x) + 3 * x + 10  * np.cos(x) + 3 * np.sin(x)

def value_in_function(x, chase_function, polynomial_list) -> int:
    value = 0
    if(chase_function == "1"):
        value = load_linear(x)
    if(chase_function == "2"):
        for i in range(0, len(polynomial_list)):
            value += polynomial_list[i] * (x ** i)
    if(chase_function == "3"):
            value = load_trigonometrical(x)
    if(chase_function == "4"):
        value = load_complex_functions(x)
    return value
def funkcja_horner(wielomian):
    def horner(x):
        result = 0
        for i in range(len(wielomian) - 1, -1, -1):
            result = result * x + wielomian[i]
        return result
    return horner
def podajwielomian(stopien):
        wielomian = []
        for i in range(stopien + 1):
            wspolczynnik_string = input("Podaj współczynnik przy x^" + str(i) + ": ")
            wspolczynnik = float(wspolczynnik_string)
            wielomian.append(wspolczynnik)
        return wielomian