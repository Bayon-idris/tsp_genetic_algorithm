import random
from utils import route_distance


def create_chromosome(num_cities):
    """
    Creates a random permutation of cities.
    """
    chromosome = list(range(1, num_cities + 1))
    random.shuffle(chromosome)
    return chromosome


def initialize_population(pop_size, num_cities):
    """
    Creates an initial population of random chromosomes.
    """
    population = [create_chromosome(num_cities) for _ in range(pop_size)]
    return population
