from CLI import prompt_main
from hermitePolynomial import approximate, approximate_iterative, approximation_error
from plot_service import plot_approximation


check, function, left, right, tmp, nodes = prompt_main()

app = None
if check == 2: # iterative
    error = tmp
    app = approximate_iterative(function, nodes, error)
    print('wspolczynniki wielomianu aproksymujacego:', app.approximationCoefficients)
    error = approximation_error(left, right, function, app)
    print('error:', error)
else: # degree
    degree = tmp
    app = approximate(function, degree, nodes)
    error = approximation_error(left, right, function, app)

    print(f'Blad aproksymacji: {error:.5f}')
    print(f'Wspolczynniki wielomianu aproksymacji: ', app.approximationCoefficients)

plot_approximation(function, app, left, right)
