from .base import Chromosome


class IntegerChromosome(Chromosome):
    @classmethod
    def random(cls, length: int, low: int = 0, high: int = 1, permutation: bool = False):
        """Genes: list of ints in [low, high]. If permutation=True: a shuffled permutation
        of the values low..high (length must equal high-low+1)."""
        raise NotImplementedError
