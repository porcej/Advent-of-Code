import re
# Part 1
num_fully_contained = 0
num_contains = 0

test = [
	"2-4,6-8",
	"2-3,4-5",
	"5-7,7-9",
	"2-8,3-7",
	"6-6,4-6",
	"2-6,4-8"
]

def checkIfSubset(r1, r2):
	if r1.issubset(r2):
		return 1
	elif r2.issubset(r1):
		return 1
	else:
		return 0

def checkIntersection(r1, r2):
	if r1.isdisjoint(r2):
		return 0
	return 1
	

with open("input.txt", "r") as _input_file:
	for line in _input_file:
	# for line in test:
		start1, end1, start2, end2 = re.split(r',|-', line.strip())
		
		r1 = set(range(int(start1), int(end1)+1))
		r2 = set(range(int(start2), int(end2)+1))

		# Part #1
		num_fully_contained += checkIfSubset(r1, r2)
		
		# Part #2
		num_contains += checkIntersection(r1, r2)


		

part_1 = num_fully_contained
part_2 = num_contains

print("Part 1: {}".format(part_1))
print("Part 2: {}".format(part_2))