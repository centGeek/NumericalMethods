
from AbstractBaseFunction import AbstractBaseFunction

class Nested(AbstractBaseFunction):
    def __init__(self, functions) -> None:
        super().__init__()
        self.functions = functions

    def __call__(self, argument):
        for function in self.functions:
            argument = function(argument)

        return argument
