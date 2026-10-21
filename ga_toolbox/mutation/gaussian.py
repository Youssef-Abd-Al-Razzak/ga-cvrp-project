import random
from .base import Mutation


class GaussianMutation(Mutation):
    """For FloatChromosome. Each gene gets N(0, sigma) noise with probability `rate`,
    then is clamped to [low, high]."""

    def __init__(self, sigma: float = 0.1, low: float = 0.0, high: float = 1.0):
        if sigma < 0:
            raise ValueError("sigma must be non-negative")
        if low > high:
            raise ValueError("low must not be greater than high")
        self.sigma, self.low, self.high = sigma, low, high

    def mutate(self, chromosome, rate):
        child = chromosome.copy()
        child.genes = [
            min(self.high, max(self.low, g + random.gauss(0, self.sigma)))
            if random.random() < rate else g
            for g in child.genes
        ]
        child.fitness = None
        return child
