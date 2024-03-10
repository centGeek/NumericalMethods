import przyklady_funkcji as pf 
import numpy as np
def wykladnicza_i_wielomian(x):
    return np.exp(x)  + x * x * (x - 2) - 7
def trygonometryczna_i_wielomian(x):
   return 5 * np.sin(x)  + x * x * (x - 2) - 8
def trygonometryczna_i_wykladnicza(x):
    return 5 * np.sin(x) + np.exp(x) - 5
def wszystkie(x):
     return 5 * np.sin(x)  + x * x * (x - 2)  +np.exp(x) - 10
def pochodna_wykladnicza_i_wielomian(x):
    return np.e**2 + 3 * x * x - 4 * x
def poch_trygonometryczna_i_wykladnicza(x):
    return 5 * np.cos(x) + np.e**2
def poch_trygonometryczna_i_wielomian(x):
    return 5 * np.cos(x) + 3 * x * x - 4 * x
def poch_wszystkie(x):
    return 5 * np.cos(x) + np.e**2 + 3 * x * x - 4 * x