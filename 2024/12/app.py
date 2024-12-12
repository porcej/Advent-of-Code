from collections import deque

def load_map(file_path):
    grid = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                row = line.strip()
                grid.append(list(row))
        return grid

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print("Error: File contains non-numeric values or invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def find_neighbors(grid, point):
    r,c = point
    neighbors = []
    rows = len(grid)
    for nr, nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
        if 0 <= nr < rows and 0 <= nc < len(grid[nr]):
            neighbors.append((nr, nc))
    return neighbors


def part_one(garden_map):
    # plant_plots = get_plots_by_plant(map_grid)
    visted_plots = set()
    cost = 0
    for rdx in range(len(garden_map)):
        for cdx in range(len(garden_map[rdx])):
            if (rdx, cdx) in visted_plots:
                continue
            queue = deque([(rdx, cdx)])
            area = 0
            perimeter = 0
            while queue:
                r, c = queue.popleft()
                if (r, c) in visted_plots:
                    continue
                visted_plots.add((r,c))
                area += 1

                neighbors = find_neighbors(garden_map, (r, c))
                for neighbor in neighbors:
                    nr, nc = neighbor
                    if garden_map[r][c] == garden_map[nr][nc]:
                        queue.append(neighbor)
                    else:
                        perimeter += 1
                perimeter += 4 - len(neighbors)

            cost += area * perimeter
    return cost





def part_two(map_grid):
    pass

if __name__ == "__main__":
    # file_path = "example.txt"
    # file_path = "example2.txt"
    file_path = "input.txt"

    map_grid = load_map(file_path)
    for row in map_grid:
        print("".join(row))


    cost = part_one(map_grid)
    print(f'The cost for the fencse is {cost}.')

    cost = part_two(map_grid)
    print(f'The cost for the fense is {cost}.')


