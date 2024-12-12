from math import sqrt, floor

def load_map(file_path):
    grid = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                row = line.strip().split()
                grid.append(row)
        return grid

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print("Error: File contains non-numeric values or invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")




def part_one(map):
    pass


def part_two(map):
    pass

if __name__ == "__main__":
    file_path = "example.txt"
    # file_path = "example2.txt"
    # file_path = "input.txt"

    map_grid = load_map(file_path)
    for row in map_grid:
        print("".join(row))


    cost = part_one(map_grid)
    print(f'The cost for the fencse is {cost}.')

    cost = part_two(map_grid)
    print(f'The cost for the fense is {cost}.')


