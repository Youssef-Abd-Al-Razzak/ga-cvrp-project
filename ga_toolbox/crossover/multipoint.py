import random
from .base import Crossover

class MultiPointCrossover(Crossover):
    def __init__(self, num_points: int = 2):
        if num_points < 1:
            raise ValueError("num_points must be >= 1")
        self.num_points = num_points

    def crossover(self, parent1, parent2):
        g1, g2 = parent1.genes, parent2.genes
        length = len(g1)
        if length != len(g2):
            raise ValueError("parents must have the same length")
        if length < 2:
            return parent1.copy(), parent2.copy()
        k = min(self.num_points, length - 1)
        points = sorted(random.sample(range(1, length), k))
        child1_genes, child2_genes = [], []
        prev, swap = 0, False

        for point in points + [length]:
            seg1, seg2 = g1[prev:point], g2[prev:point]
            if swap:
                seg1, seg2 = seg2, seg1
            child1_genes.extend(seg1)
            child2_genes.extend(seg2)
            swap = not swap
            prev = point
        child1 = type(parent1)(child1_genes)
        child2 = type(parent2)(child2_genes)
        return child1, child2