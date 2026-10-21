import random
from .base import Mutation


class InversionMutation(Mutation):
    """Reverse a random segment. For permutation chromosomes.
    `rate` = probability that the chromosome is mutated at all."""

    def mutate(self, chromosome, rate):
        child = chromosome.copy()
        n = len(child.genes)
        if n >= 2 and random.random() < rate:
            a, b = sorted(random.sample(range(n), 2))
            child.genes[a:b + 1] = child.genes[a:b + 1][::-1]
            child.fitness = None
        return child
