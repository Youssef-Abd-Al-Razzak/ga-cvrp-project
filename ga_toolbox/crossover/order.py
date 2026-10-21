import random
from .base import Crossover

class OrderCrossover(Crossover):
    def crossover(self, parent1, parent2):
        n = len(parent1.genes)
        if n != len(parent2.genes):
            raise ValueError("parents must have the same length")
        if n < 2:
            return parent1.copy(), parent2.copy()
        a, b = sorted(random.sample(range(n), 2))
        child1 = type(parent1)(self._ox(parent1.genes, parent2.genes, a, b))
        child2 = type(parent2)(self._ox(parent2.genes, parent1.genes, a, b))
        return child1, child2

    @staticmethod
    def _ox(keep_from, fill_from, a, b):
        n = len(keep_from)
        child = [None] * n
        child[a:b + 1] = keep_from[a:b + 1]
        used = set(child[a:b + 1])
        order = [fill_from[(b + 1 + i) % n] for i in range(n)]
        remaining = [g for g in order if g not in used]
        positions = [(b + 1 + i) % n for i in range(n - (b - a + 1))]
        for pos, gene in zip(positions, remaining):
            child[pos] = gene
        return child