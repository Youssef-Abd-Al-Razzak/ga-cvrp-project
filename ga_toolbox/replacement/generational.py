from .base import Replacement


class GenerationalReplacement(Replacement):
    def replace(self, population, offspring):
        raise NotImplementedError
