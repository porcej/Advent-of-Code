from collections import deque
import re

def load_robots(file_path):
    robots = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(f'Line: {line}')
                raw_robot_data = list(map(int, re.findall(r'([-\d]+)', line)))
                robot = {
                    'p': [raw_robot_data[0], raw_robot_data[1]],
                    'v': [raw_robot_data[2], raw_robot_data[3]],
                }
                robots.append(robot)
        return robots

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print("Error: File contains non-numeric values or invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def part_one(robots, run_time, max_x, max_y):
    quadrants = [0 for i in range(4)]
    for robot in robots:
        x = (robot['p'][0] + run_time * robot['v'][0]) % max_x
        y = (robot['p'][1] + run_time * robot['v'][1]) % max_y
        print(f'X,Y >= {x}, {y}')
        mid_x, mid_y = max_x // 2, max_y // 2
        if x < mid_x and y < mid_y:
            quadrants[0] += 1
        elif x >mid_x and y < mid_y:
            quadrants[1] += 1
        elif x < mid_x and y > mid_y:
            quadrants[2] += 1
        elif x > mid_x and y > mid_y:
            quadrants[3] += 1
    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def part_two(robots, max_x, max_y):
    for time_step in range(17047):
        for rdx in range(max_y):
            row = sorted({robot['p'][0] for robot in robots if robot['p'][1] == rdx})
            n = 0
            for cdx in range(len(row) -1):
                n = n + 1 if row[cdx + 1] == row[cdx] + 1 else 0
                if n > 10:
                    return time_step
            print(f'n: {n} - {row}')
        for robot in robots: 
            robot['p'][0] = (robot['p'][0] + robot['v'][0])% max_x
            robot['p'][1] = (robot['p'][1] + robot['v'][1]) % max_y
    pass

if __name__ == "__main__":
    # file_path = "example.txt"
    file_path = "input.txt"

    robots = load_robots(file_path)

    run_time = 100 
    safety_factor = part_one(robots, run_time, 101, 103)
    print(f'The safety factor after {run_time} seconds will be {safety_factor}.')

    christmas_tree_time = part_two(robots, 101, 103)
    print(f'The time to the christmas tree easter egg is {christmas_tree_time}.')



