import random


def segment_shuffle_mutation(chromosome, mutation_rate=0.1):
    """
    Mutation: select a segment and shuffle inside.
    """
    if random.random() > mutation_rate:
        return chromosome

    size = len(chromosome)
    i, j = sorted(random.sample(range(size), 2))

    segment = chromosome[i:j]
    random.shuffle(segment)

    new_chromosome = chromosome.copy()
    new_chromosome[i:j] = segment

    return new_chromosome
