
# Part 1
num_fully_contained = 0

test = [
	"2-4,6-8",
	"2-3,4-5",
	"5-7,7-9",
	"2-8,3-7",
	"6-6,4-6",
	"2-6,4-8"
]



with open("input.txt", "r") as _input_file:
	for line in _input_file:
		range1, range2 = line.split(",")

		chars = list(set(compartment1))
		for char in chars:
			if char in compartment2:
				priority = priority_map[char]
				sum_priority += priority
				print("{} {}: {}-{}".format(char, priority, compartment1, compartment2))
part_1 = sum_priority


# Part 2
# Config and initiliazation
group_size = 3
sum_priority = 0

with open("input.txt", "r") as _input_file:
	lines = [x.strip() for x in _input_file.readlines()]

# Take each group in sets of 
groups = zip(*(iter(lines),)*group_size)

for group in groups:
	items = list(set(group[0])) # Get all the unique items in the first line
	item = [idx for idx in items if idx in group[1] and idx in group[2]][0]
	priority = priority_map[item]
	sum_priority += priority
	print("Badge: {}, Priority: {}, Priority Sum: {}".format(item, priority, sum_priority))

part_2 = sum_priority

print("Part 1: {}".format(part_1))
print("Part 2: {}".format(part_2))