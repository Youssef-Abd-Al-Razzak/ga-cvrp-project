from abc import ABC, abstractmethod


class Crossover(ABC):
    @abstractmethod
    def crossover(self, parent1, parent2):
        """Return (child1, child2) as NEW chromosomes. Parents must not be modified."""
