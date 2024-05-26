from AbstractBaseFunction import AbstractBaseFunction
from math import sin
from math import fabs

class Polynomial(AbstractBaseFunction):
    def __init__(self, coefficients) -> None:
        super().__init__()
        self.coefficients = coefficients

    def __call__(self, argument):
        return horner(argument, self.coefficients)
    from math import sin

class Trigonometric(AbstractBaseFunction):
  
    def __init__(self, A, B, C):
        super().__init__()
        self.A = A
        self.B = B
        self.C = C

    def __call__(self, argument):
        return self.A * sin(self.B * argument + self.C)
class Modulus(AbstractBaseFunction):
   
    def __init__(self, A, B, C) -> None:
        super().__init__()
        self.A = A
        self.B = B
        self.C = C

    def __call__(self, argument):
        return self.A * fabs(self.B * argument + self.C) # A * |B * x + C|
class Exponential(AbstractBaseFunction):
    def __init__(self, A) -> None:
        super().__init__()
        self.A = A

    def __call__(self, argument):
        if argument is int:
            return exponentation(self.A, argument) #A ^ x

        return self.A ** argument
def exponentation(base, exponent):
    if exponent == 0:
        return 1
    y = 1
    while exponent > 1:
        if exponent % 2:  # odd
            y = y * base
            base = base * base
            exponent = (exponent - 1) // 2
        else:  # even
            base = base * base
            exponent //= 2
    return base * y
def horner(x, coefficients):
    value = coefficients[0]

    for coef in coefficients[1:]:
        value = value * x + coef

    return value