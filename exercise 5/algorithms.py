import numpy as np
import math
class Interpolation():    
    def __init__(self) -> None:
         pass
    def weight(self, x):
        return (math.e ** ((x ** 2) * - 1))
    def hermite_polynomial(self, n, x):
        if n == 0:
            return 1
        elif n == 1:
            return 2 * x
        else:
            return 2 * x * self.hermite_polynomial(n - 1, x) - 2 * (n - 1) * self.hermite_polynomial(n - 2, x)
    def gauss_hermite(self, data, fun):
        sum = 0
        for i in range(len(data)):
            sum += data[i][0] * fun(data[i][1])
        return sum
    def coefficient(self, f,n, data):
        def integrand(x):
            return f(x) * self.hermite_polynomial(n, x)
        return self.gauss_hermite(data, integrand) / (2**n * math.factorial(n) * np.sqrt(np.pi))
    def hermite_approximation(self, f, x, max_degree, data):
        approximation = 0
        for n in range(max_degree + 1):
            coef = self.coefficient(f, n, data)
            approximation += coef * self.hermite_polynomial(n, x)
        return approximation
        