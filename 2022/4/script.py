import re
# Part 1
num_fully_contained = 0

test = [
	"2-4,6-8",
	"2-3,4-5",
	"5-7,7-9",
	"2-8,3-7",
	"6-6,4-6",
	"2-6,4-8",
	"7-7,8-42",
]



import re
# Part 1
num_fully_contained = 0

test = [
	"2-4,6-8",
	"2-3,4-5",
	"5-7,7-9",
	"2-8,3-7",
	"6-6,4-6",
	"2-6,4-8",
	"7-7,4-5",
	"8-9,7-7"
]


with open("input.txt", "r") as _input_file:
	for line in _input_file:
	# for line in test:
		start1, end1, start2, end2 = re.split(r',|-', line.strip())
		print("{}-{},{}-{}:\t".format(start1, end1, start2, end2), end=" ")
		r1 = set(range(int(start1), int(end1)+1))
		r2 = set(range(int(start2), int(end2)+1))

		if r1.issubset(r2):
			num_fully_contained += 1
			print('Range 1 {}-{} is contianed in {}-{}'.format(start1, end1, start2, end2))
		elif r2.issubset(r1):
			num_fully_contained += 1
			print('Range 2 {}-{} is contianed in {}-{}'.format(start2, end2, start1, end1))
		else:
			print('{}-{} X {}-{}'.format(start1, end1, start2, end2))

part_1 = num_fully_contained



# Part 2
# Config and initiliazation

part_2 = 2

print("Part 1: {}".format(part_1))
print("Part 2: {}".format(part_2))