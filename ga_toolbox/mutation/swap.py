import random
from .base import Mutation


class SwapMutation(Mutation):
    """Swap two genes. For permutation chromosomes.
    `rate` = probability that the chromosome is mutated at all."""

    def mutate(self, chromosome, rate):
        child = chromosome.copy()
        n = len(child.genes)
        if n >= 2 and random.random() < rate:
            i, j = random.sample(range(n), 2)
            child.genes[i], child.genes[j] = child.genes[j], child.genes[i]
            child.fitness = None
        return child
