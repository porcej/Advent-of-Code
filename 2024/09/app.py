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

def decompact_file_system(disk_map):
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

    return blocks, file_id - 1

def compute_checksum(blocks):
    checksum = 0
    for i, b in enumerate(blocks):
        if b != '.':
            checksum += i * int(b)
    return checksum

def part_one(disk_map):
    blocks, max_file_id = decompact_file_system(disk_map)

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
    checksum = compute_checksum(blocks)
    return checksum

def part_two(disk_map):
    blocks, max_file_id = decompact_file_system(disk_map)

    file_positions = {}  # file_id -> (start_index, end_index)
    current_file_id = None
    start_pos = None

    for fid in range(max_file_id + 1):
        str_fid = str(fid)
        if str_fid in blocks:
            start_pos = blocks.index(str_fid)
            end_pos = len(blocks) - 1 - blocks[::-1].index(str_fid)
            file_positions[fid] = (start_pos, end_pos)


    # Define a helper to find a suitable free span for a given file length to the left of a certain index.
    def find_free_span_left(length, limit_index):
        # Find a contiguous run of '.' of at least `length` blocks entirely located
        # to the left of `limit_index`.
        # We look from left to right for the first such span that ends before limit_index.
        count = 0
        start = 0
        best_start = None

        # We'll scan over blocks up to limit_index-1
        # We want to find a run of '.' that is big enough
        for i in range(min(limit_index, len(blocks))):
            if blocks[i] == '.':
                # print(f'\tIndex: {i} - count: {count} start: {start} length: {length}')

                # Continue a free run
                if count == 0:
                    start = i
                count += 1
                if count >= length:
                    # Found a suitable span
                    best_start = start
                    break
            else:
                # Not free, reset
                count = 0

        return best_start

    for fid in range(max_file_id, -1, -1):
        if fid not in file_positions:
            # This file has zero length, no move needed
            continue
        start_pos, end_pos = file_positions[fid]
        file_length = end_pos - start_pos + 1

        # Find a free span to the left of start_pos
        free_start = find_free_span_left(file_length, start_pos)

        if free_start is not None:
            # Move the file to [free_start, free_start+file_length-1]
            # First, clear old position
            for i in range(start_pos, end_pos+1):
                blocks[i] = '.'
            # Place file at new position
            for i in range(file_length):
                blocks[free_start + i] = str(fid)
            # Update file_positions for this file
            file_positions[fid] = (free_start, free_start + file_length - 1)

    checksum = compute_checksum(blocks)
    return checksum


if __name__ == "__main__":
    file_path = "example.txt"
    file_path = "input.txt"

    disk_map = load_disk_map(file_path)
    checksum = part_one(disk_map)
    print(f'The file system\'s checksum is {checksum}.')
    checksum = part_two(disk_map)
    print(f'The file system\'s checksum is now {checksum}.')

