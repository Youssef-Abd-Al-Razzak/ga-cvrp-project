from .base import Mutation


class GaussianMutation(Mutation):
    """For FloatChromosome."""

    def __init__(self, sigma: float = 0.1, low: float = 0.0, high: float = 1.0):
        self.sigma, self.low, self.high = sigma, low, high

    def mutate(self, chromosome, rate):
        raise NotImplementedError
