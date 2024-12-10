from math import sqrt, floor

def load_disk_map(file_path):
    try:
        with open(file_path, 'r') as file:
            disk_map = file.read().strip()
        return disk_map

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print("Error: File contains non-numeric values or invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def part_one(disk_map):
    lengths = [int(c) for c in disk_map]
    blocks = []
    file_id = 0
    # True if we are expecting a file-length next, False if expecting free-length next
    expect_file = True

    for length in lengths:
        if length == 0:
            # Zero-length segment means nothing added, just switch context
            if expect_file:
                file_id += 1
            # If it's free and length=0, it's just no free blocks added.
            expect_file = not expect_file
            continue

        if expect_file:
            # Add 'length' file blocks with current file_id
            blocks.extend(str(file_id) for _ in range(length))
            file_id += 1
        else:
            # Add 'length' free blocks
            blocks.extend('.' for _ in range(length))

        expect_file = not expect_file

    # Move the rightmost file block to the leftmost '.' until no '.' is left before any file block.
    while True:
        # Find leftmost '.'
        left_dot = None
        for i, b in enumerate(blocks):
            if b == '.':
                left_dot = i
                break

        # If no free space found, we are done
        if left_dot is None:
            break

        # Find rightmost file block
        right_file = None
        for i in range(len(blocks)-1, -1, -1):
            if blocks[i] != '.':
                right_file = i
                break

        # If no file found (all free), we are done
        if right_file is None:
            break

        # If the leftmost '.' is to the right of the rightmost file block, we are done
        if left_dot > right_file:
            break

        # Move the rightmost file block to the leftmost '.'
        file_id_char = blocks[right_file]
        blocks[right_file] = '.'
        blocks[left_dot] = file_id_char

    compacted = blocks
    checksum = 0
    for i, b in enumerate(compacted):
        if b != '.':
            checksum += i * int(b)

    return checksum



def part_two(map_grid):
    pass


if __name__ == "__main__":
    file_path = "example.txt"
    file_path = "input.txt"

    disk_map = load_disk_map(file_path)
    checksum = part_one(disk_map)


    print(f'The file system\'s checksum is {checksum}.')
