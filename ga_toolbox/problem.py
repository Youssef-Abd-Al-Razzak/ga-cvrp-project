"""Problem interface. The user inherits from it to plug any problem into the GA.

Convention: HIGHER fitness = BETTER (for minimization return -cost).
"""
from abc import ABC, abstractmethod


class Problem(ABC):
    @abstractmethod
    def create_chromosome(self):
        """Return a new random Chromosome for this problem."""

    @abstractmethod
    def evaluate(self, chromosome) -> float:
        """Return the fitness of the chromosome (higher is better)."""

    @abstractmethod
    def is_feasible(self, chromosome) -> bool:
        """Return True if the chromosome satisfies all constraints."""

    def repair(self, chromosome):
        """Optional: fix an infeasible chromosome and return it. Default: no change."""
        return chromosome
