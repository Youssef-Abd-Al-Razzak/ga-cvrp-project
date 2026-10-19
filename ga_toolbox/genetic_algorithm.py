"""GA engine. It knows nothing about the specific problem."""
from .config import GAConfig


class GeneticAlgorithm:
    def __init__(self, problem, selection, crossover, mutation, replacement,
                 config: GAConfig = None):
        raise NotImplementedError

    def _evaluate(self, chromosome):
        """Set chromosome.feasible and chromosome.fitness (apply penalty/repair if infeasible)."""
        raise NotImplementedError

    def run(self):
        """Run the GA loop and return the best Chromosome found."""
        raise NotImplementedError
