from collections import deque
import re

def load_machines(file_path):
    machines = []
    try:
        with open(file_path, 'r') as file:
            for machine_data in file.read().split('\n\n'):
                raw_machine_data = list(map(int, re.findall(r'(\d+)', machine_data)))
                machine = {
                    'a': (raw_machine_data[0], raw_machine_data[1]),
                    'b': (raw_machine_data[2], raw_machine_data[3]),
                    'p': (raw_machine_data[4], raw_machine_data[5])
                }
                machines.append(machine)
        return machines

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print("Error: File contains non-numeric values or invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def button_press(machine, cost_a=3, cost_b=1):
    a,b,p = machine['a'], machine['b'], machine['p']
    a_presses = (b[0]*p[1] - b[1]*p[0])/(b[0]*a[1] - b[1]*a[0])
    b_presses = (a[0]*p[1] - a[1]*p[0])/(a[0]*b[1] - a[1]*b[0])


    if a_presses == int(a_presses) and b_presses == int(b_presses):
        return cost_a * int(a_presses) + cost_b * int(b_presses)
    else:
        return 0


def part_one(machines):
    return sum(button_press(machine) for machine in machines)


def part_two(machines):
    pass

if __name__ == "__main__":
    file_path = "example.txt"
    file_path = "input.txt"

    machines = load_machines(file_path)

    tokens = part_one(machines)
    print(f'You would have to spend {tokens} tokens to win all the prizes.')

    tokens = part_two(machines)
    print(f'You would have to spend {tokens} tokens to win all the prizes.')


