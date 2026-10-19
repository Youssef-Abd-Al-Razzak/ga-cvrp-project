from .base import Chromosome


class BinaryChromosome(Chromosome):
    @classmethod
    def random(cls, length: int):
        """Genes: list of 0/1."""
        raise NotImplementedError
