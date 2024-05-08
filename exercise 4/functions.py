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

    def gauss_hermite(data, fun):
        sum = 0
        for i in range(len(data)):
            #print(str(data[i][0]) + " " + str(data[i][1]))
            sum += data[i][0] * fun(data[i][1])
            #print(str(sum) + '\n')
        return sum
    
    def error(n):
        return math.factorial(n + 1) * math.sqrt(math.pi) / (2 ** (n + 1)) / math.factorial(2 * n + 2)

    def function(x):
        return x**2
    
    def cosinus(x):
        return math.cos(2 * x * x + 1)
    
    def test(x):
        return math.sqrt(4 - x * x)