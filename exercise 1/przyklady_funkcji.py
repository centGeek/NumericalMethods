import numpy as np
from sympy import symbols, diff

def sinus(x):
    return 5 * np.sin(x) - 3 

def wielomian(x):
    return x * x * (x - 2) - 5
def poch_wielomian(x):
    return 3 * x * x - 4 * x

def wykladnicza(x):
    return np.exp(x) - 2
def pochodna_wykladniczej(x):
    return np.e ** x

def poch_sinus(x):
    return 5 * np.cos(x)
