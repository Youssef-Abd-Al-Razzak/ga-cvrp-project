from .base import Chromosome


class FloatChromosome(Chromosome):
    @classmethod
    def random(cls, length: int, low: float = 0.0, high: float = 1.0):
        """Genes: list of floats in [low, high]."""
        raise NotImplementedError
