"""Entry point: python -m cvrp.main <instance_file>"""
import argparse

from ga_toolbox.config import GAConfig
from ga_toolbox.crossover.order import OrderCrossover
from ga_toolbox.genetic_algorithm import GeneticAlgorithm
from ga_toolbox.mutation.inversion import InversionMutation
from ga_toolbox.replacement.elitism import ElitismReplacement
from ga_toolbox.selection.tournament import TournamentSelection

from .cvrp_problem import CVRPProblem
from .instance import load_instance
from .output import print_solution


def main(argv=None):
    parser = argparse.ArgumentParser(description="Solve CVRP with the GA toolbox")
    parser.add_argument("instance", help="path to the CVRP instance file")
    parser.add_argument("--pop", type=int, default=300, help="population size")
    parser.add_argument("--gens", type=int, default=1000, help="number of generations")
    parser.add_argument("--cx", type=float, default=0.9, help="crossover rate")
    parser.add_argument("--mut", type=float, default=0.2, help="mutation rate")
    parser.add_argument("--elite", type=int, default=5, help="elite size")
    parser.add_argument("--seed", type=int, default=None, help="random seed")
    parser.add_argument("--verbose", action="store_true", help="print every generation")
    args = parser.parse_args(argv)

    problem = CVRPProblem(load_instance(args.instance))
    config = GAConfig(pop_size=args.pop, generations=args.gens,
                      crossover_rate=args.cx, mutation_rate=args.mut,
                      seed=args.seed, verbose=args.verbose)
    ga = GeneticAlgorithm(
        problem=problem,
        selection=TournamentSelection(tournament_size=3),
        crossover=OrderCrossover(),
        mutation=InversionMutation(),
        replacement=ElitismReplacement(elite_size=args.elite),
        config=config,
    )
    best = ga.run()
    print_solution(problem, best)


if __name__ == "__main__":
    main()
