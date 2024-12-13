from collections import deque
import re

def load_machines(file_path):
    machines = []
    try:
        with open(file_path, 'r') as file:
            for machine_data in file.read().split('\n\n'):
                raw_machine_data = list(map(int, re.findall(r'(\d+)', machine_data)))
                machine = {
                    'button_a': {'x': raw_machine_data[0], 'y':raw_machine_data[1]},
                    'button_b': {'x': raw_machine_data[2], 'y':raw_machine_data[3]},
                    'prize': {'x': raw_machine_data[4], 'y':raw_machine_data[5]}
                }
                machines.append(machine)
        return machines

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print("Error: File contains non-numeric values or invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def part_one(machines):
    pass


def part_two(machines):
    pass

if __name__ == "__main__":
    file_path = "example.txt"
    # file_path = "input.txt"

    machines = load_machines(file_path)

    tokens = part_one(machines)
    print(f'You would have to spend {tokens} tokens to win all the prizes.')

    tokens = part_two(machines)
    print(f'You would have to spend {tokens} tokens to win all the prizes.')


