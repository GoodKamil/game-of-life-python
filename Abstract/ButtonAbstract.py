from abc import ABC, abstractmethod


class ButtonAbstract(ABC):
    @abstractmethod
    def draw(self, surface):
        pass

    @abstractmethod
    def check_click(self):
        pass

    @abstractmethod
    def setEnabled(self, boolean):
        pass
