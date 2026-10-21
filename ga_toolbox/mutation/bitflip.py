import random
from .base import Mutation


class BitFlipMutation(Mutation):
    """For BinaryChromosome. Each bit flips independently with probability `rate`."""

    def mutate(self, chromosome, rate):
        child = chromosome.copy()
        child.genes = [1 - g if random.random() < rate else g for g in child.genes]
        child.fitness = None
        return child
