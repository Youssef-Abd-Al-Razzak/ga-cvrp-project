from .base import Chromosome
import random


class FloatChromosome(Chromosome):
    @classmethod
    def random(cls, length: int, low: float = 0.0, high: float = 1.0):
        if length < 0:
            raise ValueError("length must be non-negative")
        if low > high:
            raise ValueError("low must not be greater than high")
        return cls([random.uniform(low, high) for _ in range(length)])
