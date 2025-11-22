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


from selection import tournament_selection
from crossover import pmx_crossover, erx_crossover
from mutation import segment_shuffle_mutation
from simulated_annealing import simulated_annealing


def genetic_algorithm(
        cities,
        pop_size=100,
        generations=500,
        mutation_rate=0.1,
        use_erx=False,
        use_sa=False):

    num_cities = len(cities)
    population = initialize_population(pop_size, num_cities)

    best_history = []
    best_route = min(population, key=lambda c: route_distance(c, cities))

    for gen in range(generations):

        new_population = []

        # elitism
        new_population.append(best_route)

        for _ in range(pop_size - 1):

            # 1. Selection
            p1 = tournament_selection(population, cities)
            p2 = tournament_selection(population, cities)

            # 2. Crossover
            child = erx_crossover(p1, p2) if use_erx else pmx_crossover(p1, p2)

            # 3. Mutation
            child = segment_shuffle_mutation(child, mutation_rate)

            # 4. Simulated annealing (optional)
            if use_sa:
                child = simulated_annealing(child, cities)

            new_population.append(child)

        # update population
        population = new_population

        # track best
        current_best = min(population, key=lambda c: route_distance(c, cities))
        best_distance = route_distance(current_best, cities)

        if route_distance(best_route, cities) > best_distance:
            best_route = current_best

        best_history.append(best_distance)

        if gen % 50 == 0:
            print(f"Generation {gen}, best distance = {best_distance}")

    return best_route, best_history
