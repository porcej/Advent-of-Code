from math import sqrt, floor

def load_map(file_path):
    grid = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    grid.append(list(line))
        return grid

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print("Error: File contains non-numeric values or invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def find_antennas(map_grid):
    antennas = {}
    for rdx, map_row in enumerate(map_grid):
        for cdx, point in enumerate(map_row):
            if point.isalnum():
                if point in antennas:
                    antennas[point].append((rdx,cdx))
                else:
                    antennas[point] = [(rdx,cdx)]
    return antennas

def find_slope_and_intercept(point1, point2):
    """
    Given two points as tuples (x1, y1) and (x2, y2),
    calculate the slope and y-intercept of the line connecting them.
    """
    x1, y1 = point1
    x2, y2 = point2

    # Check for vertical line
    if x1 == x2:
        return None, None  # Undefined slope, no y-intercept

    # Calculate slope
    slope = (y2 - y1) / (x2 - x1)

    # Calculate y-intercept
    intercept = y1 - slope * x1

    return slope, intercept

def part_one(map_grid):
    antinodes = set()
    antennas = find_antennas(map_grid)
    max_rows = len(map_grid[0])
    max_cols = len(map_grid)

    for freq, points in antennas.items():
        while len(points) > 0:
            first_ant = points.pop(0)
            for second_ant in points:
                delta = tuple(x - y for x, y in zip(first_ant, second_ant))
                
                # Minus Side (subtract delta from first point)
                antinode = tuple(x + y for x, y in zip(first_ant, delta))
                if (0 <= antinode[0] < max_cols) and (0 <= antinode[1] < max_rows):
                    antinodes.add(antinode)
                
                # Plus Size (add delta to second point)
                antinode = tuple(x - y for x, y in zip(second_ant, delta))
                if (0 <= antinode[0] < max_cols) and (0 <= antinode[1] < max_rows):
                    antinodes.add(antinode)

    return antinodes

def get_antinodes(ant1, ant2, num_rows, num_cols):
    delta = tuple(x - y for x, y in zip(ant2, ant1))
    antinodes = set()
    next_step = ant1

    while next_step[0] in range(num_rows) and next_step[1] in range(num_cols):
        antinodes.add(next_step)
        next_step = tuple(x + y for x, y in zip(next_step, delta))

    next_step = ant1
    while next_step[0] in range(num_rows) and next_step[1] in range(num_cols):
        antinodes.add(next_step)
        next_step = tuple(x - y for x, y in zip(next_step, delta))
    return antinodes

def part_two(map_grid):
    antinodes = set()
    antennas = find_antennas(map_grid)
    max_rows = len(map_grid[0])
    max_cols = len(map_grid)

    for freq, points in antennas.items():
        # for first_ant in points:
        while len(points) > 0:
            first_ant = points.pop(0)
            for second_ant in points:
                antinodes |= get_antinodes(first_ant, second_ant, max_rows, max_cols)
    return antinodes



if __name__ == "__main__":
    file_path = "example.txt"
    file_path = "input.txt"

    map_grid = load_map(file_path)
    antinodes = part_one(map_grid)
    print(f'There are {len(antinodes)} antinodes if the distance is doubled.')
    antinodes = part_two(map_grid)
    print(f'There are {len(antinodes)} antinodes if the distance is unbounded.')
    for antinode in antinodes:
        c, r = antinode
        if not map_grid[c][r].isalnum():
            map_grid[c][r] = '#'

    for row in map_grid:
        print(f'\t{"".join(row)}')




