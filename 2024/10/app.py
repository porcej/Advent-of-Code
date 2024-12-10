from math import sqrt, floor

def load_map(file_path):
    grid = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                row = [int(ch) if ch.isdigit() else -1 for ch in line]
                grid.append(row)
        return grid

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print("Error: File contains non-numeric values or invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def find_by_symbols(grid, symbol):
    rows = len(grid)
    trailheads = [(rdx,cdx) for rdx in range(rows) for cdx in range(len(grid[rdx])) if grid[rdx][cdx] == symbol]
    return trailheads

def find_neighbors(grid, point):
    r,c = point
    neighbors = []
    rows = len(grid)
    for nr, nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
        if 0 <= nr < rows and 0 <= nc < len(grid[nr]):
            neighbors.append((nr, nc))
    return neighbors

def walk_trails(grid, point, peak=9, tracks=None):
            if tracks is not None:
                if point in tracks:
                    return 0
                tracks.add(point)
            r, c = point

            if grid[r][c] == peak:
                return 1
            result = 0
            for nr, nc in find_neighbors(grid, point):
                if grid[nr][nc] == grid[r][c] + 1:
                    result += walk_trails(grid, (nr, nc), peak, tracks)

            return result


def part_one(grid):
    trailheads = find_by_symbols(grid, symbol=0)
    trailends = find_by_symbols(grid, symbol=9)

    max_num_trails = len(trailheads) * len(trailends)
    
    num_trails = 0

    for trailhead in trailheads:
        tracks = set()
        num_trails += walk_trails(grid, point=trailhead, peak=9, tracks=tracks)

    return num_trails

def part_two(grid):
    trailheads = find_by_symbols(grid, symbol=0)
    trailends = find_by_symbols(grid, symbol=9)

    max_num_trails = len(trailheads) * len(trailends)
    
    num_trails = 0

    for trailhead in trailheads:
        tracks = set()
        num_trails += walk_trails(grid, point=trailhead, peak=9, tracks=None)

    return num_trails


if __name__ == "__main__":
    file_path = "example.txt"
    file_path = "example2.txt"
    file_path = "input.txt"

    map_grid = load_map(file_path)
    score_sum = part_one(map_grid)
    print(f'The the trailhead score sum is {score_sum}.')
    score_sum = part_two(map_grid)
    print(f'The the trailhead rating sum is now {score_sum}.')

