from .base import Mutation


class SwapMutation(Mutation):
    """Swap two genes. For permutation chromosomes."""

    def mutate(self, chromosome, rate):
        raise NotImplementedError
