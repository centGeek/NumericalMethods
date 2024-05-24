import math
import numpy as np

class Functions:
    def __init__(self):
        init()

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
                        data.append((float(numbers[0]), float(numbers[1]))) #numbers[0] contains xi, numbers[1] contains Ai
        return data
    
    def give_polynomial(self, stopien):
        wielomian = []
        for i in range(stopien + 1):
            wspolczynnik_string = input("Podaj współczynnik przy x^" + str(i) + ": ")
            wspolczynnik = float(wspolczynnik_string)
            wielomian.append(wspolczynnik)
        wielomian.reverse()
        return wielomian
    
    def horner(polynominal):
        def horner(x):
            result = 0
            for i in range(len(polynominal) - 1, -1, -1):
                result = result * x + polynominal[i]
            return result
        return horner
    
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
            diff = math.fabs(sum - previousSum)
            previousSum = sum
            if math.fabs(diff) < accuracy:
                condition = False

        return sum
    """def horner_in_place(x, polynominal_list):
        result = 0
        for i in range(len(polynominal_list) - 1, -1, -1):
            result = result * x + polynominal_list[i]
        return result
    
    def horner_in_place_weight(x, polynominal_list):
        result = 0
        for i in range(len(polynominal_list) - 1, -1, -1):
            result = result * x + polynominal_list[i]
        return ((math.e ** ((-1) *x ** 2)) * result)"""
       
    def limes (self, f, accuracy, weight):
        lim = 10.0
        temp = 0.0
        result = 0.0

        a = 0.0
        b = lim
        condition = True

        while condition:
            temp = self.complex_newton_cotes(self, f, a, b, accuracy, weight)
            result += temp
            a = b
            b = b + ((lim - b) / 2)
            if math.fabs(temp) < accuracy:
                condition = False

        a = (-1) * lim
        b = 0.0
        condition = True

        while condition:
            temp = self.complex_newton_cotes(self, f, a, b, accuracy, weight)
            result += temp
            b = a
            a = a - ((lim - math.fabs(b)) / 2)
            if math.fabs(temp) < accuracy:
                condition = False

        return result
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
            diff = math.fabs(sum - previousSum)
            previousSum = sum
            if math.fabs(diff) < accuracy:
                condition = False

        return sum
    def gauss_hermite(data, fun):
        sum = 0
        for i in range(len(data)):
            sum += data[i][0] * fun(data[i][1])
        return sum
    
    """def error(n):
        return math.factorial(n + 1) * math.sqrt(math.pi) / (2 ** (n + 1)) / math.factorial(2 * n + 2)"""

    def linear(x):
        return x * 2 - 1

    def trygonometric(x):
        return math.cos(2 * x * x + 1)
    
    def absolute(x):
        return math.fabs(x + 2) - 3
    
    def mixed(x):
        return math.cos(x) - x * x * x
    
    def weight(x):
        return (math.e ** ((x ** 2) * - 1))