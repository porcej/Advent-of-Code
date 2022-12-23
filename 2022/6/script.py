test = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb"]
buffer = ""
MARKER_LENGTH = 14

def marker_strart_position(buffer, marker_length=4):
	for idx in range(marker_length, len(buffer)):
		maker = buffer[idx - marker_length:idx]
		if len(set(maker)) == marker_length:
			return idx

with open("input.txt", "r") as _input_file:
	for line in _input_file:
	# for line in test:
		buffer += line

part_1 = marker_strart_position(buffer, marker_length=4)

part_2 = marker_strart_position(buffer, marker_length=14)

print("Part 1: {}".format(part_1))
print("Part 2: {}".format(part_2))