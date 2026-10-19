"""CVRP instance data + file reader."""
from dataclasses import dataclass


@dataclass
class CVRPInstance:
    name: str
    capacity: int
    coords: list        # coords[i] = (x, y); index 0 = depot
    demands: list       # demands[i]; demands[0] = 0

    @property
    def num_customers(self) -> int:
        return len(self.coords) - 1


def load_instance(path: str) -> CVRPInstance:
    raise NotImplementedError
