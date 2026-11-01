import numpy as np

# Sample distance matrix for 4 cities
distance_matrix = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])

def calculate_tour_distance(tour, matrix):
    """Calculates total distance of a tour, including return to start."""
    distance = sum(matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))
    distance += matrix[tour[-1], tour[0]]
    return distance

def get_2opt_neighbor(tour, i, j):
    """Reverses the segment between index i and j to eliminate edge-crossings."""
    new_tour = tour.copy()
    new_tour[i:j+1] = reversed(tour[i:j+1])
    return new_tour

def hill_climbing_tsp(matrix):
    num_cities = len(matrix)
    # Step 1: Initialize random tour
    current_tour = list(range(num_cities))
    np.random.shuffle(current_tour)
    current_distance = calculate_tour_distance(current_tour, matrix)

    improved = True
    while improved:
        improved = False
        # Evaluate all 2-opt neighbors
        for i in range(1, num_cities - 1):
            for j in range(i + 1, num_cities):
                neighbor = get_2opt_neighbor(current_tour, i, j)
                neighbor_distance = calculate_tour_distance(neighbor, matrix)

                # Step 2 & 3: Compare and Move
                if neighbor_distance < current_distance:
                    current_tour = neighbor
                    current_distance = neighbor_distance
                    improved = True
                    break  # First-choice improvement
        if improved:
            break

    return current_tour, current_distance

# Execute optimization
best_tour, best_distance = hill_climbing_tsp(distance_matrix)
print(f"Optimized Tour: {best_tour} | Total Distance: {best_distance}")