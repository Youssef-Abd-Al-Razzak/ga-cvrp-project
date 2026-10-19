import random
from .base import Selection
 
class TournamentSelection(Selection):
    def __init__(self, tournament_size: int = 3):
        if tournament_size < 1:
            raise ValueError("tournament_size must be >= 1")
        self.tournament_size = tournament_size
        
    def select(self, population, n):
        if not population:
            raise ValueError("population is empty")
        k = min(self.tournament_size, len(population))
        selected = []
        for _ in range(n):
            contenders = random.sample(population, k)
            selected.append(max(contenders, key=lambda c: c.fitness))
        return selected
 