from .base import Chromosome
import random


class BinaryChromosome(Chromosome):
    @classmethod
    def random(cls, length: int):
        """Genes: list of 0/1."""
        if length < 0:
            raise ValueError("length must be non-negative")
        return cls([random.randint(0, 1) for _ in range(length)])