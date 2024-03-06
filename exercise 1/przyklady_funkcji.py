import numpy as np
from sympy import symbols, diff
def sinus(x):
    return 5 * np.sin(x) - 3 

def wielomian(x):
    return x * x * (x - 2) - 5
def poch_wielomian(x):
    return

def wykladnicza(x):
    return np.exp(x) - 2
def pochodna_wykladniczej():
    x = symbols('x')
    wykladnicza_sym =np.exp(x) - 2
    pochodna = diff(wykladnicza_sym, x)
    return pochodna

def poch_sinus(x):
    return 5 * np.cos(x)