import numpy as np
import math
class Interpolation():    
    def __init__(self) -> None:
         pass
    def weight(self, x):
        return (math.e ** ((x ** 2) * - 1))
    def complex_newton_cotes(self, f, a, b, accuracy, weight):
        n = 1
        condition = True
        previousSum = float('-inf')
        while condition:
            sum = 0.0
            aux1sum = 0.0
            aux2sum = 0.0

            n = n * 2
            h = (b - a) / n
            amount = n + 1
            fx = []

            for i in range(amount):
                if weight == 1:
                    fx.append(f(a + i * h) * self.weight(a + i * h))
                else:
                    fx.append(f(a + i * h))
                if i % 2 == 0 and i != 0 and i != (amount - 1):
                    aux1sum = aux1sum + 2 * fx[i]
                elif i % 2 != 0 and i != 0 and i != (amount - 1):
                    aux2sum = aux2sum + 4 * fx[i]

            sum = (h / 3) * (fx[0] + fx[amount - 1] + aux1sum + aux2sum)
            diff = np.fabs(sum - previousSum)
            previousSum = sum
            if np.fabs(diff) < accuracy:
                condition = False

        return sum
    def lagrange_basis(self, x, x_nodes, j):
        L_j = 1
        for m in range(len(x_nodes)):
            if m != j:
                L_j *= (x - x_nodes[m]) / (x_nodes[j] - x_nodes[m])
        return L_j

    def hermite_basis(self, x, x_nodes, weights, j):
        H_j = weights[j] * np.exp(-(x**2)/2) * self.lagrange_basis(x, x_nodes, j)
        return H_j

    def hermite_interpolation(self, f, n, a, b, accuracy, weight):
        nodes, weights = np.polynomial.hermite.hermgauss(n)
        nodes = 0.5 * (nodes + 1) * (b - a) + a  # Przekształcenie węzłów do przedziału [a, b]

        f_values = np.array([f(node) for node in nodes])
        
        def approximating_function(x):
            P_x = 0
            for j in range(n):
                integral_value = self.complex_newton_cotes(lambda t: f(t) * self.hermite_basis(t, nodes, weights, j), a, b, accuracy, weight)
                P_x += integral_value * self.hermite_basis(x, nodes, weights, j)
            return P_x
        
        return approximating_function
    
            
        