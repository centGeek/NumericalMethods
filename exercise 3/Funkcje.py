import numpy as np
def load_polynominal(x):
    return x *(x *(x + 3) + 4) + 5
def load_linear(x):
    return 3 * x + 2
def load_trigonometrical(x):
    return 5 * np.cos(x) + 3 * np.sin(x)
def load_complex_functions(x):
    return x * x * (3 + x) + 3 * x + 10  * np.cos(x) + 3 * np.sin(x)

def value_in_function(x, chase_function) -> int:
    value = 0
    if(chase_function == "1"):
        value = load_linear(x)
    if(chase_function == "2"):
        value = load_polynominal(x)
    if(chase_function == "3"):
        value = load_trigonometrical(x)
    if(chase_function == "4"):
        value = load_complex_functions(x)
    return value
def funkcja_horner(wielomian):
        def horner(x):
            n = len(wielomian)
            result = wielomian[0]
            for i in range(1, n):
                result = result * x + wielomian[i]
            return result
        return horner