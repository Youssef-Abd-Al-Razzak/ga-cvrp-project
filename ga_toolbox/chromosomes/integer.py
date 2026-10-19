from .base import Chromosome
import random

class IntegerChromosome(Chromosome):
    @classmethod
    def random(cls, length: int, low: int = 0, high: int = 1, permutation: bool = False):
        if length < 0:
            raise ValueError("length must be non-negative")
        if low > high:
            raise ValueError("low must not be greater than high")
        if permutation:
            values = list(range(low, high + 1))
            if len(values) != length:
                raise ValueError("permutation length must equal high - low + 1")
            random.shuffle(values)
            return cls(values)
        return cls([random.randint(low, high) for _ in range(length)])
