"""CVRP built on top of the GA toolbox. Solution = permutation of customers 1..n.

Representation : IntegerChromosome (permutation of customers 1..n, a "giant tour").
Decoding       : optimal Split (dynamic programming). The giant tour is cut into
                 consecutive routes so that total distance is minimal and no
                 route exceeds the vehicle capacity.
Constraints    : is_feasible() checks that (a) every customer appears exactly once
                 and (b) every route load <= capacity.
Infeasibility  : repair() rebuilds a valid permutation (drop duplicates / foreign
                 genes, append missing customers). Anything still infeasible
                 (e.g. one customer demand > capacity) gets the GA penalty.
"""
import math

from ga_toolbox.chromosomes.integer import IntegerChromosome
from ga_toolbox.problem import Problem
from .instance import CVRPInstance


class CVRPProblem(Problem):
    def __init__(self, instance: CVRPInstance):
        self.instance = instance
        n = len(instance.coords)
        self._dist = [[math.dist(instance.coords[i], instance.coords[j])
                       for j in range(n)] for i in range(n)]
        self._cache = {}

    def create_chromosome(self):
        """IntegerChromosome (permutation) of customers 1..n."""
        n = self.instance.num_customers
        return IntegerChromosome.random(n, 1, n, permutation=True)

    # ------------------------------------------------------------ decoding
    def decode(self, chromosome) -> list:
        """Split the permutation into routes. Return list of routes (each a list of customers)."""
        key = tuple(chromosome.genes)
        cached = self._cache.get(key)
        if cached is None:
            if len(self._cache) > 200000:
                self._cache.clear()
            cached = self._split(list(key))
            self._cache[key] = cached
        return [list(r) for r in cached]

    def _split(self, tour: list) -> list:
        """Optimal split of the giant tour under the capacity limit (Prins' Split)."""
        demands, cap, d = self.instance.demands, self.instance.capacity, self._dist
        n = len(tour)
        INF = float("inf")
        best = [INF] * (n + 1)   # best[j] = min cost to serve first j customers
        pred = [0] * (n + 1)
        best[0] = 0.0
        for i in range(n):
            if best[i] == INF:
                continue
            load, cost = 0, 0.0
            for j in range(i, n):
                c = tour[j]
                load += demands[c]
                # a single customer above capacity still gets its own route
                # (is_feasible reports it); otherwise stop growing the route.
                if load > cap and j > i:
                    break
                cost = (d[0][c] if j == i else cost - d[tour[j - 1]][0] + d[tour[j - 1]][c])
                total = best[i] + cost + d[c][0]
                if total < best[j + 1]:
                    best[j + 1] = total
                    pred[j + 1] = i
        routes, j = [], n
        while j > 0:
            i = pred[j]
            routes.append(tour[i:j])
            j = i
        routes.reverse()
        return routes

    # ------------------------------------------------------------ distance
    def distance(self, i: int, j: int) -> float:
        return self._dist[i][j]

    def route_distance(self, route: list) -> float:
        """Depot -> customers in order -> depot."""
        if not route:
            return 0.0
        total = self._dist[0][route[0]] + self._dist[route[-1]][0]
        for a, b in zip(route, route[1:]):
            total += self._dist[a][b]
        return total

    def total_distance(self, routes: list) -> float:
        return sum(self.route_distance(r) for r in routes)

    # ------------------------------------------------------------ feasibility
    def route_load(self, route: list) -> int:
        return sum(self.instance.demands[c] for c in route)

    def is_feasible(self, chromosome) -> bool:
        n = self.instance.num_customers
        if sorted(chromosome.genes) != list(range(1, n + 1)):
            return False   # missing / duplicated / unknown customer
        cap = self.instance.capacity
        return all(self.route_load(r) <= cap for r in self.decode(chromosome))

    def repair(self, chromosome):
        """Rebuild a valid permutation: keep first occurrence of each valid customer,
        append the missing ones. Capacity is handled by the Split decoder."""
        n = self.instance.num_customers
        seen, genes = set(), []
        for g in chromosome.genes:
            if 1 <= g <= n and g not in seen:
                seen.add(g)
                genes.append(g)
        genes.extend(c for c in range(1, n + 1) if c not in seen)
        fixed = type(chromosome)(genes)
        return fixed

    def evaluate(self, chromosome) -> float:
        """Return -total_distance."""
        return -self.total_distance(self.decode(chromosome))
