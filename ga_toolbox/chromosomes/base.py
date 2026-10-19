"""Base chromosome. Every chromosome has: genes, fitness, feasible."""
from abc import ABC, abstractmethod


class Chromosome(ABC):
    def __init__(self, genes):
        self.genes = genes
        self.fitness = None
        self.feasible = True

    @classmethod
    @abstractmethod
    def random(cls, *args, **kwargs):
        """Create a random chromosome."""

    def copy(self):
        c = type(self)(list(self.genes))
        c.fitness, c.feasible = self.fitness, self.feasible
        return c

    def get_fitness(self):
        return self.fitness

    def __len__(self):
        return len(self.genes)
