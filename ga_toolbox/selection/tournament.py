from .base import Selection


class TournamentSelection(Selection):
    def __init__(self, tournament_size: int = 3):
        self.tournament_size = tournament_size

    def select(self, population, n):
        raise NotImplementedError
