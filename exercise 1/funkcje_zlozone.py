import przyklady_funkcji as pf 
import numpy as np
def wykladnicza_i_wielomian(x):
    return np.exp(x) - 2 + x * x * (x - 2) - 5
def trygonometryczna_i_wielomian(x):
   return 5 * np.sin(x) - 3 + x * x * (x - 2) - 5
def trygonometryczna_i_wykladnicza(x):
    return 5 * np.sin(x) - 3 + np.exp(x) - 2
def wszystkie(x):
     return 5 * np.sin(x) - 3 + x * x * (x - 2) - 5 +np.exp(x) - 2
