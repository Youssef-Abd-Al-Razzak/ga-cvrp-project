from .base import Mutation


class BitFlipMutation(Mutation):
    """For BinaryChromosome."""

    def mutate(self, chromosome, rate):
        raise NotImplementedError
