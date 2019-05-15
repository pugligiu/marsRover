
def changeOrientation(orientation, spin):
	if (orientation == 'E' and spin == 'L') or (orientation == 'W' and spin == 'R'):
		return 'N'
	if (orientation == 'S' and spin == 'L') or (orientation == 'N' and spin == 'R'):
		return 'E'
	if (orientation == 'W' and spin == 'L') or (orientation == 'E' and spin == 'R'):
		return 'S'
	if (orientation == 'N' and spin == 'L') or (orientation == 'S' and spin == 'R'):
		return 'W'


def move(x, y, orientation):
	if orientation == 'N':
		return x, y+1
	if orientation == 'E':
		return x+1, y
	if orientation == 'S':
		return x, y-1
	if orientation == 'W':
		return x-1, y


def calcFinalPos(x, maxX, y, maxY, orientation, commands):

	if x < 0 or x > maxX or y < 0 or y > maxY:
		raise ValueError("Invalid starting point")
	if orientation != 'N' and orientation != 'E' and orientation != 'S' and orientation != 'W':
		raise ValueError("Invalid orientation value")

	for c in commands:
		if c == 'M':
			x, y = move(x, y, orientation)
			if x < 0 or x > maxX or y < 0 or y > maxY:
				raise ValueError("Out of border limits")
		elif c == 'L' or c == 'R':
			orientation = changeOrientation(orientation, c)
		else:
			raise ValueError("Invalid command value")

	return x, y, orientation


if __name__ == "__main__":
   print(str(calcFinalPos(3,5,3,5,'E','MMRMMRMRRM')))
