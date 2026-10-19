"""GA hyperparameters with default values. The user can override any of them."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class GAConfig:
    pop_size: int = 100
    generations: int = 200
    crossover_rate: float = 0.9
    mutation_rate: float = 0.1
    penalty_factor: float = 1000.0   # subtracted from fitness of infeasible solutions
    seed: Optional[int] = None
    verbose: bool = True
