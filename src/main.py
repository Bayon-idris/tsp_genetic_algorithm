from utils import load_cities, plot_route, plot_convergence, route_distance
from tsp_ga import genetic_algorithm


def main():
    cities = load_cities("data/cities.csv")

    best_route, history = genetic_algorithm(
        cities,
        pop_size=120,
        generations=600,
        mutation_rate=0.15,
        use_erx=False,
        use_sa=True
    )

    print("Best distance:", route_distance(best_route, cities))
    print("Best route:", best_route)

    plot_route(best_route, cities)
    plot_convergence(history)


if __name__ == "__main__":
    main()
  