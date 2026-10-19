from .base import Crossover


class OrderCrossover(Crossover):
    """Order crossover (OX) for permutation chromosomes."""

    def crossover(self, parent1, parent2):
        raise NotImplementedError
