from abc import ABC, abstractmethod


class GameAbstract(ABC):
    @abstractmethod
    def update(self, window, cells):
        pass

    @abstractmethod
    def playing_field(self, window, cells):
        pass
