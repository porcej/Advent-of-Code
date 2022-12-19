elves = []
current_elf = 0
elves.append(0)
with open("input.txt", "r") as _input_file:
	for line in _input_file:
		if line == "\n":
			current_elf += 1
			elves.append(0)
		else:
			elves[current_elf] += int(line)

part_1 = max(elves)
print("Part 1: {}".format(part_1))

part_2 = sum(sorted(elves, reverse=True)[0:3])
print("Part 2: {}".format(part_2))