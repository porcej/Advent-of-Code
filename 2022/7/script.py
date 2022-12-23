import sys

test = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


if __name__ == "__main__":
	raw_input = {}
	directory_structure = 
	if ("-h" in sys.argv[1:]) or ("--help" in sys.argv[1:]):
		print("$ python -[ht] --[test help]")
		print("\t-t, --test: runs script on test data")
		print("\t-h, --help: Displays usages")
	elif ("-t" in sys.argv[1:]) or ("--test" in sys.argv[1:]):
		pass
	else:
		with open("input.txt", "r") as _input_file:
			test = _input_file.read()

	raw_input = test.split("\n")
	test = []
	filesystem = {}
	currentpath = ""
	depth = 0
	for line in raw_input:
		parts = line.split(" ")

		if parts[0] == "$":
			# We have a command
			if parts[1] == "cd":
				if parts[3] == "\\":
					depth = 0


			elif parts[1] == "ls":


		print(line)

buffer = ""
MARKER_LENGTH = 14

# def marker_strart_position(buffer, marker_length=4):
# 	for idx in range(marker_length, len(buffer)):
# 		maker = buffer[idx - marker_length:idx]
# 		if len(set(maker)) == marker_length:
# 			return idx

# with open("input.txt", "r") as _input_file:
# 	for line in _input_file:
# 	# for line in test:
# 		buffer += line

# part_1 = marker_strart_position(buffer, marker_length=4)

# part_2 = marker_strart_position(buffer, marker_length=14)

# print("Part 1: {}".format(part_1))
# print("Part 2: {}".format(part_2))