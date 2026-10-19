from .base import Replacement


class ElitismReplacement(Replacement):
    def __init__(self, elite_size: int = 2):
        self.elite_size = elite_size

    def replace(self, population, offspring):
        raise NotImplementedError
