import random


# ----------------------------------------------------
#                PMX CROSSOVER
# ----------------------------------------------------
def pmx_crossover(parent1, parent2):
    size = len(parent1)

    # Choose two cut positions
    cx1, cx2 = sorted(random.sample(range(size), 2))

    child = [None] * size

    # Copy the slice from parent1
    child[cx1:cx2] = parent1[cx1:cx2]

    # Process parent2 values
    for i in range(cx1, cx2):
        if parent2[i] not in child:
            value = parent2[i]
            idx = i

            while True:
                mapped = parent1[idx]
                idx = parent2.index(mapped)

                if child[idx] is None:
                    child[idx] = value
                    break

    # Fill remaining missing positions
    for i in range(size):
        if child[i] is None:
            child[i] = parent2[i]

    return child


# ----------------------------------------------------
#            EDGE RECOMBINATION CROSSOVER (ERX)
# ----------------------------------------------------
def build_edge_map(parent1, parent2):
    edge_map = {city: set() for city in parent1}

    parents = [parent1, parent2]

    for p in parents:
        for i in range(len(p)):
            current = p[i]
            left = p[i - 1]
            right = p[(i + 1) % len(p)]
            edge_map[current].add(left)
            edge_map[current].add(right)

    return edge_map


def erx_crossover(parent1, parent2):
    edge_map = build_edge_map(parent1, parent2)

    current = random.choice(parent1)
    child = [current]

    for _ in range(len(parent1) - 1):
        for k in edge_map:
            edge_map[k].discard(current)

        # choose next city
        if len(edge_map[current]) > 0:
            next_city = min(edge_map[current], key=lambda c: len(edge_map[c]))
        else:
            unused = [c for c in parent1 if c not in child]
            next_city = random.choice(unused)

        child.append(next_city)
        current = next_city

    return child
