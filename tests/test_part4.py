"""Self-check for Part 4 (mutation & replacement). Run: python -m tests.test_part4"""
from ga_toolbox.chromosomes.binary import BinaryChromosome
from ga_toolbox.chromosomes.floating import FloatChromosome
from ga_toolbox.chromosomes.integer import IntegerChromosome
from ga_toolbox.mutation.bitflip import BitFlipMutation
from ga_toolbox.mutation.gaussian import GaussianMutation
from ga_toolbox.mutation.inversion import InversionMutation
from ga_toolbox.mutation.swap import SwapMutation
from ga_toolbox.replacement.elitism import ElitismReplacement
from ga_toolbox.replacement.generational import GenerationalReplacement


def demo():
    b = BinaryChromosome([0, 1, 0, 1])
    assert BitFlipMutation().mutate(b, 1.0).genes == [1, 0, 1, 0]
    assert BitFlipMutation().mutate(b, 0.0).genes == b.genes
    assert b.genes == [0, 1, 0, 1]  # parent untouched

    f = FloatChromosome.random(50)
    m = GaussianMutation(sigma=5.0).mutate(f, 1.0)
    assert all(0.0 <= g <= 1.0 for g in m.genes) and m.genes != f.genes

    p = IntegerChromosome.random(10, 1, 10, permutation=True)
    for op in (SwapMutation(), InversionMutation()):
        for _ in range(100):
            c = op.mutate(p, 1.0)
            assert sorted(c.genes) == list(range(1, 11)) and c.genes != p.genes
    assert sorted(p.genes) == list(range(1, 11))

    def pop(fits):
        out = []
        for x in fits:
            c = BinaryChromosome([0])
            c.fitness = x
            out.append(c)
        return out

    parents, kids = pop([10, 5, 1]), pop([3, 2, 4])
    assert GenerationalReplacement().replace(parents, kids) == kids
    new = ElitismReplacement(elite_size=1).replace(parents, kids)
    assert [c.fitness for c in new] == [10, 4, 3]
    print("Part 4 OK")


if __name__ == "__main__":
    demo()
