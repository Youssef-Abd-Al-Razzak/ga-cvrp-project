"""CVRP built on top of the GA toolbox. Solution = permutation of customers 1..n."""
from ga_toolbox.problem import Problem
from .instance import CVRPInstance


class CVRPProblem(Problem):
    def __init__(self, instance: CVRPInstance):
        self.instance = instance

    def create_chromosome(self):
        """IntegerChromosome (permutation) of customers 1..n."""
        raise NotImplementedError

    def decode(self, chromosome) -> list:
        """Split the permutation into routes. Return list of routes (each a list of customers)."""
        raise NotImplementedError

    def distance(self, i: int, j: int) -> float:
        raise NotImplementedError

    def total_distance(self, routes: list) -> float:
        raise NotImplementedError

    def is_feasible(self, chromosome) -> bool:
        raise NotImplementedError

    def evaluate(self, chromosome) -> float:
        """Return -total_distance."""
        raise NotImplementedError
