from .base import Mutation


class InversionMutation(Mutation):
    """Reverse a random segment. For permutation chromosomes."""

    def mutate(self, chromosome, rate):
        raise NotImplementedError
