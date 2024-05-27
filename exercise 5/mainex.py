from scipy.special import roots_hermite

# Liczba punktów (n)
n = 2
nodes, weights = roots_hermite(n)
print("Węzły:", nodes)
print("Wagi:", weights)
n=3
nodes, weights = roots_hermite(n)
print("Węzły:", nodes)
print("Wagi:", weights)
