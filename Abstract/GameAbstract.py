from abc import ABC, abstractmethod


class GameAbstract(ABC):
    @abstractmethod
    def update(self, window, cells):
        pass

    @abstractmethod
    def nextSteps(self, window, cells):
        pass
