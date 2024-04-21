import numpy as np

# def load_polynominal(x):
#     return x *(x *(x + 3) + 4) + 5
def load_linear(x):
    return 3 * x + 2
def load_trigonometrical(x):
    return np.sin(x)
def load_complex_functions(x):
    return x * x * (3 + x) + 3 * x + 10  * np.cos(x) + 3 * np.sin(x)
def load_absolute_value(x):
     return 3 * abs(x) + 2

def value_in_function(x, chase_function, polynominal_list) -> int:
    value = 0
    if(chase_function == "1"):
        value = load_linear(x)
    if(chase_function == "2"):
            value = horner_in_place(x, polynominal_list)
    if(chase_function == "3"):
            value = load_trigonometrical(x)
    if(chase_function == "4"):
        value = load_absolute_value(x)
    if(chase_function == "5"):
        value = load_complex_functions(x)
    return value
def horner(polynominal):
    def horner(x):
        result = 0
        for i in range(len(polynominal) - 1, -1, -1):
            result = result * x + polynominal[i]
        return result
    return horner
def horner_in_place(x, polynominal_list):
    result = 0
    for i in range(len(polynominal_list) - 1, -1, -1):
        result = result * x + polynominal_list[i]
    return result
def give_polynominal(stopien):
        polynominal = []
        for i in range(stopien + 1):
            point_string = input("Podaj współczynnik przy x^" + str(i) + ": ")
            point = float(point_string)
            polynominal.append(point)
        return polynominal