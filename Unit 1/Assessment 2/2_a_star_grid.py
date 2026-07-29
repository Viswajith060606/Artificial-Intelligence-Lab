import heapq

# 5x5 Grid representation: 0 = Free cell, 1 = Obstacle
# Grid dimensions
ROWS, COLS = 5, 5

# Start and Goal positions
START = (0, 0)
GOAL = (4, 4)

# Obstacle coordinates
OBSTACLES = {(1, 1), (1, 2), (2, 1), (3, 3)}

# Movement directions: Up, Down, Left, Right
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def manhattan_distance(p1, p2):
    """Calculates Manhattan Distance heuristic h(n)."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def a_star_search(start, goal):
    """Executes A* search algorithm and prints priority queue updates."""
    # Priority Queue stores tuples: (f_score, counter, current_node)
    # Counter handles tie-breaking in priority queue
    counter = 0
    pq = []

    g_score = {start: 0}
    f_score = {start: manhattan_distance(start, goal)}

    heapq.heappush(pq, (f_score[start], counter, start))

    parent = {}
    visited = set()

    step = 0
    print("=" * 65)
    print("                 A* SEARCH STEP-BY-STEP TRACE                 ")
    print("=" * 65)

    while pq:
        current_f, _, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)
        step += 1

        print(f"\nStep {step}:")
        print(f"  Popped Node: {current} | g = {g_score[current]}, h = {manhattan_distance(current, goal)}, f = {current_f}")

        # Check for Goal
        if current == goal:
            print("\n>>> GOAL REACHED! <<<")
            break

        # Explore neighbors
        for dr, dc in DIRECTIONS:
            neighbor = (current[0] + dr, current[1] + dc)
            r, c = neighbor

            # Check grid bounds and obstacles
            if 0 <= r < ROWS and 0 <= c < COLS and neighbor not in OBSTACLES:
                tentative_g = g_score[current] + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    parent[neighbor] = current
                    g_score[neighbor] = tentative_g
                    h = manhattan_distance(neighbor, goal)
                    f = tentative_g + h
                    f_score[neighbor] = f

                    counter += 1
                    heapq.heappush(pq, (f, counter, neighbor))
                    print(f"    Expanded Neighbor {neighbor}: g={tentative_g}, h={h}, f={f}")

    # Reconstruct optimal path
    path = []
    curr = goal
    while curr in parent:
        path.append(curr)
        curr = parent[curr]
    path.append(start)
    path.reverse()

    return path, g_score[goal]


def print_grid_visualization(path):
    """Displays visual grid in terminal."""
    print("\n" + "=" * 35)
    print("       GRID VISUALIZATION        ")
    print("=" * 35)
    path_set = set(path)
    for r in range(ROWS):
        row_str = ""
        for c in range(COLS):
            pos = (r, c)
            if pos == START:
                row_str += " S "
            elif pos == GOAL:
                row_str += " G "
            elif pos in OBSTACLES:
                row_str += " X "
            elif pos in path_set:
                row_str += " * "
            else:
                row_str += " . "
        print(row_str)
    print("=" * 35)
    print(" Legend: S=Start, G=Goal, X=Obstacle, *=Path, .=Empty\n")


if __name__ == "__main__":
    optimal_path, path_cost = a_star_search(START, GOAL)

    print("\n" + "=" * 65)
    print(f"Optimal Path: {optimal_path}")
    print(f"Total Path Cost: {path_cost}")
    print("=" * 65)

    print_grid_visualization(optimal_path)