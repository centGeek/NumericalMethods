from abc import ABC, abstractmethod

class AbstractBaseFunction(ABC):
    @abstractmethod
    def __call__(self, argument):
        pass
