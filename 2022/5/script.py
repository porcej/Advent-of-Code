import re
from pprint import pprint

test = [
	"    [D]    \n",
	"[N] [C]    \n",
	"[Z] [M] [P]\n",
	" 1   2   3 \n",
	"\n",
	"move 1 from 2 to 1\n",
	"move 3 from 1 to 3\n",
	"move 2 from 2 to 1\n",
	"move 1 from 1 to 2\n"
]
stacks = {}
in_map = True

# Part #1

with open("input.txt", "r") as _input_file:
	for line in _input_file:
	# for line in test:

		if in_map:
			if line == "\n":
				in_map = False

			else:
				positions = [str(1+int(m.start()/4))  for m in re.finditer('\[', line)]
				boxes = re.findall('[a-zA-Z]+', line)
				for idx, box in enumerate(boxes):
					stacks.setdefault(positions[idx], []).insert(0, box)
		elif line.startswith('move'):
			num_moves, stack_from, stack_to = re.findall('\d+', line)
			# print("---# Moves:{}, from:{}, to:{}".format(num_moves, stack_from, stack_to))
			for x in range(int(num_moves)):
				stacks[stack_to].append(stacks[stack_from].pop())


top_crates = "".join([boxes[-1] for key, boxes in sorted(stacks.items())])

part_1 = top_crates

# Part #2
stacks = {}
in_map = True

# Part #1

with open("input.txt", "r") as _input_file:
	for line in _input_file:
	# for line in test:

		if in_map:
			if line == "\n":
				in_map = False

			else:
				positions = [str(1+int(m.start()/4))  for m in re.finditer('\[', line)]
				boxes = re.findall('[a-zA-Z]+', line)
				for idx, box in enumerate(boxes):
					stacks.setdefault(positions[idx], []).insert(0, box)
		elif line.startswith('move'):
			num_moves, stack_from, stack_to = re.findall('\d+', line)
			print("---# Moves:{}, from:{}, to:{}".format(num_moves, stack_from, stack_to))
			last_index = 0-int(num_moves)
			stacks[stack_to].extend(stacks[stack_from][last_index:])
			stacks[stack_from] = stacks[stack_from][:last_index]
				


top_crates = "".join([boxes[-1] for key, boxes in sorted(stacks.items())])




part_2 = top_crates

print("Part 1: {}".format(part_1))
print("Part 2: {}".format(part_2))