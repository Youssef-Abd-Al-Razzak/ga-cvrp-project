from ga_toolbox.chromosomes.base import Chromosome
from .base import Replacement


class ElitismReplacement(Replacement):
    """Keep the best `elite_size` parents, fill the rest with the best offspring."""

    def __init__(self, elite_size: int = 2):
        if elite_size < 0:
            raise ValueError("elite_size must be non-negative")
        self.elite_size = elite_size

    def replace(self, population, offspring):
        n = len(population)
        k = min(self.elite_size, n)
        if len(offspring) < n - k:
            raise ValueError("not enough offspring to fill the population")
        elites = sorted(population, key=Chromosome.get_fitness, reverse=True)[:k]
        rest = sorted(offspring, key=Chromosome.get_fitness, reverse=True)[:n - k]
        return elites + rest
