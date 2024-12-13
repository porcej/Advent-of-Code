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

def find_neighbors(grid, point, directions=[(-1,0), (0,1), (1,0), (0,-1)]):
    r,c = point
    neighbors = []
    rows = len(grid)
    for dr, dc in directions:
        # print(f'(r, c)=({r}, {c}), (dr,dc)=({dr}, {dc})')
        nr, nc = dr + r, dc + c
        if 0 <= nr < rows and 0 <= nc < len(grid[nr]):
            neighbors.append(((nr, nc), (dr, dc)))
    return neighbors


def part_one(garden_map):
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
                    (nr, nc), (dr, dc)  = neighbor
                    if garden_map[r][c] == garden_map[nr][nc]:
                        queue.append((nr, nc))
                    else:
                        perimeter += 1
                perimeter += 4 - len(neighbors)

            cost += area * perimeter
    return cost


def part_two(garden_map):
    visted_plots = set()
    directions = [(-1,0), (0,1), (1,0), (0,-1)] # [(-1,0),(1,0),(0,-1),(0,1)]
    cost = 0
    for rdx in range(len(garden_map)):
        for cdx in range(len(garden_map[rdx])):
            if (rdx, cdx) in visted_plots:
                continue
            queue = deque([(rdx, cdx)])
            area = 0
            perimeter = 0
            border_plots = dict()
            while queue:
                r, c = queue.popleft()
                if (r, c) in visted_plots:
                    continue
                visted_plots.add((r,c))
                area += 1

                # neighbors = find_neighbors(garden_map, (r, c))
                for dr, dc in directions:
                # for neighbor in neighbors:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<len(garden_map) and 0<=nc<len(garden_map[rdx]) and garden_map[r][c] == garden_map[nr][nc]:
                        queue.append((nr,nc))
                    else:
                        perimeter += 1
                        if (dr,dc) not in border_plots:
                            border_plots[(dr,dc)] = set()
                        border_plots[(dr,dc)].add((r,c))

            sides = 0
            for key, values in border_plots.items():
                seen_sides = set()
                old_sides = sides
                for (prdx,pcdx) in values:
                    if (prdx, pcdx) not in seen_sides:
                        sides += 1
                        queue = deque([(prdx, pcdx)])
                        while queue:
                            nr, nc = queue.popleft()
                            if (nr, nc) in seen_sides:
                                continue
                            seen_sides.add((nr, nc))
                            for dr, dc in directions:
                                rr, cc = nr + dr, nc + dc
                                if (rr, cc) in values:
                                    queue.append((rr,cc))
            cost += area * sides
    return cost

if __name__ == "__main__":
    file_path = "example.txt"
    # file_path = "example2.txt"
    # file_path = "example3.txt"
    file_path = "input.txt"

    map_grid = load_map(file_path)

    cost = part_one(map_grid)
    print(f'The cost for the fence is {cost} using perimeter.')

    cost = part_two(map_grid)
    print(f'The cost for the fence is {cost} using number of sides.')


