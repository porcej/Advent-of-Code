from math import sqrt, floor

def load_stones(file_path):
    try:
        with open(file_path, 'r') as file:
            line = file.read().strip()
            stones = [int(ch) if ch.isdigit() else -1 for ch in line.split(" ")]
        return stones

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print("Error: File contains non-numeric values or invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def blink(stones):
    new_stones = []
    for sdx, stone in enumerate(stones):
        # Rules
        pass

    return new_stones


def part_one(stones, blinks=25):
    for bdx in range(blinks):
        stones = blink(stones)

    
    return len(stones)



def part_two(stones):
    pass


if __name__ == "__main__":
    file_path = "example.txt"
    file_path = "example2.txt"
    file_path = "input.txt"

    stones = load_stones(file_path)
    num_stones = part_one(stones)
    print(f'After blinking 25 times there are {num_stones}.')
    num_stones = part_two(stones)
    print(f'After blinking 25 times there are {num_stones}.')

