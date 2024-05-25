import numpy as np
import math
class Functions:
    def __init__(self):
        pass

    def read_data_from_file(self, filename, p):
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
    
    def weight(x):
        return (math.e ** ((x ** 2) * - 1))
    
    def linear(x):
        return x * 2 - 1
    
    def trygonometric(x):
        return np.cos(2 * x * x + 1)
    
    def absolute(x):
        return np.fabs(x + 2) - 3
    
    def mixed(x):
        return np.cos(x) - x * x * x
    
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
   