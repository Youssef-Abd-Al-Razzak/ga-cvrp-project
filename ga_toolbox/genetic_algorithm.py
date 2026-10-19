"""GA engine. It knows nothing about the specific problem."""
import random

from ga_toolbox.chromosomes.base import Chromosome
from .config import GAConfig

class GeneticAlgorithm:
    def __init__(self, problem, selection, crossover, mutation, replacement,
                 config: GAConfig = None):
        self.problem = problem
        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation
        self.replacement = replacement
        self.config = config or GAConfig()
        if self.config.seed is not None:
            random.seed(self.config.seed)
        self.best = None

    def _evaluate(self, chromosome):
        chromosome.feasible = self.problem.is_feasible(chromosome)
        
        if not chromosome.feasible:
            repaired = self.problem.repair(chromosome)
            if repaired is None:
                raise ValueError("Problem.repair must return a chromosome")
            chromosome = repaired
            chromosome.feasible = self.problem.is_feasible(chromosome)

        chromosome.fitness = self.problem.evaluate(chromosome)
        if not chromosome.feasible:
            chromosome.fitness -= self.config.penalty_factor
        return chromosome

    def _evaluate_population(self, population):
        return [self._evaluate(chromosome) for chromosome in population]

    def run(self):
        population = [self.problem.create_chromosome()
                      for _ in range(self.config.pop_size)]
        population = self._evaluate_population(population)
        self.best = max(population,key=Chromosome.get_fitness).copy()

        for generation in range(self.config.generations):
            selected = self.selection.select(population, self.config.pop_size)
            offspring = []

            for index in range(0, self.config.pop_size, 2):
                parent1 = selected[index]
                parent2 = selected[(index + 1) % self.config.pop_size]
                
                if random.random() < self.config.crossover_rate:
                    child1, child2 = self.crossover.crossover(parent1, parent2)
                else:
                    child1, child2 = parent1.copy(), parent2.copy()
                offspring.extend((
                    self.mutation.mutate(child1, self.config.mutation_rate),
                    self.mutation.mutate(child2, self.config.mutation_rate),
                ))

            evaluated_offspring = self._evaluate_population(offspring[:self.config.pop_size])
            population = self.replacement.replace(population, evaluated_offspring)
            current_best = max(population, key=Chromosome.get_fitness)

            if current_best.fitness > self.best.fitness:
                self.best = current_best.copy()

            if self.config.verbose:
                print(f"Generation {generation + 1}/{self.config.generations}: "
                      f"best fitness = {self.best.fitness}")
                
        return self.best