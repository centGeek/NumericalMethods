import numpy as np
def wykladnicza_i_wielomian(x):
    return np.exp(x)  + x * x * (x - 2) - 7
def trygonometryczna_i_wielomian(x):
   return 5 * np.sin(x)  + x * x * (x - 2) - 8
def trygonometryczna_i_wykladnicza(x):
    return np.sin(np.exp(x))
def wszystkie(x):
     return np.exp(np.sin(x * x - 1)) - 2
def wykladnicza_i_wielomian_poch(x):
    return np.exp(x) + x * (3 * x - 4)
def trygonometryczna_i_wykladnicza_poch(x):
    return np.cos(np.exp(x)) * np.exp(x)
def trygonometryczna_i_wielomian_poch(x):
    return 5 * np.cos(x) + x * (3 * x - 4)
def wszystkie_poch(x):
    return 2 * x * np.exp(np.sin(x * x - 1)) * np.cos(x * x -1)
