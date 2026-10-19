from abc import ABC, abstractmethod


class Replacement(ABC):
    @abstractmethod
    def replace(self, population: list, offspring: list) -> list:
        """Return the NEW population (same size as `population`). Both inputs are evaluated."""
