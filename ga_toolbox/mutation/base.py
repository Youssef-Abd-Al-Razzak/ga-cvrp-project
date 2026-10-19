from abc import ABC, abstractmethod


class Mutation(ABC):
    @abstractmethod
    def mutate(self, chromosome, rate: float):
        """Return the mutated chromosome (a copy is fine). `rate` = mutation probability."""
