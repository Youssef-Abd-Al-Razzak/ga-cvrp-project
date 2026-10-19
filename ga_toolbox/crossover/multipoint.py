from .base import Crossover


class MultiPointCrossover(Crossover):
    def __init__(self, num_points: int = 2):
        self.num_points = num_points

    def crossover(self, parent1, parent2):
        raise NotImplementedError
