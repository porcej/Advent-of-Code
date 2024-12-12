from math import sqrt, floor

def load_stones(file_path):
    try:
        with open(file_path, 'r') as file:
            line = file.read().strip()
            stones = [int(ch) if ch.isdigit() else -1 for ch in line.split(" ")]
            # stones = map(int, line.split(' '))
        return stones

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print("Error: File contains non-numeric values or invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


seen = {}
def blink(stone, blinks, scale=2024):
    if (stone, blinks) in seen:
        return seen[(stone, blinks)]
    new_stones = []
    if blinks == 0:
        ret = 1
    elif stone == 0:
        ret = blink(1, blinks-1)
    elif len(str(stone))  % 2 == 0:
        stone_str = str(stone)
        midpoint = len(stone_str) // 2
        left, right = int(stone_str[:midpoint]), int(stone_str[midpoint:])
        ret = blink(left, blinks-1) + blink(right, blinks-1)
    else:
        ret = blink(stone*scale, blinks-1)
    seen[(stone,blinks)] = ret
    return ret


def part_one(stones, blinks=25):
    return sum(blink(stone, blinks) for stone in stones)


def part_two(stones, blinks=75):
    return sum(blink(stone, blinks) for stone in stones)

if __name__ == "__main__":
    # file_path = "example.txt"
    file_path = "example2.txt"
    file_path = "input.txt"

    stones = load_stones(file_path)
    num_stones = part_one(stones)
    print(f'After blinking 25 times there are {num_stones}.')
    print(stones)

    num_stones = part_two(stones)
    print(f'After blinking 75 times there are {num_stones}.')


