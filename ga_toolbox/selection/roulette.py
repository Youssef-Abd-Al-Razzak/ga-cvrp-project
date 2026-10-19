from .base import Selection


class RouletteWheelSelection(Selection):
    def select(self, population, n):
        raise NotImplementedError
