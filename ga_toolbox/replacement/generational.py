from .base import Replacement


class GenerationalReplacement(Replacement):
    """Offspring fully replace the current population."""

    def replace(self, population, offspring):
        if len(offspring) < len(population):
            raise ValueError("need at least as many offspring as population size")
        return offspring[:len(population)]
