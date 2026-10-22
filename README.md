# ga-cvrp-project

Genetic Algorithm toolbox (`ga_toolbox/`) + CVRP application (`cvrp/`). No GA libraries used.

## Run
    python -m cvrp.main data/sample-n30.vrp --seed 1
    python -m cvrp.main <file> --pop 300 --gens 1000 --cx 0.9 --mut 0.2 --elite 5 --verbose

Output format:
    Route #1: 2 28 16 18 8
    Route #2: ...
    Cost: 1068.59

## Input formats (auto-detected)
1. TSPLIB / CVRPLIB `.vrp` (NODE_COORD_SECTION, DEMAND_SECTION, CAPACITY).
2. Plain: first line `<num_nodes> <capacity>`, then `<id> <x> <y> <demand>` per node (depot first).

## CVRP design
- Chromosome: `IntegerChromosome` permutation of customers 1..n (giant tour).
- Decoding: optimal Split (DP) cuts the tour into routes, capacity respected.
- Feasibility: every customer exactly once + every route load <= capacity.
- Infeasible handling: `repair()` fixes the permutation; any remaining violation gets the GA penalty.
- Fitness: `-total_distance` (depot -> customers -> depot for each route).
- Operators: Tournament selection, Order Crossover, Inversion mutation, Elitism replacement.
- Toolbox core is untouched; CVRP only plugs in through `Problem`.

## Tests
    python -m tests.test_part4
