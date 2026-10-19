# Interfaces Contract

**Do NOT rename classes, methods, or parameters without telling the whole team.**
Fitness convention: **higher = better** (for minimization return `-cost`).

| File | Class | Signature |
|---|---|---|
| `config.py` | `GAConfig` | dataclass: `pop_size, generations, crossover_rate, mutation_rate, penalty_factor, seed, verbose` |
| `problem.py` | `Problem` | `create_chromosome()`, `evaluate(ch)`, `is_feasible(ch)`, `repair(ch)` |
| `genetic_algorithm.py` | `GeneticAlgorithm` | `__init__(problem, selection, crossover, mutation, replacement, config=None)`, `run() -> best` |
| `chromosomes/base.py` | `Chromosome` | attrs: `genes, fitness, feasible`; `copy()`, `random(...)` (classmethod) |
| `chromosomes/binary.py` | `BinaryChromosome` | `random(length)` |
| `chromosomes/integer.py` | `IntegerChromosome` | `random(length, low=0, high=1, permutation=False)` |
| `chromosomes/floating.py` | `FloatChromosome` | `random(length, low=0.0, high=1.0)` |
| `selection/*` | `RouletteWheelSelection()`, `TournamentSelection(tournament_size=3)` | `select(population, n) -> list` |
| `crossover/*` | `MultiPointCrossover(num_points=2)`, `OrderCrossover()` | `crossover(p1, p2) -> (c1, c2)` |
| `mutation/*` | `BitFlipMutation`, `SwapMutation`, `InversionMutation`, `GaussianMutation(sigma, low, high)` | `mutate(ch, rate) -> ch` |
| `replacement/*` | `GenerationalReplacement()`, `ElitismReplacement(elite_size=2)` | `replace(population, offspring) -> new_population` |
| `cvrp/instance.py` | `CVRPInstance`, `load_instance(path)` | fields: `name, capacity, coords, demands` (index 0 = depot) |
| `cvrp/cvrp_problem.py` | `CVRPProblem(Problem)` | `decode(ch) -> routes`, `distance(i, j)`, `total_distance(routes)`, `is_feasible`, `evaluate` |
| `cvrp/output.py` | - | `print_solution(problem, chromosome)` |

## Rules
- Operators never modify parents in place; return new chromosomes.
- Every chromosome type uses `.genes` as a Python list.
- Imports are absolute from the project root: `from ga_toolbox.problem import Problem`.
