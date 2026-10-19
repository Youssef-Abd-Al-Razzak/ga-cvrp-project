import bisect
import random
from .base import Selection

class RouletteWheelSelection(Selection):
    def select(self, population, n):
        if not population:
            raise ValueError("population is empty")
        fits = [ind.fitness for ind in population]
        if any(f is None for f in fits):
            raise ValueError("all chromosomes must be evaluated before selection")
        lowest = min(fits)
        eps = 1e-9
        weights = [f - lowest + eps for f in fits]
        cumulative, total = [], 0.0
        for w in weights:
            total += w
            cumulative.append(total)
        selected = []
        for _ in range(n):
            spin = random.uniform(0, total)
            idx = bisect.bisect_left(cumulative, spin)
            selected.append(population[min(idx, len(population) - 1)])
        return selected