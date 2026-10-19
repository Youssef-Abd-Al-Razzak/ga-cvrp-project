from abc import ABC, abstractmethod


class Selection(ABC):
    @abstractmethod
    def select(self, population: list, n: int) -> list:
        """Return n selected chromosomes (references, not copies)."""
