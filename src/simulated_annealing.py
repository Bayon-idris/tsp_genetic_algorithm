import random
import math
from utils import route_distance


def swap_two(route):
    """Helper: swap two cities to create a neighbor."""
    r = route.copy()
    i, j = random.sample(range(len(route)), 2)
    r[i], r[j] = r[j], r[i]
    return r


def simulated_annealing(route, cities, T=1000, alpha=0.995):
    """
    Applies SA to a route to locally optimize it.
    """
    current = route.copy()
    current_dist = route_distance(current, cities)

    while T > 1:
        candidate = swap_two(current)
        candidate_dist = route_distance(candidate, cities)

        delta = candidate_dist - current_dist

        if delta < 0 or random.random() < math.exp(-delta / T):
            current = candidate
            current_dist = candidate_dist

        T *= alpha

    return current
