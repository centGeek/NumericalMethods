import numpy as np

from Functions import Polynomial
from AbstractBaseFunction import AbstractBaseFunction
from Gauss_Hermite import gauss_hermite_quadrature


def generateHermitePolynomial(k):
    # Hi​(x) = 2xHi−1​(x) − 2(i−1)*Hi−2​(x)
    if k == 0:
        return Polynomial([1])
    elif k == 1:
        return Polynomial([2, 0])
    H0 = [1]
    H1 = [2, 0]
    current = []
    for i in range(2, k + 1):
        current = [2 * x for x in H1]
        current.append(0)
        l0 = len(H0)
        l1 = len(current)
        for j in range(len(H0)):
            current[l1 - 1 - j] -= 2 * (i - 1) * H0[l0 - 1 - j]
        H0 = H1
        H1 = current
        # current - wspolczynniki wielomianu
    return Polynomial(current)


class ApproximationPolynomial(AbstractBaseFunction):
    def __init__(self, approximationCoefficients) -> None:
        super().__init__()
        self.approximationCoefficients = approximationCoefficients
        self.hermitePolynomials = []
        for i in range(len(approximationCoefficients)):
            self.hermitePolynomials.insert(0, generateHermitePolynomial(i))



    def __call__(self, x):
        return sum(self.approximationCoefficients[i] * (self.hermitePolynomials[i])(x) for i in range(len(self.hermitePolynomials)))


def approximate(func, degree, nodes):
    coeffs = []
    for i in range(degree + 1):
        hermite = generateHermitePolynomial(i)
        fg = lambda x : hermite(x) * func(x)
        # Definiowanie funkcji dla mianownika: całka z H_i(x)^2 * e^(-x^2) dx
        gg = lambda x : hermite(x) * hermite(x)

        # Obliczanie i-tego współczynnika za pomocą kwadratury Gaussa-Hermite'a
        c = gauss_hermite_quadrature(nodes, fg) / gauss_hermite_quadrature(nodes, gg)

        coeffs.insert(0, c)

    return ApproximationPolynomial(coeffs)


def approximate_iterative(func, nodes, eps):
    d = 0
    a = approximate(func, d, nodes)  # Początkowa aproksymacja dla stopnia 0
    # Definiowanie funkcji błędu: (a(x) - f(x))^2
    diff = lambda x : a(x) - func(x)
    diff_sq = lambda x : diff(x) * diff(x)

    error = gauss_hermite_quadrature(nodes, diff_sq)
    # Iteracja w celu zwiększania stopnia wielomianu, aż błąd będzie poniżej progu
    while (error >= eps):
        d += 1
        a = approximate(func, d, nodes)
        diff = lambda x : a(x) - func(x)
        diff_sq = lambda x : diff(x) * diff(x)
        error = gauss_hermite_quadrature(nodes, diff_sq)
    # Zwracanie końcowego aproksymacyjnego wielomianu
    return a


def horner(list_of_coefs, x):
    result = list_of_coefs[0]

    for i in range(1, len(list_of_coefs)):
        result = result * x + list_of_coefs[i]

    return result


def approximation_error(left, right, function, approximation): 
    # MSE=  1/n * ​∑i=1n​(f(xi​)−a(xi​))^2
    error = 0
    points = np.linspace(left, right)

    # Obliczanie błędu kwadratowego dla każdego punktu
    for i in range(len(points)):
        error += (approximation(points[i]) - function(points[i])) * (approximation(points[i]) - function(points[i]))
    # Obliczanie średniego błędu kwadratowego
    error = error / len(points)

    return error
