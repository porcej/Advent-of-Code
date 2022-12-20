p1_total = 0
p2_total = 0

# rock = 1 	    A   X
# paper = 2     B   Y
# scissors = 3  C   Z
win_points = 6
draw_points = 3
lose_points = 0

			#   Lose, Draw, Win	
_input_file = ["B X", "B Y", "B Z"]

# Part 1 
with open("input.txt", "r") as _input_file:
	for line in _input_file:
		p1 = ord(line[0]) - ord("A")
		p2 = ord(line[2]) - ord("X")

		# You win
		if (p1 + 1) % 3 == p2:
			p1_total += lose_points + p1 + 1
			p2_total +=  win_points + p2 + 1

		# Its a draw
		elif p1 == p2:
			p1_total +=  draw_points + p1 + 1
			p2_total +=  draw_points + p2 + 1

		# Else your opponent wins
		else:
			p1_total += win_points + p1 + 1
			p2_total += lose_points + p2 + 1

part_1 = p2_total


# Part #2
p1_total = 0
p2_total = 0

def win(x):
	return (x + 1) % 3 + 1 + win_points

def lose(x):
	return (2 + x) % 3 + 1 + lose_points

def draw(x):
	return x + 1 + draw_points

score_map = {'X': lose, 'Y': draw, 'Z': win}

with open("input.txt", "r") as _input_file:
	for line in _input_file:
		p1 = ord(line[0]) - ord("A")
		p2_total += score_map[line[2]](p1)
print("Part 1: {}".format(part_1))

part_2 = p2_total
print("Part 2: {}".format(part_2))