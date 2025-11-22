import csv
import math
import matplotlib.pyplot as plt


def load_cities(path="data/cities.csv"):
    """
    Load city coordinates.
    CSV format expected: id, x, y
    """
    cities = []
    with open(path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header

        for row in reader:
            city_id = int(row[0])
            x = float(row[1])
            y = float(row[2])
            cities.append((city_id, x, y))

    return cities


def euclidean_distance(a, b):
    """
    Computes Euclidean distance between two cities (x1,y1) and (x2,y2)
    """
    return math.sqrt((a[1] - b[1])**2 + (a[2] - b[2])**2)


def route_distance(route, cities):
    """
    Computes the total distance of a TSP route:
    route = list of city indices (permutation)
    """
    total = 0
    for i in range(len(route)):
        city1 = cities[route[i] - 1]
        city2 = cities[route[(i + 1) % len(route)] - 1]
        total += euclidean_distance(city1, city2)
    return total


def plot_route(route, cities, save_path="results/best_route.png"):
    """
    Plot the best route on a 2D map.
    """
    xs = [cities[city - 1][1] for city in route] + [cities[route[0] - 1][1]]
    ys = [cities[city - 1][2] for city in route] + [cities[route[0] - 1][2]]

    plt.figure(figsize=(8, 6))
    plt.plot(xs, ys, marker='o')
    plt.title("Best TSP Route")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.savefig(save_path)
    plt.close()


def plot_convergence(history, save_path="results/convergence.png"):
    """
    Plot GA convergence curve (best distance per generation).
    """
    plt.figure(figsize=(8, 6))
    plt.plot(history)
    plt.title("GA Convergence Curve")
    plt.xlabel("Generation")
    plt.ylabel("Best Distance")
    plt.savefig(save_path)
    plt.close()
