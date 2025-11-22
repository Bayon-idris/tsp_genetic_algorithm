import random
from utils import route_distance


def tournament_selection(population, cities, k=3):
    """
    Tournament selection:
    - Randomly pick k individuals
    - Return the best among them
    """
    selected = random.sample(population, k)
    selected.sort(key=lambda chromo: route_distance(chromo, cities))
    return selected[0]  # best individual


def roulette_selection(population, cities):
    """
    Roulette-Wheel Selection (fitness proportional).
    We use 1/distance as fitness.
    """
    fitness_values = []
    
    for chromo in population:
        dist = route_distance(chromo, cities)
        fitness_values.append(1 / dist)

    total_fitness = sum(fitness_values)
    probabilities = [f / total_fitness for f in fitness_values]

    # choose index based on probabilities
    r = random.random()
    cumulative = 0

    for idx, p in enumerate(probabilities):
        cumulative += p
        if r <= cumulative:
            return population[idx]
